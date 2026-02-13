def score(n):
    if 9 <= n <= 10:
        result = "A"
    elif 7 <= n <= 8.9:
        result = "B"
    elif 5 <= n <= 6.9:
        result = "C"
    elif 3 <= n <= 4.9:
        result = "D"
    elif 0<= n <= 2.9:
        result = "F"
    else:
        result = "Not a valid score"
    return result

s = int(input("Enter a score:"))
print("Score", s, "->", score(s))
