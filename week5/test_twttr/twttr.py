def main():
    user_input = input("Input: ")

    shorten_word = shorten(user_input)

    print(f"Output: {shorten_word}")

def shorten(word):
    output = ""

    for character in word:
        c = character.lower()
        if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
            output += character

    return output


if __name__ == "__main__":
    main()