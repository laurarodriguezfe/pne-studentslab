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
            msg = arguments.get("id", [""])[0]
            g_name = int(msg)
            if 0 <= g_name <= 4:
                genes = {
                    0: ADA,
                    1: FRAT1,
                    2: FXN,
                    3: RNU6_269P,
                    4: U5
                }
                gene = genes[g_name]
            contents = read_html_file("gene.html").render(context={"id": g_name, "gene": gene})

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