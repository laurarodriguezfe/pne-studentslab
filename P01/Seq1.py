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
    def count_base(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return {"A": 0, "C": 0, "T": 0, "G": 0}
        else:
            base_counts = {"A": 0, "C": 0, "T": 0, "G": 0}
            for b in self.bases:
                if b in base_counts:
                    base_counts[b] += 1
            return base_counts
    def __str__(self):
        return self.bases

