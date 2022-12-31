def main():
    time = input("What time is it? ").lower().strip()
    n_hours = convert(time)

    if 7 <= n_hours <= 8:
        print("breakfast time")
    elif 12 <= n_hours <= 13:
        print("lunch time")
    elif 18 <= n_hours <= 19:
        print("dinner time")


def convert(time):
    if time.endswith("a.m."):
        # Separate the "10:40" and "a.m." and get only the "10:40", for instance
        real_time = time.split(" ")[0]
        hours, minutes = real_time.split(":")
        hour_fraction = float(minutes) / 60
        return float(hours) + hour_fraction
    elif time.endswith("p.m."):
        # Separate the "10:40" and "p.m." and get only the "10:40", for instance
        real_time = time.split(" ")[0]
        hours, minutes = real_time.split(":")
        hour_fraction = float(minutes) / 60
        return 12 + float(hours) + hour_fraction
    else:
        hours, minutes = time.split(":")
        hour_fraction = float(minutes) / 60
        return float(hours) + hour_fraction


if __name__ == "__main__":
    main()
