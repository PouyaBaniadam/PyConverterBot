time_to_other_units = {"ps": 1000000000000, "ns": 1000000000, "μs": 1000000, "ms": 1000, "s": 1,
                       "min": 0.01666666667, "h": 0.00027777778, "d": 0.0000115740741, "mo": 0.00000038052,
                       "y": 0.000000031709792, "dec": 0.0000000031709792, "cent": 0.00000000031709792}


def time_converter(first_symbol, second_symbol, number):
    number = float(number)
    answer = ""

    if first_symbol == "s" and second_symbol != "s":
        answer = number * time_to_other_units.get(second_symbol)

    if first_symbol != "s" and second_symbol == "s":
        answer = number / time_to_other_units.get(first_symbol)

    if first_symbol != "s" and second_symbol != "s":
        answer = (number / time_to_other_units.get(first_symbol) * time_to_other_units.get(second_symbol))

    try:
        if float(answer).is_integer():
            answer = int(answer)
    except:
        pass

    answer = "{:,}".format(answer)

    if first_symbol == second_symbol:
        answer = number

    return answer
