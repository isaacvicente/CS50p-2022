while True:
    fraction = input("Fraction: ")
    try:
        numer, denom = fraction.split("/")

        numer = int(numer)
        denom = int(denom)

        porc = round((numer / denom) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if numer <= denom:
            break

if porc <= 1:
    print("E")
elif porc >= 99:
    print("F")
else:
    print(f"{round(porc)}%")
