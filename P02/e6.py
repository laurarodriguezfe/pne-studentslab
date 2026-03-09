from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 5 |------")
IP = "127.0.0.1"
PORT = 8080
PORT2 = 8081
c = Client(IP, PORT)
c2 = Client(IP, PORT2)
print(c)
print(c2)
folder = "../P00/sequences/"
gene_name = "FRAT1"
s = Seq()
s.read_fasta(folder + gene_name + ".txt")
print(f"Sending {gene_name} Gene to the server...")
fragments = c.cut(str(s))
print(f"Gene {gene_name}: {s}")

for t in range(len(fragments)):
    a = t + 1
    s = fragments[t]
    print(f"Fragment {a}: {s}")
    mes = f"Fragment {a}: {s}"
    if a % 2 != 0:
        response = c.talk(mes)
    else:
        response = c2.talk(mes)