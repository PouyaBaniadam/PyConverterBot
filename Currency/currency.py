import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
from Settings.languages.languages_dictionary import languages

currency_flags = {"USD": "🇺🇸", "EUR": "🇪🇺", "GBP": "🇬🇧", "LIR": "🇹🇷", "CHF": "🇸🇪", "JPY": "🇯🇵", "AED": "🇦🇪",
                  "IRR": "🇮🇷"}
key_value_list = list(currency_flags.items())
key = key_value_list[0][1]


async def current_currency_rate(session, currency: str):
    url = f"https://fa.navasan.net/dayRates.php?item={currency.lower()}"
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        divs = soup.find('div', {'class': 'idesc lastrate pos'})

        if divs is None:
            divs = soup.find('div', {'class': 'idesc lastrate neg'})

            if divs is None:
                divs = soup.find('div', {'class': 'idesc lastrate'})

            if divs is not None:
                for div in divs:
                    return re.sub(r'\s+', ' ', div.text).strip()
            else:
                return "?"

        else:
            for div in divs:
                return re.sub(r'\s+', ' ', div.text).strip()


async def momentarily_currency_rate(user_language):
    currencies_list = ["USD", "EUR", "GBP", "TRY", "CHF", "JPY", "AED"]
    currencies_list_after_process = currencies_list.copy()

    currency_names = [languages[user_language]['dollar_currency'], languages[user_language]['euro_currency'],
                      languages[user_language]['pound_currency'], languages[user_language]['lir_currency'],
                      languages[user_language]['swiss_franc_currency'], languages[user_language]['japan_yen'],
                      languages[user_language]['dirham_currency']]

    currencies_dictionary = {}
    tasks = []

    async with aiohttp.ClientSession() as session:
        for currency in currencies_list:
            tasks.append(asyncio.ensure_future(current_currency_rate(session, currency)))

        rates_list = await asyncio.gather(*tasks)

    currency_index = 0
    for rate in rates_list:
        try:
            currencies_list[currency_index] = float(rate.replace(",", ""))
            if currencies_list[currency_index] % 1 == 0:
                currencies_list[currency_index] = int(currencies_list[currency_index])
        except:
            currencies_list[currency_index] = rate

        currencies_dictionary.update(
            {currencies_list_after_process[currency_index]: {
                currencies_list[currency_index]: key_value_list[currency_index][1]}})

        currency_index += 1

    output = ""

    index = 0
    for currency_short_name, currency_rate_and_symbol in currencies_dictionary.items():
        output += f"""
{currency_rate_and_symbol[currencies_list[index]]} {currency_names[index]} {currency_rate_and_symbol[currencies_list[index]]} :\t {"🇮🇷"} <code> {'{:,}'.format(currencies_list[index])} {languages[user_language]['tooman_currency']} </code> {"🇮🇷"}

        """
        index += 1

    question_mark_count = 0
    for question_mark in currencies_list:
        if question_mark == "?":
            question_mark_count += 1

    has_so_many_question_marks = False

    if question_mark_count >= 3:
        has_so_many_question_marks = True
        return output, has_so_many_question_marks

    return output, has_so_many_question_marks
