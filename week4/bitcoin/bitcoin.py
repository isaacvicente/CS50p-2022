import requests
import sys


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.JSONDecodeError:
    sys.exit(1)

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


bitcoin_price = response["bpi"]["USD"]["rate_float"]
amount = bitcoin_price * n_bitcoins

print(f"${amount:,.4f}")
