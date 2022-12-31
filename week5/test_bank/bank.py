def main():
    greeting = input("Greeting: ")

    response = value(greeting)

    print(f"${response}")


def value(greeting):
    text = greeting.lower().strip()

    if text.startswith("hello"):
        return 0
    elif text.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
