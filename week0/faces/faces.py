def main():
    no_faces = input()

    with_faces = convert(no_faces)
    print(with_faces)


def convert(txt):
    converted_text = txt

    if ":)" in txt:
        converted_text = converted_text.replace(":)", "🙂")
    if ":(" in txt:
        converted_text = converted_text.replace(":(", "🙁")

    return converted_text


main()
