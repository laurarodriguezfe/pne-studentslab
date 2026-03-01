from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.len()}) {s1}\n  A: {s1.count_base('A')},  C: {s1.count_base('C')},  T: {s1.count_base('T')},  G: {s1.count_base('G')}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}\n  A: {s2.count_base('A')},  C: {s2.count_base('C')},  T: {s2.count_base('T')},  G: {s2.count_base('G')}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}\n  A: {s3.count_base('A')},  C: {s3.count_base('C')},  T: {s3.count_base('T')},  G: {s3.count_base('G')}")