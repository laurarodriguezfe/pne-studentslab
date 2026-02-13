dna = "ATGCGATCGATCGATCGATCGA"

print("Length:", len(dna))

print("First 5:", dna[:5])

print("Last 3:", dna[len(dna)-3:])

print("Lowercase:", dna.lower())

print("ATC count:", dna.count("ATC"))

rna = ""
for n in dna:
    if n == "T":
        rna += "U"
    else:
        rna += n
print("RNA:", rna)