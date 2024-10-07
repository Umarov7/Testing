import os, colorama
os.system("clear")

# hexadecimal = input("Enter a number in hexadecimal: ")
# try:
#     binary = bin(int(hexadecimal, 16))[2:]
#     if binary:
#         print(binary)
# except:
#     print(colorama.Fore.RED + 'ERROR')
# else:
#     print(colorama.Fore.GREEN + "Success")
# finally:
#     print('Programme ended')
"""
import requests
url = 'https://nbu.uz/uz/exchange-rates/json/'
answer = requests.get(url)
json_file = answer.json()
# for x in json_file:
#     print('1', x['title'], "-", x["cb_price"], 'UZS')
print('Exchange rate:\n1. US DOLLARS\n2. EURO\n3. ROUBLE\n4. EXIT')
while 1:
    n = int(input("Choose: "))
    for x in json_file:
        if n == 1 and x['code'] == "USD":
            print('1', x['title'], '-', x['cb_price'], 'UZS')
        elif n == 2 and x['code'] == "EUR":
            print('2', x['title'], '-', x['cb_price'], 'UZS')
        elif n == 3 and x['code'] == "RUB":
            print('3', x['title'], '-', x['cb_price'], 'UZS')
    if n == 4:
        print("Thanks for using the programme!")
        break
"""
