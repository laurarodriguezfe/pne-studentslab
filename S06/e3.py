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

def generate_seqs(seq, n):
    seq_list = []
    for i in range(1, n + 1):
        new_seq = Seq(seq * i)
        seq_list.append(new_seq)
    return seq_list

def print_seqs(seq_list):
    n = 0
    for i in seq_list:
        print(f"Sequence {n}: (Lenght: {i.len()}) {i}")
        n += 1

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)
print("\nList 1:")
print_seqs(seq_list1)
print("\nList 2:")
print_seqs(seq_list2)