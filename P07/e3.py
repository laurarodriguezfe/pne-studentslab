import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
GENE_NAME = "MIR633"
GENE_ID = genes[GENE_NAME]

ENDPOINT = f"/sequence/id/{GENE_ID}"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

def gene_data():
    conn = http.client.HTTPSConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
        res = conn.getresponse()

        print()
        print(f"Server: {SERVER}")
        print(f"URL: {URL}")
        print(f"Response received!: {res.status} {res.reason}")
        print()

        if res.status == 200:
            data = json.loads(res.read().decode("utf-8"))
            print(f"Gene ID: {GENE_NAME}")
            print(f"Description: {data.get('desc')}")
            print(f"Sequence: {data.get('seq')}")
        else:
            print("An error ocurred!")

    except Exception as e:
        print(f"An error occurred: {e}")

    conn.close()

if __name__ == "__main__":
    gene_data()