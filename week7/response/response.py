import validators


def main():
    adress = input("What's your email adress? ")
    print(validate_email(adress))


def validate_email(adress):
    if validators.email(adress):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
