months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ")
    # For the format month/day/year, with "/"
    if "/" in date:
        try:
            # Split them
            month, day, year = date.split("/")
            # Convert each one to integers (they must be one)
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            # Check if the month and day numbers are invalid
            if month > 12 or day > 31:
                pass
            # If not, break the loop
            else:
                break
    # If the format is not with slashes, try the other one, e.g., September 9, 2019
    else:
        try:
            # Split month and day together (e.g. "September 9") and the year
            month_day, year = date.split(",")
            month, day = month_day.split()
            # The day and the year must be integers
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            # If "January", for instance, we've got 0 (it's index) plus 1, which is 1 (the first month)
            month = months.index(month) + 1
            # Check if the month and the day numbers are invalid
            if month > 12 or day > 31:
                pass
            # If not, break the loop
            else:
                break
# Print year-month-day formated as ####-##-##
print(f"{year:04}-{month:02}-{day:02}")
