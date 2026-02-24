class Seq:
    def __init__(self, bases):
        self.bases = bases
        valid_bases = ['A', 'C', 'G', 'T']
        total = 0
        for i in bases:
            if i in valid_bases:
                total += 1
        if total == len(bases):
            self.bases = bases
            print("New sequence created!!")
        else:
            self.bases = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.bases

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")

