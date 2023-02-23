import re

text = "Hello, my name is Alice. What's your name?"

# find all occurrences of the word "name" in the text
matches = re.findall(r"name", text)

# replace all occurrences of "name" with "nickname"
new_text = re.sub(r"name", "nickname", text)

print(matches)   # Output: ['name', 'name']
print(new_text)  # Output: Hello, my nickname is Alice. What's your nickname?
