import socket
from P01.Seq1 import Seq

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    (cs, client_ip_port) = ls.accept()

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode().strip()
    parts = msg.split()
    sequence = parts[1]
    print(f"Message received: {msg}")

    if parts[0] == "PING":
        print("PING command!")

        response = "OK!\n"
        print(response)
        cs.send(response.encode())

    elif parts[0] == "GET":
        print("GET command!")

        n = int(parts[1])

        if n == 0:
            response = "ATCAGATACTTGA\n"
        elif n == 1:
            response = "AGATAGAGCGATA\n"
        elif n == 2:
            response = "TAGACCAGATATA\n"
        elif n == 3:
            response = "CTAGACTGAAGAT\n"
        elif n == 4:
            response = "TAGACATGAATCA\n"
        else:
            response = "Invalid number"

        print(response)
        cs.send(response.encode())

    elif parts[0] == "INFO":
        print("INFO command!")

        seq = Seq(sequence)

        length = seq.len()
        counts = seq.count()

        response = f"Sequence: {sequence}\nTotal length: {length}\n"

        for base, count in counts.items():
            percentage = (count / length * 100)
            response += f"{base}: {count} ({round(percentage, 2)}%)\n"

        print(response)
        cs.send(response.encode())

    elif parts[0] == "COMP":
        print("COMP command!")
        seq = Seq(sequence)
        response = seq.complement()
        print(response)
        cs.send(response.encode())

    elif parts[0] == "REV":
        print("REV command!")
        seq = Seq(sequence)
        response = seq.reverse()
        print(response)
        cs.send(response.encode())

    elif parts[0] == "GENE":
        print("GENE command!")
        folder = "../sequences/"
        g = parts[1]
        filename = f"{g}.txt"
        full_path = folder + filename
        seq = Seq()
        sequence = seq.read_fasta(full_path)
        response = sequence + "\n"
        print(response)
        cs.send(response.encode())
    else:
        print("Command not found!")

    cs.close()