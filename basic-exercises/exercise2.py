text = "  Hello, World! Welcome to Python Programming.  "

stripped_text = text.strip()
print("Stripped:", stripped_text)

words = stripped_text.split()
print("Word count:", len(words))

print("Title case:", stripped_text.title())

print("Starts with Hello:", stripped_text.startswith("Hello"))

print("Ends with ing.:", stripped_text.endswith("ing."))

print("Python position:", stripped_text.find("Python"))

print("Joined:", " - ".join(words))
