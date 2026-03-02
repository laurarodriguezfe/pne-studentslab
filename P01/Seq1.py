from pathlib import Path

class Seq:
    def __init__(self, bases=None):
        if bases is None:
            self.bases = "NULL"
            print("NULL sequence created")
        else:
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
                print("INVALID sequence created")
    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)
    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            base_counts = {"A": 0, "C": 0, "T": 0, "G": 0}
            for b in self.bases:
                if b in base_counts:
                    base_counts[b] += 1
            return base_counts[base]
    def count(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return {"A": 0, "C": 0, "T": 0, "G": 0}
        else:
            base_counts = {"A": 0, "C": 0, "T": 0, "G": 0}
            for b in self.bases:
                if b in base_counts:
                    base_counts[b] += 1
            return base_counts
    def reverse(self):
        if self.bases == "NULL":
            return "NULL"
        elif self.bases == "ERROR":
            return "ERROR"
        else:
            return self.bases[::-1]
    def complement(self):
        if self.bases == "NULL":
            return "NULL"
        elif self.bases == "ERROR":
            return "ERROR"
        else:
            base_replace = {"A": "T", "T": "A", "C": "G", "G": "C"}
            complement_chain = ""
            for b in self.bases:
                complement_chain += base_replace[b]
            return complement_chain
    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        file_split = file_contents.split("\n")
        body = "".join(file_split[1:])
        self.bases = body
        return self.bases
    def most_frequent_base(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return None
        else:
            bases = {"A": 0, "T": 0, "C": 0, "G": 0}
            for base in self.bases:
                if base in bases:
                    bases[base] += 1
            most_frequent = max(bases, key=bases.get)
            return most_frequent
    def __str__(self):
        return self.bases

