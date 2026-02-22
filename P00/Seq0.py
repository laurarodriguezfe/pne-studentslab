def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    n = filename.find("\n")
    body = filename[n:]
    bases = body.replace("\n", "")
    return bases

def seq_len(seq):
    n = seq.find("\n")
    body = seq[n:]
    bases = body.replace("\n", "")
    return len(bases)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases

def seq_reverse(seq, n):
    i = seq.find("\n")
    body = seq[i:]
    bases = body.replace("\n", "")
    seq_n = bases[:n]
    reversed_seq = seq_n[::-1]
    print(f"FRAGMENT: {seq_n}")
    return reversed_seq

def seq_complement(seq):
    i = seq.find("\n")
    body = seq[i:]
    bases = body.replace("\n", "")
    seq_20 = bases[:20]
    base_replace = {"A" : "U", "T" : "A", "C" : "G", "G" : "C"}
    complement_chain = ""
    print("Frag:", seq_20)
    for b in seq_20:
        complement_chain += base_replace.get(b, b)
    return complement_chain

def most_frequent_base(seq):
    bases = {"A": 0, "T": 0, "C": 0, "G": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    most_frequent = None
    highest_count = -1
    for base, count in bases.items():
        if count > highest_count:
            most_frequent = base
            highest_count = count
    return most_frequent