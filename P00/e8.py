from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("-----| Exercise 8 |------")
    FOLDER = "sequences/"
    FILENAME = ["U5", "ADA", "FRAT1", "FXN"]
    for g in FILENAME:
        file_name = g + ".txt"
        file = Path(FOLDER + file_name).read_text()
        print(f"Gene {g}: Most frequent base: {most_frequent_base(file)}")