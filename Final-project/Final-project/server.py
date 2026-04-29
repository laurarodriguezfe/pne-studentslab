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
            params = parse_qs(url_path.query)
            limit = params.get("limit", [""])[0]
            data = get_data("/info/species")
            all_species = data["species"]
            total_species = len(all_species)

            #print("Q:", url_path.query)
            #print("P:", params)
            #print("L:", limit)

            names = []
            for s in all_species:
                names.append(s["display_name"])

            if limit != "":
                names = names[:int(limit)]
                display_limit = limit
            else:
                display_limit = "All"

            species_html = ""
            for n in names:
                species_html += f"<li>{n}</li>"

            contents = read_html_file("species.html").render(info={"list": species_html, "total": total_species, "limit": display_limit})
            self.send_response(200)

        elif path == "/karyotype":
            params = parse_qs(url_path.query)
            species = params.get("species", [""])[0]
            data = get_data(f"/info/assembly/{species}")
            chromosomes = data.get("karyotype", [])

            print("S:", species)

            result = ""
            for c in chromosomes:
                result += f"<li>{c}</li>"

            contents = read_html_file("karyotype.html").render(info={"result": result})

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