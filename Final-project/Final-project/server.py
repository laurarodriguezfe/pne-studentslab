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
    PARAMS = "content-type=application/json"
    conn.request("GET", endpoint + PARAMS)
    res = conn.getresponse()
    if res.status == 200:
        data = json.loads(res.read().decode("utf-8"))
    else:
        data = {}
    conn.close()
    return data

def clean_param(params):
    param = params.replace(" ", "%20")
    return param

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, "green")
        url_path = urlparse(self.path)
        path = url_path.path

        if path == "/":
            contents = Path("html/index.html").read_text()
            self.send_response(200)

        elif path == "/listSpecies":
            try:
                params = parse_qs(url_path.query)
                limit = params.get("limit", [""])[0]
                data = get_data("/info/species?")
                all_species = data["species"]
                total_species = len(all_species)

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

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/karyotype":
            try:
                params = parse_qs(url_path.query)
                species = clean_param(params.get("species", [""])[0])
                if not species:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/info/assembly/{species}?")
                    chromosomes = data.get("karyotype", None)

                    if chromosomes == None:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)
                    else:
                        result = ""
                        for c in chromosomes:
                            result += f"<li>{c}</li>"

                        contents = read_html_file("karyotype.html").render(info={"result": result})

                        self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/chromosomeLength":
            try:
                params = parse_qs(url_path.query)
                species = clean_param(params.get("species", [""])[0])
                chromo = params.get("chromo", [""])[0]
                if not species or not chromo:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/info/assembly/{species}?")
                    regions = data.get("top_level_region", None)
                    length = ""

                    if regions == None:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)
                    else:
                        for r in regions:
                            if r["name"] == chromo:
                                length = r["length"]

                        contents = read_html_file("chromosome.html").render(info={"length": length})

                        self.send_response(200)
            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/geneLookup":
            try:
                params = parse_qs(url_path.query)
                gene = params.get("gene", [""])[0]

                if not gene:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/lookup/symbol/homo_sapiens/{gene}?")
                    gene_id = data.get("id", None)

                    if gene_id is None:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)
                    else:
                        contents = read_html_file("geneLookup.html").render(info={"gene": gene, "id": gene_id})
                        self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/geneSeq":
            try:
                params = parse_qs(url_path.query)
                gene = params.get("gene", [""])[0]

                if not gene:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/lookup/symbol/homo_sapiens/{gene}?")
                    gene_id = data.get("id", None)

                    if gene_id is None:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)
                    else:
                        data_seq = get_data(f"/sequence/id/{gene_id}?")
                        sequence = data_seq.get("seq", None)

                        if sequence is None:
                            contents = Path("html/error.html").read_text()
                            self.send_response(404)
                        else:
                            contents = read_html_file("geneSeq.html").render(info={"gene": gene, "seq": sequence})
                            self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/geneInfo":
            try:
                params = parse_qs(url_path.query)
                gene = params.get("gene", [""])[0]

                if not gene:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/lookup/symbol/homo_sapiens/{gene}?")
                    gene_id = data.get("id", None)
                    start = data.get("start", None)
                    end = data.get("end", None)
                    chromo = data.get("seq_region_name", None)

                    if None in (gene_id, start, end, chromo):
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)

                    else:
                        length = int(end) - int(start)
                        contents = read_html_file("geneInfo.html").render(info={"gene": gene, "id": gene_id, "start": start, "end": end, "length": length, "chromo": chromo})

                        self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/geneCalc":
            try:
                params = parse_qs(url_path.query)
                gene = params.get("gene", [""])[0]

                if not gene:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    data = get_data(f"/lookup/symbol/homo_sapiens/{gene}?")
                    gene_id = data.get("id", None)

                    if gene_id is None:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)

                    else:
                        data_seq = get_data(f"/sequence/id/{gene_id}?")
                        sequence = data_seq.get("seq", None)

                        if sequence is None:
                            contents = Path("html/error.html").read_text()
                            self.send_response(404)

                        else:
                            data_seq = get_data(f"/sequence/id/{gene_id}?")
                            sequence = data_seq.get("seq", None)

                            if sequence is None:
                                contents = Path("html/error.html").read_text()
                                self.send_response(404)

                            else:
                                length = len(sequence)
                                bases = {"A": 0, "C": 0, "T": 0, "G": 0}
                                for b in sequence:
                                    if b in bases:
                                        bases[b] += 1
                                    perc = {}

                                    for b in bases:
                                        if length > 0:
                                            perc[b] = round((bases[b] / length) * 100, 2)
                                        else:
                                            perc[b] = 0
                                    contents = read_html_file("geneCalc.html").render(info={"gene": gene, "length": length, "A": perc["A"], "C": perc["C"], "G": perc["G"], "T": perc["T"]})

                                self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

        elif path == "/geneList":
            try:
                params = parse_qs(url_path.query)
                chromo = params.get("chromo", [""])[0]
                start = params.get("start", [""])[0]
                end = params.get("end", [""])[0]

                if not chromo or not start or not end:
                    contents = Path("html/error.html").read_text()
                    self.send_response(404)

                else:
                    endpoint = f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;"
                    data = get_data(endpoint)

                    if not data:
                        contents = Path("html/error.html").read_text()
                        self.send_response(404)

                    else:
                        result = ""
                        genes = data
                        print(genes)
                        for g in genes:
                            gene_id = g.get("id", "")
                            gene_name = g.get("external_name", "")
                            result += f"{gene_id}: {gene_name}<br>"
                        contents = read_html_file("geneList.html").render(info={"result": result})

                        self.send_response(200)

            except Exception as e:
                contents = f"<h1>Internal Error: {e}</h1>"
                self.send_response(500)

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