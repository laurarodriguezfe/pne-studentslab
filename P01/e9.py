from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s1 = Seq()
s1.read_fasta("sequences/U5.txt")
print(f"Sequence: (Length: {s1.len()}) {s1}\n  Bases: {s1.count()}\n  Rev: {s1.reverse()}\n  Comp: {s1.complement()}")