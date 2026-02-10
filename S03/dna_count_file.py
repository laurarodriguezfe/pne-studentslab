#lines = {"AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"}
#print("From variable:", lines
from dna_count import count_bases #to import a function of another file without the need to paste it REMEMBER YOU CAN'T HAVE ANYTHING GON YOUR LEFT", that's why we put "if __name__ == "__main__":"

#option 1
f = open("dna.txt", "r") # Opening the file
lines = f.readlines()
f.close() # If we open the file this way we have to remember to close the function!!

#option 2
with open("dna.txt", "r") as f: # This is a way where we don't have to remember to close the open function "f.close()"
    lines = f.readlines()

total_number = 0
bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for sequence in lines:
    sequence = sequence.strip() # Remove spaces and newline characters at the end of the string
    total_number += len(sequence)

    result = count_bases(seq)

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(F"{base}: {count}")
