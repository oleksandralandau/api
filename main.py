import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open('currency.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';')
    filewriter.writerow(['currency', 'code', 'bid', 'ask'])
    filewriter.writerow(['dolar amerykański', 'USD', '4.2480', '4.3338'])
    filewriter.writerow(['dolar australijski', 'AUD', '2.8496', '2.9072'])
    filewriter.writerow(['dolar kanadyjski', 'CAD', '3.1399', '3.2033'])
    filewriter.writerow(['euro', 'EUR', '4.6274', '4.7208'])
    filewriter.writerow(['forint (Węgry)', 'HUF', '0.01217', '0.012416'])
    filewriter.writerow(['frank szwajcarski', 'CHF', '4.6532', '4.7472}'])
    filewriter.writerow(['funt szterling', 'GBP', '5.2634', '5.3698'])
    filewriter.writerow(['jen (Japonia)', 'JPY', '0.031939', '0.032585'])
    filewriter.writerow(['korona czeska', 'CZK', '0.1971', '0.2011'])
    filewriter.writerow(['korona duńska', 'DKK', '0.6212', '0.6338'])
    filewriter.writerow(['korona norweska"', 'NOK', '0.4063', '0.4145'])
    filewriter.writerow(['korona szwedzka', 'SEK', '0.4106', '0.4188'])
    filewriter.writerow(['DR (MFW)', 'XDR', '5.7202', '5.8358'])
