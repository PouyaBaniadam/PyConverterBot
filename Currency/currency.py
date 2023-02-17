import requests
from bs4 import BeautifulSoup

from Settings.languages.languages_dictionary import languages

currency_symbols = {"USD": "$", "IRR": "T", "EUR": "€", "GBP": "£", "CHF": "₣", "LIR": "₺", "AED": "dh"}


def currency_converter(amount, source_currency, target_currency):
    url = "https://www.tgju.org"

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
    url = "https://www.tgju.org"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    market_price_tags = soup.find_all("td", class_="market-price")

    USD = float(market_price_tags[0].text.replace(",", ""))
    EUR = float(market_price_tags[1].text.replace(",", ""))
    AED = float(market_price_tags[2].text.replace(",", ""))
    GBP = float(market_price_tags[3].text.replace(",", ""))
    LIR = float(market_price_tags[4].text.replace(",", ""))
    CHF = float(market_price_tags[5].text.replace(",", ""))

    USD /= 10
    EUR /= 10
    AED /= 10
    GBP /= 10
    LIR /= 10
    CHF /= 10

    if USD % 1 == 0:
        USD = int(USD)

    if EUR % 1 == 0:
        EUR = int(EUR)

    if AED % 1 == 0:
        AED = int(AED)

    if GBP % 1 == 0:
        GBP = int(GBP)

    if LIR % 1 == 0:
        LIR = int(LIR)

    if CHF % 1 == 0:
        CHF = int(CHF)

    return f"""{languages[user_language]['dollar_currency_converter']} : <code> {USD} {languages[user_language]['tooman_currency_converter']} </code>
    
{languages[user_language]['euro_currency_converter']} : <code> {EUR} {languages[user_language]['tooman_currency_converter']} </code>

{languages[user_language]['pound_currency_converter']} : <code> {GBP} {languages[user_language]['tooman_currency_converter']} </code>

{languages[user_language]['lir_currency_converter']} : <code> {LIR} {languages[user_language]['tooman_currency_converter']} </code>

{languages[user_language]['swiss_franc_currency_converter']} : <code> {CHF} {languages[user_language]['tooman_currency_converter']} </code>

{languages[user_language]['dirham_currency_converter']} : <code> {AED} {languages[user_language]['tooman_currency_converter']} </code>

"""
