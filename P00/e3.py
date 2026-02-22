from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    FOLDER = "sequences/"
    FILENAME = ["U5", "ADA", "FRAT1", "FXN"]
    print("-----| Exercise 3 |------")
    for g in FILENAME:
        file_name = g + ".txt"
        file = Path(FOLDER + file_name).read_text()
        print("Gene", g, "-> Length:", seq_len(file))