import http.client
import json
from e2 import genes
from P01.Seq1 import Seq

SERVER = "rest.ensembl.org"

def all_genes_info():
    conn = http.client.HTTPSConnection(SERVER)

    for gene_name in genes:
        gene_id = genes[gene_name]

        ENDPOINT = f"/sequence/id/{gene_id}"
        PARAMS = "?content-type=application/json"
        URL = SERVER + ENDPOINT + PARAMS

        try:
            conn.request("GET", ENDPOINT + PARAMS)
            res = conn.getresponse()

            print("\n" + "-"*40)
            print(f"Gene: {gene_name}")
            print(f"Server: {SERVER}")
            print(f"URL: {URL}")
            print(f"Response received!: {res.status} {res.reason}")
            print()

            if res.status == 200:
                data = json.loads(res.read().decode("utf-8"))
                sequence = data.get("seq")
                description = data.get("desc")

                seq = Seq(sequence)

                print(f"Description: {description}")
                print(f"Total length: {seq.len()}")

                counts = seq.count()
                for base in counts:
                    if seq.len() > 0:
                        percent = round((counts[base] / seq.len()) * 100, 2)
                    else:
                        percent = 0
                    print(f"{base}: {counts[base]} ({percent}%)")

                print(f"Most frequent base: {seq.most_frequent_base()}")

            else:
                print("Error retrieving data!")

        except Exception as e:
            print(f"Error: {e}")

    conn.close()

if __name__ == "__main__":
    all_genes_info()