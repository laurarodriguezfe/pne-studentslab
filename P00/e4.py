from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    FOLDER = "sequences/"
    FILENAME = ["U5", "ADA", "FRAT1", "FXN"]
    print("-----| Exercise 4 |------")
    for g in FILENAME:
        file_name = g + ".txt"
        file = Path(FOLDER + file_name).read_text()
        BASES = ["A", "C", "G", "T"]
        print(f"\nGene {g}:")
        for base in BASES:
            print(f"   {base}: {seq_count_base(file, base)}")