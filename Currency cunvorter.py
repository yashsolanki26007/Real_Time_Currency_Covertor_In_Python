from forex_python.converter import CurrencyRates

c = CurrencyRates()

print("Real Time Currency Converter")

from_currency = input("From Currency (USD, INR, EUR etc): ").upper()
amount = float(input("Enter amount: "))
to_currency = input("To Currency (USD, INR, EUR etc): ").upper()

try:
    result = c.convert(from_currency, to_currency, amount)
    print(f"\n{amount} {from_currency} = {result:.2f} {to_currency}")
except:
    print("Invalid currency code. Try again.")