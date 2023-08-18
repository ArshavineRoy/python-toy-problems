import re

def highest_consonant(string):
    if string:
        substrings = re.findall(r"[^aeiou\d\W]+", string.lower())

        substring_totals = []

        for substring in substrings:
            total_unicode = 0
            for char in substring:
                total_unicode += (ord(char) - 96)
            substring_totals.append(total_unicode)
        return print(max(substring_totals))
    else:
        return print("You entered an empty string!")

highest_consonant(input("Enter a string: "))

