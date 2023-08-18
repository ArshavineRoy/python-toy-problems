def positive_numbers(a, b, c):
    matches = [num for num in [a, b, c]  if num > 0]
    return True if len(matches) == 2 else False


print ("Enter your integer values below")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

result = positive_numbers(a, b, c)
print("Input has only two positive numbers:", result)
