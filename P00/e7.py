from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 7 |------")
    print("\nGene U5")
    FOLDER = "sequences/"
    FILENAME = "U5.txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    print(f"Comp: {seq_complement(file_contents)}")