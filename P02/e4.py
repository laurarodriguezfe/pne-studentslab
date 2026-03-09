from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 4 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)
folder = "../P00/sequences/"
genes = ["U5", "ADA", "FRAT1"]
s = Seq()
for g in genes:
    print(f"\nSending the {g} Gene to the server...")
    s.read_fasta(folder + g + ".txt")
    print("From server:")
    response = c.talk(s.__str__())
    print(f"To server: {s.__str__()}")
    print(f"Response:\n{response}")