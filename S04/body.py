from pathlib import Path
FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
n = file_contents.find("\n")
print(file_contents[n:])