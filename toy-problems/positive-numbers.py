def positive_numbers(a, b, c):
    matches = [num for num in [a, b, c]  if num > 0]
    return True if len(matches) == 2 else False

try:
    print ("Enter inputs for values of a, b, c.")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    
    result = positive_numbers(a, b, c)
    print(result)

except ValueError:
    print("Please enter integer values only!")