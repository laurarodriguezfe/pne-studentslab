def analyze(seq):
    leng = len(seq)
    a = 0
    c = 0
    t = 0
    g = 0
    for n in seq:
        if n == "A":
            a += 1
        elif n == "C":
            c += 1
        elif n == "T":
            t += 1
        else:
            g += 1
    return leng, a, c, t, g


dna = str(input("Enter a dna sequence:")).upper()
lenght, a, c, t, g = analyze(dna)
print("A:", a, "\nC:", c, "\nT:", t, "\nG:", g)



############
def count_bases(sequence):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in sequence:
        if base in bases:
            bases[base] += 1
    return bases

if __name__ == "__main__":

    sequence = input("Introduce the sequence: ").upper()
    print(f"Total length: {len(sequence)}")

    result = count_bases(sequence)

    for base, count in result.items():
        print(f"{base}: {count}")
