import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
currencies = data[0]["rates"]
for item in currencies:
    print(item)

with open('currency.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';')
    filewriter.writerow(['currency', 'code', 'bid', 'ask'])
    for item in currencies:
        currency = item["currency"]
        code = item["code"]
        bid = item["bid"]
        ask = item["ask"]
        filewriter.writerow([currency, code, bid, ask])



