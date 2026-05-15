import http.client
import json

SERVER = "localhost:8080"

while True:
    print("\nGENOME CLIENT")
    print("-------------------")
    print("1. List Species")
    print("2. Karyotype")
    print("3. Chromosome Length")
    print("4. Gene Lookup")
    print("5. Gene Sequence")
    print("6. Gene Info")
    print("7. Gene Calc")
    print("8. Gene List")
    print("0. Exit")

    option = input("Choose an option: ")

    if option == "0":
        print("Exit client")
        break

    endpoint = ""

    if option == "1":
        limit = input("Limit: ")
        endpoint = f"/listSpecies?limit={limit}&json=1"

    elif option == "2":
        species = input("Species: ")
        endpoint = f"/karyotype?species={species}&json=1"

    elif option == "3":
        species = input("Species: ")
        chromo = input("Chromosome: ")
        endpoint = f"/chromosomeLength?species={species}&chromo={chromo}&json=1"

    elif option == "4":
        gene = input("Gene: ")
        endpoint = f"/geneLookup?gene={gene}&json=1"

    elif option == "5":
        gene = input("Gene: ")
        endpoint = f"/geneSeq?gene={gene}&json=1"

    elif option == "6":
        gene = input("Gene: ")
        endpoint = f"/geneInfo?gene={gene}&json=1"

    elif option == "7":
        gene = input("Gene: ")
        endpoint = f"/geneCalc?gene={gene}&json=1"

    elif option == "8":
        chromo = input("Chromosome: ")
        start = input("Start: ")
        end = input("End: ")
        endpoint = f"/geneList?chromo={chromo}&start={start}&end={end}&json=1"

    else:
        print("Invalid option")

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", endpoint)
    res = conn.getresponse()

    try:
        data = json.loads(res.read().decode())
        print("\nRESULT:")
        print(data)

    except Exception as e:
        print("Error reading response:", e)

    conn.close()