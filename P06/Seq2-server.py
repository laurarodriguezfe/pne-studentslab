import http.server
import socketserver
import termcolor
import jinja2 as j
from pathlib import Path
from urllib.parse import parse_qs, urlparse


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def read_gene_file(gene_name):
    path = Path("genes/" + gene_name + ".txt").read_text()
    return path

def sequence_info(seq):
    length = len(seq)
    a = seq.count("A")
    c = seq.count("C")
    g = seq.count("G")
    t = seq.count("T")
    return f"Length: {length}\nA: {a} | C: {c} | G: {g} | T: {t}"

def complement(seq):
    comp_dict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"}
    comp = ""
    for base in seq:
        if base in comp_dict:
            comp += comp_dict[base]
    return comp

def reverse(seq):
    return seq[::-1]

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/":
            contents = Path('html/index.html').read_text()
            self.send_response(200)

        elif path == "/ping":
            contents = f"""
            <!DOCTYPE html>
            <html>
            <body>
                <h1>PING OK!</h1>
                <p>The SEQ2 server is running...</p>
                <a href="/">Main page</a>
            </body>
            </html>
            """

            self.send_response(200)

        elif path == "/get":
            arguments = parse_qs(url_path.query)
            msg = arguments.get("n", [""])[0]
            n = int(msg)
            if 0 <= n <= 4:
                sequences = {
                    0: "GAGGAGGGACCCATACAGATCAGTAGAGCGATGAGC",
                    1: "ACAGACATAGCAGTAGACATATAGACAGTAGACGAT",
                    2: "GACCAGATACGATACGATACGATCAGATCAGATCGA",
                    3: "GTAGGGGACCAGTACAGTGACGATACGATAGATCAG",
                    4: "ACTAGATACAGTAGCAGATCAGGAAATGATACGATA"}
                seq = sequences[n]
            contents = read_html_file("get.html").render(context={"n": n, "sequence": seq})

            self.send_response(200)

        elif path == "/gene":
            arguments = parse_qs(url_path.query)
            gene_name = arguments.get("name", [""])[0]
            valid_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
            if gene_name in valid_genes:
                gene = read_gene_file(gene_name)
                contents = read_html_file("gene.html").render(context={"name": gene_name, "gene": gene})

                self.send_response(200)

        elif path == "/operation":
            arguments = parse_qs(url_path.query)
            seq = arguments.get("seq", [""])[0]
            op = arguments.get("op", [""])[0]
            op = int(op)
            if seq != "" and op in [1, 2, 3]:
                if op == 1:
                    result = sequence_info(seq)
                elif op == 2:
                    result = complement(seq)
                elif op == 3:
                    result = reverse(seq)
                contents = read_html_file("operation.html").render(context={"sequence": seq, "operation": op, "result": result})

                self.send_response(200)

        else:
            contents = Path('html/error.html').read_text()

            self.send_response(404)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()