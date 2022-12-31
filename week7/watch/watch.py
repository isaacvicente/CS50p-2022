import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r"""src="https?://(www\.)?youtube.com/embed/(\w{11})""", s)
    if match:
        return f"https://youtu.be/{match.group(2)}"


if __name__ == "__main__":
    main()
