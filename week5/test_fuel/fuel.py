def main():
    while True:
        fraction = input("Fraction: ")
        try:
            perc = convert(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    print(gauge(perc))


def convert(fraction):
    try:
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError
    else:
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
