meter_to_other_units = {"pm": 1000000000000, "nm": 1000000000, "μm": 1000000, "mm": 1000, "cm": 100, "dm": 10, "m": 1,
                        "Km": 0.001, "mi": 0.000621371192, "nmi": 0.000539956803, "ft": 3.2808399, "in": 39.3700787,
                        "yd": 1.0936133, "fur": 0.00497096954, "ftm": 0.546806649, "chi": 3, "gongli": 0.001,
                        "ly": 0.000000000000000105700083}


def length_converter(first_symbol, second_symbol, number):
    number = float(number)
    answer = ""

    if first_symbol != "m" and second_symbol == "m":
        answer = number / meter_to_other_units.get(first_symbol)

    if first_symbol == "m" and second_symbol != "m":
        answer = number * meter_to_other_units.get(second_symbol)

    if first_symbol != "g" and second_symbol != "g":
        answer = meter_to_other_units.get(second_symbol) * number / meter_to_other_units.get(first_symbol)

    try:
        if float(answer).is_integer():
            answer = int(answer)
    except:
        pass

    answer = "{:,}".format(answer)

    if first_symbol == second_symbol:
        answer = number

    return answer
