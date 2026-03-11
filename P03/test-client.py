from P02.Client0 import Client


IP = "127.0.0.1"
PORT = 8080

print(f"Connection to SERVER at {IP}, PORT: {PORT}")

c = Client(IP, PORT)

print("* Testing PING...")
response = c.talk("PING")
print(response)

print("\n* Testing GET...")
sequences = []
for i in range(5):
    msg = f"GET {i}"
    seq = c.talk(msg)
    sequences.append(seq)
    print(f"GET {i}: {seq}")

seq0 = sequences[0]

print("\n* Testing INFO...")
info = c.talk(f"INFO {seq0}")
print(info)

print("* Testing COMP...")
comp = c.talk(f"COMP {seq0}")
print(comp)

print("* Testing REV...")
rev = c.talk(f"REV {seq0}")
print(rev)

print("* Testing GENE...")
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for g in genes:
    gene_seq = c.talk(f"GENE {g}")
    print(f"GENE {g}\n{gene_seq}\n")