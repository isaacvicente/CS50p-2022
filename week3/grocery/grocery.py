grocery_list = {}

while True:
    try:
        item = input().lower()
    except EOFError:
        break
    else:
        try:
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1

print()
for food in sorted(list(grocery_list)):
    print(f"{grocery_list[food]} {food.upper()}")
