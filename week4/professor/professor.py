import random


def main():
    n_attempts = 0
    wrong_answers = 0
    score = 0

    level = get_level()

    while n_attempts < 10:
        if wrong_answers == 0:
            x = generate_integer(level)
            y = generate_integer(level)

            right_answer = x + y

        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            wrong_answers += 1
        else:
            if answer == right_answer:
                n_attempts += 1
                if wrong_answers == 0:
                    score += 1

                wrong_answers = 0
            elif wrong_answers < 3:
                print("EEE")
                wrong_answers += 1

        if wrong_answers == 3:
            print(f"{x} + {y} = {right_answer}")
            wrong_answers = 0
            n_attempts += 1

    print(f"Score: {score}")


def get_level():
    level = None
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level < 1 or level > 3:
                pass
            else:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
