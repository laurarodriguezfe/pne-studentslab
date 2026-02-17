from functools import partial
from pathlib import Path
FILENAME = "sequences/ADA_EXONS.txt"
file_contents = Path(FILENAME).read_text()
split_txt = file_contents.split("\n")
bases = ""
n = 0
for i in split_txt:
    if not split_txt[n].startswith(">"):
        bases += split_txt[n]
        bases += " "
    n += 1
split_bases = file_contents.split(" ")
print(split_bases[1])
