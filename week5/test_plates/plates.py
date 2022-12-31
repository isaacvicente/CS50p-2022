def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # If the plate has a length greater than 6 or less than 2 (the maximum and minimum, respectively), return False
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        # All vanity plates must start with at least 2 letters
        if not (s[0].isalpha() and s[1].isalpha()):
            return False
    # Iterates through the string by it's index
    for i in range(len(s)):
        # Each character of the plate must be a number or a letter
        if s[i].isalnum():
            # For the first occurrence of a number
            if s[i].isnumeric():
                # If the rest of the string is also made by numbers and the first one is not zero, return True
                if s[i:].isnumeric() and int(s[i]) != 0:
                    return True
                else:
                    return False
        # If neither a number nor letter, return False
        else:
            return False
    # If we passed all through the string and didn't catch any invalid case, return True
    return True


if __name__ == "__main__":
    main()
