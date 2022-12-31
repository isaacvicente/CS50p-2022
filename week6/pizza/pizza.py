from tabulate import tabulate
import sys
import csv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# Our table list, being each element a row in the table formatted
table = []

try:
    with open(sys.argv[1]) as file:
        # Read the first line if the CSV file, which is the header of the table
        headers = file.readline().rstrip().split(",")
        # After reading the headers, the next rows are the body of the table
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

# Print the tabulated table with its headers at the top
print(tabulate(table, headers, tablefmt="grid"))
