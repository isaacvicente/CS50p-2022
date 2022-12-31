user_input = input("Input: ")

output = ""

for character in user_input:
    c = character.lower()
    if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
        output += character

print(f"Output: {output}")
