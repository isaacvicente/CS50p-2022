import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        names.append(name)

print(f"Adieu, adieu, to {p.join(names)}")
