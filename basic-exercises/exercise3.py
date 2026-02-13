temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

print("Wednesday:", temperatures[2])

print("Max:", max(temperatures))

print("Min:", min(temperatures))

total = 0
num = 0
for n in temperatures:
    total += n
    num += 1
average = round((total / num), 1)
print("Average:", average)

above = []
for t in temperatures:
    if t > 17:
        above.append(t)
print("Days above:", above)

print("Sorted:", sorted(temperatures))