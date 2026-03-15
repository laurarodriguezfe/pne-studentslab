from P02.Client0 import Client


IP = "127.0.0.1"
PORT = 8080

def main():
    c = Client(IP, PORT)
    print(c)

    print("* Testing PING...")
    print(c.talk("PING").strip())

    print("\n* Testing GET...")
    seq0 = c.talk("GET 0").strip()
    print(f"GET 0: {seq0}")
    for i in range(1, 5):
        res = c.talk(f"GET {i}").strip()
        print(f"GET {i}: {res}")

    print("\n* Testing INFO...")
    print(f"Sequence: {seq0}")
    print(c.talk(f"INFO {seq0}").strip())

    print("\n* Testing COMP...")
    print(f"COMP {seq0}")
    print(c.talk(f"COMP {seq0}").strip())

    print("\n* Testing REV...")
    print(f"REV {seq0}")
    print(c.talk(f"REV {seq0}").strip())

    print("\n* Testing GENE...")
    genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
    for g in genes:
        full_response = c.talk(f"GENE {g}").strip()
        print(f"GENE {g}")
        print(full_response)

if __name__ == "__main__":
    main()