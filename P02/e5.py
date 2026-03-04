from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 5 |------")
IP = "212.128.255.79"
PORT = 8080
c = Client(IP, PORT)
print(c)
folder = "../P00/sequences/"
gene_name = "FRAT1"
s = Seq()
s.read_fasta(folder + gene_name + ".txt")
print(f"Gene {gene_name}: {str(s)[:76]}...")
sequence = str(s)

for i in range(5):
    start = i * 10
    end = start + 10
    fragment = sequence[start:end]
    print(f"Fragment {i+1}: {fragment}")
    c.talk(fragment)