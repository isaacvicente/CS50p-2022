from datetime import date
import sys
import inflect
import re


def main():
    birth_date = input("Date of Birth: ")
    if valid_date_format(birth_date) and date_existed(birth_date):
        print(age_as_minutes(birth_date))
    else:
        sys.exit(1)


def valid_date_format(date):
    """Validates a date in the format YYYY-MM-DD"""
    match = re.match(r"^\d{4}-\d{2}-\d{2}$", date)
    if match:
        return True
    else:
        return False


def date_existed(iso_date):
    """Takes a date (in ISO format) and determines if it existed"""
    return date.fromisoformat(iso_date) < date.today()


def age_as_minutes(birth_date):
    """Returns someone's age as minutes"""
    birth = date.fromisoformat(birth_date)
    today = date.today()

    timedelta = today - birth
    minutes = timedelta.days * 24 * 60

    p = inflect.engine()
    number_of_minutes = p.number_to_words(minutes, andword="").capitalize()

    return f"{number_of_minutes} minutes"


if __name__ == "__main__":
    main()
