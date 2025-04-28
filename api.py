import requests
import os

BASE_URL = "https://api.exchangeratesapi.io/"

API_KEY = os.getenv("EXCHANGE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Set the EXCHANGE_API_KEY environment variable.")

# method to ask user what currency they want to convert to and from
def convert_currency():
    start = input("What currency would you like to convert from?: ----> (currency code, e.g. USD) ").strip().upper()
    end = input("What currency would you like to convert it to?: ----> (currency code, e.g. EUR) ").strip().upper()
    amount = float(input(f"Amount in {start}: "))

    url = f"{BASE_URL}/latest?access_key={API_KEY}&base={start}"
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()["rates"]
    converted_amount = amount * rates[end]
    print(f"\n{amount} {start} is equal to {converted_amount} {end}\n")

# method to ask user for a currency rate in a specified date in history
def historical_rate():
    date = input("Enter the date you’d like rates for (YYYY‑MM‑DD): ")
    base = input("Select a base currency: ----> (currency code, e.g. GBP) ").strip().upper()
    target = input("Select a target currency: ----> (currency code, e.g. CAD) ").strip().upper()

    url = f"{BASE_URL}/{date}?access_key={API_KEY}&base={base}&symbols={target}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()["rates"]
    rate = data.get(target)
    print(f"\nOn {date}, 1 {base} = {rate} {target}\n")


def main():
    greeting = ('Welcome to the Currency Converter!   ｡◕‿◕｡\n'
                'Enter 1 to Convert a Currency\n'
                'Enter 2 to Lookup a Historical Rate\n'
                'Enter 3 to Quit')
    print(greeting)
    while True:
        choice = input("What would you like to choose? ")
        if choice == "1":
            convert_currency()
        elif choice == "2":
            historical_rate()
        elif choice == "3":
            print("Thanks for using the Currency Converter! --- Goodbye ʕ•ᴥ•ʔ")
            break
        else:
            print("Hmm.. That doesnt seem to match one of the choices. Try again")


main()
