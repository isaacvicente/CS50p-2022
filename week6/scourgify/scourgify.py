import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

table = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        for row in reader:
            last, first = row["name"].split(",")

            table.append(
                # Append a dictionary as a list element and remove any whitespace in the name
                # (first and last)
                {"first": first.strip(), "last": last.strip(), "house": row["house"]}
            )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as new_file:
    writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
    # Writer the file header as specified by the field names
    writer.writeheader()

    for row in table:
        writer.writerow(
            {"first": row["first"], "last": row["last"], "house": row["house"]}
        )
