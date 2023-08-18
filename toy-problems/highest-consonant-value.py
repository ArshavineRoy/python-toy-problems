import re

def highest_consonant(string):
    substrings = re.findall(r"[^aeiou\d\W]+", string.lower())

