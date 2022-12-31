amount_due = 50

while amount_due > 0:
    coins = int(input("Insert Coin: "))
    if coins == 5 or coins == 10 or coins == 25:
        amount_due -= coins
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
        else:
            print(f"Amount Due: {amount_due}")
    else:
        print(f"Amount Due: {amount_due}")
