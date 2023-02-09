gram_to_other_units = {"ng": 1000000000, "μg": 1000000, "q": 100000, "mg": 1000, "cg": 100, "dg": 10, "g": 1,
                       "Kg": 0.001, "t": 0.000001, "lb": 0.00220462262, "oz": 0.0352739619, "ct": 5, "gr": 15.4323584,
                       "l.t": 0.000000984206528, "sh.t": 0.00000110231131, "st": 0.000157473044, "dr": 0.564383391,
                       "dan": 0.00002, "sir": 0.0133547009}


def mass_converter(first_symbol, second_symbol, number):
    number = float(number)
    answer = ""

    if first_symbol != "g" and second_symbol == "g":
        answer = number / gram_to_other_units.get(first_symbol)

    if first_symbol == "g" and second_symbol != "g":
        answer = number * gram_to_other_units.get(second_symbol)

    if first_symbol != "g" and second_symbol != "g":
        answer = gram_to_other_units.get(second_symbol) * number / gram_to_other_units.get(first_symbol)

    try:
        if float(answer).is_integer():
            answer = int(answer)
    except:
        pass

    answer = "{:,}".format(answer)

    if first_symbol == second_symbol:
        answer = number

    return answer
