import requests
from bs4 import BeautifulSoup
import re

from Settings.languages.languages_dictionary import languages

currency_symbols = {"USD": "$", "IRR": "T", "EUR": "€", "GBP": "£", "CHF": "₣", "LIR": "₺", "AED": "DH"}

def currency_converter(amount, source_currency, target_currency):
    url = "https://www.tgju.org"

    currency_symbols = {"USD": "$", "IRR": "T", "EUR": "€", "GBP": "£", "CHF": "₣", "LIR": "₺", "AED": "DH"}

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    market_price_tags = soup.find_all("td", class_="market-price")

    USD = float(market_price_tags[0].text.replace(",", ""))
    EUR = float(market_price_tags[1].text.replace(",", ""))
    AED = float(market_price_tags[2].text.replace(",", ""))
    GBP = float(market_price_tags[3].text.replace(",", ""))
    LIR = float(market_price_tags[4].text.replace(",", ""))
    CHF = float(market_price_tags[5].text.replace(",", ""))
    IRR = 10.0

    if source_currency == "USD":
        source_currency_amount = float(USD)

    elif source_currency == "EUR":
        source_currency_amount = float(EUR)

    elif source_currency == "AED":
        source_currency_amount = float(AED)

    elif source_currency == "GBP":
        source_currency_amount = float(GBP)

    elif source_currency == "LIR":
        source_currency_amount = float(LIR)

    elif source_currency == "CHF":
        source_currency_amount = float(CHF)

    elif source_currency == "AED":
        source_currency_amount = float(AED)

    elif source_currency == "IRR":
        source_currency_amount = float(IRR)

    if target_currency == "USD":
        target_currency_amount = float(USD)

    elif target_currency == "EUR":
        target_currency_amount = float(EUR)

    elif target_currency == "AED":
        target_currency_amount = float(AED)

    elif target_currency == "GBP":
        target_currency_amount = float(GBP)

    elif target_currency == "LIR":
        target_currency_amount = float(LIR)

    elif target_currency == "CHF":
        target_currency_amount = float(CHF)

    elif target_currency == "AED":
        target_currency_amount = float(AED)

    elif target_currency == "IRR":
        target_currency_amount = float(IRR)

    answer = round((source_currency_amount * float(amount)) / target_currency_amount, 5)

    if answer % 1 == 0:
        answer = int(answer)

    return f"{amount} {currency_symbols[source_currency]} = <code> {answer} {currency_symbols[target_currency]} </code>"


def momentarily_currency_rate(user_language):
    rates_list = []

    currency_symbols = {"USD": "$", "IRR": "T", "EUR": "€", "GBP": "£", "CHF": "₣", "LIR": "₺",
                        "AED": languages[user_language]['derham_symbol']}

    # USD Rate
    url = "https://fa.navasan.net/dayRates.php?item=usd"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is not None:
            for div in divs:
                rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
                break
        else:
            rates_list.append(languages[user_language]['cant_fetch_data'])

    else:
        for div in divs:
            rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
            break

    # EUR Rate
    url = "https://fa.navasan.net/dayRates.php?item=eur"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is not None:
            for div in divs:
                rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
                break
        else:
            rates_list.append(languages[user_language]['cant_fetch_data'])

    else:
        for div in divs:
            rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
            break

    # Pound Rate
    url = "https://fa.navasan.net/dayRates.php?item=gbp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is not None:
            for div in divs:
                rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
                break
        else:
            rates_list.append(languages[user_language]['cant_fetch_data'])

    else:
        for div in divs:
            rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
            break

    # AED Rate
    url = "https://fa.navasan.net/dayRates.php?item=aed"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is not None:
            for div in divs:
                rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
                break
        else:
            rates_list.append(languages[user_language]['cant_fetch_data'])

    else:
        for div in divs:
            rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
            break

    # LIR Rate
    url = "https://fa.navasan.net/dayRates.php?item=try"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find('div', {'class': 'idesc lastrate pos'})

    if divs is None:
        divs = soup.find('div', {'class': 'idesc lastrate neg'})

        if divs is not None:
            for div in divs:
                rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
                break
        else:
            rates_list.append(languages[user_language]['cant_fetch_data'])

    else:
        for div in divs:
            rates_list.append(re.sub(r'\s+', ' ', div.text).strip())
            break

    try:
        USD = float(rates_list[0].replace(",", ""))
        if USD % 1 == 0:
            USD = int(USD)
    except:
        USD = rates_list[0]

    try:
        EUR = float(rates_list[1].replace(",", ""))
        if EUR % 1 == 0:
            EUR = int(EUR)
    except:
        EUR = rates_list[1]

    try:
        GBP = float(rates_list[2].replace(",", ""))
        if GBP % 1 == 0:
            GBP = int(GBP)
    except:
        GBP = rates_list[2]

    try:
        AED = float(rates_list[3].replace(",", ""))
        if AED % 1 == 0:
            AED = int(AED)
    except:
        AED = rates_list[3]

    try:
        LIR = float(rates_list[4].replace(",", ""))
        if LIR % 1 == 0:
            LIR = int(LIR)
    except:
        LIR = rates_list[4]

    return f"""{currency_symbols['USD']} {languages[user_language]['dollar_currency_converter']} {currency_symbols['USD']} : {currency_symbols['IRR']} <code> {USD} {languages[user_language]['tooman_currency_converter']} </code> {currency_symbols['IRR']}
    
{currency_symbols['EUR']} {languages[user_language]['euro_currency_converter']} {currency_symbols['EUR']} : {currency_symbols['IRR']} <code> {EUR} {languages[user_language]['tooman_currency_converter']} </code> {currency_symbols['IRR']}

{currency_symbols['GBP']} {languages[user_language]['pound_currency_converter']} {currency_symbols['GBP']} : {currency_symbols['IRR']} <code> {GBP} {languages[user_language]['tooman_currency_converter']} </code> {currency_symbols['IRR']}

{currency_symbols['LIR']} {languages[user_language]['lir_currency_converter']} {currency_symbols['LIR']} : {currency_symbols['IRR']} <code> {LIR} {languages[user_language]['tooman_currency_converter']} </code> {currency_symbols['IRR']}

{currency_symbols['AED']} {languages[user_language]['dirham_currency_converter']} {currency_symbols['AED']} : {currency_symbols['IRR']} <code> {AED} {languages[user_language]['tooman_currency_converter']} </code> {currency_symbols['IRR']}
"""
