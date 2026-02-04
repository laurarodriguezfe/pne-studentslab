def fibonacci():
    a = 0
    b = 1
    i = 2
    while i < 15:
        c = a + b
        a = b
        b = c
        i += 1
        if i == 5:
            print("The 5th fibonacci element is:", c)
        elif i == 10:
            print("The 10th fibonacci element is:", c)
        elif i == 15:
            print("The 15th fibonacci element is:", c)

fibonacci()
