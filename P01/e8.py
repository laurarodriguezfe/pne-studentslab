from Seq1 import Seq

print("-----| Practice 1, Exercise 8 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}\nBases: {s1.count()}\nRev: {s1.reverse()}\nComp: {s1.complement()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}\nBases: {s2.count()}\nRev: {s2.reverse()}\nComp: {s2.complement()}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}\nBases: {s3.count()}\nRev: {s3.reverse()}\nComp: {s3.complement()}")