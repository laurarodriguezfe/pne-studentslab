from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 6 |------")
    print("\nGene U5")
    FOLDER = "sequences/"
    FILENAME = "U5.txt"
    file_contents = Path(FOLDER + FILENAME).read_text()
    print(f"REVERSE: {seq_reverse(file_contents, 20)}")