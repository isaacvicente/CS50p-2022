import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"^(([1-9]|1[0-2])(:(0[0-9]|[1-5][0-9]))?) (PM|AM) to (([1-9]|1[0-2])(:(0[0-9]|[1-5][0-9]))?) (PM|AM)$",
        s,
    )
    if match:
        # Let's say we have: 9:00 AM to 5:00 PM
        first_clock_setting = match.group(5)
        # 9:00 AM to 5:00 PM
        #      ^^
        first_hour_field = match.group(2)
        # 9:00 AM to 5:00 PM
        # ^
        second_clock_setting = match.group(10)
        # 9:00 AM to 5:00 PM
        #                 ^^
        second_hour_field = match.group(7)
        # 9:00 AM to 5:00 PM
        #            ^
        first_full_hour_format = match.group(1)
        # 9:00 AM to 5:00 PM
        # ^^^^
        second_full_hour_format = match.group(6)
        # 9:00 AM to 5:00 PM
        #            ^^^^

        if first_clock_setting == "AM":
            if first_hour_field == "12":
                hour = "00"
            else:
                hour = f"{int(first_hour_field):02}"
        else:  # If it's PM
            if first_hour_field == "12":
                hour = first_hour_field
            else:
                hour = int(first_hour_field) + 12
                hour = f"{hour:02}"

        if ":" in first_full_hour_format:
            minutes = match.group(4)
            first_hour = f"{hour}:{minutes}"
        else:
            first_hour = f"{hour}:00"

        # --------------------------------

        if second_clock_setting == "AM":
            if second_hour_field == "12":
                hour = "00"
            else:
                hour = f"{int(second_hour_field):02}"
        else:  # If it's PM
            if second_hour_field == "12":
                hour = second_hour_field
            else:
                hour = int(second_hour_field) + 12
                hour = f"{hour:02}"

        if ":" in second_full_hour_format:
            minutes = match.group(9)
            second_hour = f"{hour}:{minutes}"
        else:
            second_hour = f"{hour}:00"

        # Return the 24-hour equivalent format
        return f"{first_hour} to {second_hour}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
