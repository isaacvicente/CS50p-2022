camel_case = input("camelCase: ")
snake_case = ""

for character in camel_case:
    if character.isupper():
        snake_case += f"_{character.lower()}"
    else:
        snake_case += character

print(f"snake_case: {snake_case}")
