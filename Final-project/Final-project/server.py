import http.server
import http.client
import socketserver
import termcolor
import jinja2 as j
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8080
SERVER = "rest.ensembl.org"
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_data(endpoint):
    conn = http.client.HTTPSConnection(SERVER)
    PARAMS = "?content-type=application/json"
    conn.request("GET", endpoint + PARAMS)
    res = conn.getresponse()
    if res.status == 200:
        data = json.loads(res.read().decode("utf-8"))
    else:
        data = {}
    conn.close()
    return data

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, "green")
        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/":
            contents = Path("html/index.html").read_text()
            self.send_response(200)

        elif path == "/listSpecies":
            args = parse_qs(url_path.query)
            limit = args.get("seq", [""])[0]
            conn = http.client.HTTPSConnection("rest.ensembl.org")
            conn.request("GET", "/info/species?content-type=application/json")

            res = conn.getresponse()
            data = json.loads(res.read().decode("utf-8"))
            conn.close()
            species = data["species"]

            if limit == "":
                n = len(species)
            else:
                n = int(limit)

            result = ""

            for sp in species[:n]:
                result += sp["name"] + "<br>"

            contents = read_html_file("species.html").render(context={"result": result})

            self.send_response(200)

        else:
            contents = Path("html/error.html").read_text()
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