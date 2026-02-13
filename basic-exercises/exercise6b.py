def triangles(a, b, c):
    if a == b == c:
        result = "equilateral"
    elif a == b or a == c or b == c:
        result = "isosceles"
    else:
        result = "scalene"
    return result

side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))

print("classify_triangle(", side_a, ",", side_b, ",", side_c, ") =", triangles(side_a, side_b, side_c))