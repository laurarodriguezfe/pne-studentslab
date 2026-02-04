def fibosum(n):
    a = 0
    b = 1
    sum = 1
    i = 2
    while i < n:
        c = a + b
        sum += c
        a = b
        b = c
        i += 1
    return sum

print("The sum of the first 5 elements of the fibonacci series is:", fibosum(5))
print("The sum of the first 10 elements of the fibonacci series is:", fibosum(10))