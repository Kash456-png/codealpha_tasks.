stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total_value = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock] * quantity
        total_value += value
    else:
        print("Stock not found!")

print("Total Investment Value: $", total_value)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_value}")

print("Result saved in portfolio.txt")