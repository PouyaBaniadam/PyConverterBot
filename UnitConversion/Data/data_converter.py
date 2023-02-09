byte_to_other_units = {"b": 8, "KB": 0.0009765625, "MB": 0.000000953674316, "GB": 0.00000000093132257421875,
                       "TB": 0.000000000000909494702, "PB": 0.000000000000000888178419921875,
                       "EB": 0.00000000000000000086736173820495}


def data_converter(first_symbol, second_symbol, number):
    number = float(number)
    answer = ""

    if first_symbol != "B" and second_symbol == "B":
        answer = number / byte_to_other_units.get(first_symbol)

    if first_symbol == "B" and second_symbol != "B":
        answer = number * byte_to_other_units.get(second_symbol)

    if first_symbol != "B" and second_symbol != "B":
        answer = byte_to_other_units.get(second_symbol) * number / byte_to_other_units.get(first_symbol)

    try:
        if float(answer).is_integer():
            answer = int(answer)
    except:
        pass

    answer = "{:,}".format(answer)

    if first_symbol == second_symbol:
        answer = number

    return answer
