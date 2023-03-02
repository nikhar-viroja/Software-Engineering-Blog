import re

text = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
match = re.search(pattern, text)
print(match.start(), match.end())  # Output: 10 15
