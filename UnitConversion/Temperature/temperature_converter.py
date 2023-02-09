def temperature_converter(first_symbol, second_symbol, number):
    temperature_formulas = {"F°->C°": ((float(number) - 32) * 5) / 9, "C°->F°": ((float(number) * 1.8) + 32),
                            "K->C°": float(number) - 273.15, "C°->K": (float(number) + 273.15),
                            "K->F°": (1.8 * (float(number) - 273.15)) + 32,
                            "F°->K": ((float(number) - 32) / 1.8) + 273.15}

    data = f"{first_symbol}->{second_symbol}"

    if first_symbol != second_symbol:
        answer = temperature_formulas[data]

    else:
        answer = str(number)

    try:
        if float(answer).is_integer():
            answer = int(answer)
    except:
        pass

    answer = "{:,}".format(answer)

    if first_symbol == second_symbol:
        answer = number

    return answer
