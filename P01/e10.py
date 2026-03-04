from Seq1 import Seq
from pathlib import Path

if __name__ == "__main__":
    print("-----| Practice 1, Exercise 10 |------")
    genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
    folder = "sequences/"
    for g in genes:
        s1 = Seq()
        s1.read_fasta(folder + g + ".txt")
        most_frequent = s1.most_frequent_base()
        print(f"Gene {g}: Most frequent Base: {most_frequent}")