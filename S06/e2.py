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
    def len(self):
        return len(self.bases)
    def __str__(self):
        return self.bases

def print_seqs(seq_list):
    n = 0
    for i in seq_list:
        print(f"Sequence {n}: (Lenght: {i.len()}) {i}")
        n += 1

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)