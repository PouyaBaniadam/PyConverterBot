from decimal import Decimal
from math import sin, cos, tan, log10, sqrt, factorial

from Settings.languages.languages_dictionary import languages
from Settings.languages.users_languages import get_user_current_language


def calculator(phrase, user_id):
    global calculation_answer
    data = phrase

    try:
        data = data.replace(" ", "")
    except:
        pass

    try:
        data = data.replace("×", "*")
    except:
        pass

    try:
        data = data.replace("÷", "/")
    except:
        pass

    def calculation(data):
        global final_answer, temp_answer, calculation_answer

        all_operators = ("^", "*", "/", "+", "-")
        all_parenthesis = ("(", ")")
        all_trigonometry_and_log = ("sin", "cos", "tan", "cot", "log", "-sin", "-cos", "-tan", "-cot", "-log")
        all_first_alphabet_of_sin_cos_tan_cot_log = ("s", "c", "t", "l")

        temp = []
        for o in data:
            temp.append(o)

        if temp[-1] == "n" or temp[-1] == "s" or temp[-1] == "s" or temp[-1] == "g":
            temp.append("(")
            temp.append("0")

        temp.append("+")
        temp.append("0")

        temp_index_0 = -1
        for remaker_0 in temp:
            temp_index_0 += 1

            if remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

        temp.append("+")
        temp_index_1 = -1
        for remaker_1 in temp:
            temp_index_1 += 1

            if remaker_1.isdigit():

                if temp[temp_index_1 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_1 + 1, "(")

        temp.pop(-1)

        temp_index_2 = -1
        for remaker_2 in temp:
            temp_index_2 += 1

            if remaker_2 == "n" or remaker_2 == "s" or remaker_2 == "t" or remaker_2 == "g":

                if temp[temp_index_2 + 1] == "-" or temp[temp_index_2 + 1].isdigit():
                    temp.insert(temp_index_2 + 1, "(")

        temp_index_4 = -1
        for remaker_4 in temp:
            temp_index_4 += 1

            if remaker_4 == "(":
                if temp[temp_index_4 - 1] in all_parenthesis:
                    temp.insert(temp_index_4, "*")

        temp_index_5 = -1
        for remaker_5 in temp:
            temp_index_5 += 1

            if remaker_5 == "(":
                if temp[temp_index_5 - 1].isdigit():
                    temp.insert(temp_index_5, "*")

        temp_index_6 = -1
        for remaker_6 in temp:
            temp_index_6 += 1

            if remaker_6 == "(":
                if temp[temp_index_6 - 1] == "*" and temp[temp_index_6 - 2] == "(":
                    temp.insert(temp_index_6 - 1, "1")

        temp_index_7 = -1
        for remaker_7 in temp:
            temp_index_7 += 1

            if remaker_7 == ")":
                if temp[temp_index_7 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_7 + 1, "*")

        temp_index_8 = -1
        for remaker_8 in temp:
            temp_index_8 += 1

            if remaker_8 == "√":
                if temp[temp_index_8 - 1].isdigit():
                    temp.insert(temp_index_8, "*")

        temp_index_10 = -1
        for remaker_10 in temp:
            temp_index_10 += 1

            if remaker_10 == "!":
                if temp[temp_index_10 + 1] not in all_operators:
                    temp.insert(temp_index_10 + 1, "*")

        temp_index_11 = -1
        for remaker_11 in temp:
            temp_index_11 += 1

            if remaker_11 == "!":
                if temp[temp_index_11 + 1] == "*" and temp[temp_index_11 + 2] == ")":
                    temp.pop(temp_index_11 + 1)

        if temp[0] == "*":
            temp.insert(0, "1")

        data = "".join(map(str, temp))
        del temp

        if data[0] == "-":
            negative_to_be_added_later = "-"
            data = data[1:]

        else:
            negative_to_be_added_later = ""

        if data[0] == "+":
            posetive_to_be_added_later = "-+"
            data = data[1:]

        else:
            posetive_to_be_added_later = ""

        data = data + "+"
        data_list = []
        all_operators = ("^", "*", "/", "+", "-")

        temp_num_holder = ""
        temp_counter = -1

        for data_list_adder in data:
            temp_counter += 1

            if data_list_adder.isdigit() or data_list_adder == ".":
                temp_num_holder = temp_num_holder + data_list_adder

            elif data_list_adder == "s":
                if data[temp_counter - 1] != "o":
                    data_list.append("sin")

            elif data_list_adder == "c":
                if data[temp_counter + 2] == "s":
                    data_list.append("cos")

                if data[temp_counter + 2] == "t":
                    data_list.append("cot")

            elif data_list_adder == "t":
                if data[temp_counter - 1] != "o":
                    data_list.append("tan")

            elif data_list_adder == "l":
                data_list.append("log")

            elif data_list_adder == "-":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""

            elif data_list_adder == "+":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""


            elif data_list_adder in all_operators:
                data_list.append(temp_num_holder)
                data_list.append(data_list_adder)
                temp_num_holder = ""


            elif data_list_adder == "(":
                if temp_counter == 0:
                    data_list.append("(")

                elif data[temp_counter - 1] == "-" and data[temp_counter - 2] in all_operators:
                    data_list.append("-")
                    data_list.append("(")
                    temp_num_holder = ""

                else:
                    data_list.append("(")


            elif data_list_adder == ")":
                if data[temp_counter - 1].isdigit():
                    if len(temp_num_holder) != 0:
                        data_list.append(temp_num_holder)
                        data_list.append(")")
                        temp_num_holder = ""

                    else:
                        data_list.append(")")

                elif data[temp_counter - 1] == ")":
                    data_list.append(")")

                elif data[temp_counter - 1] == "!":
                    data_list.append(")")


            elif data_list_adder == "√":
                data_list.append("√")


            elif data_list_adder == "!":
                if len(temp_num_holder) != 0:
                    data_list.append(temp_num_holder)
                    data_list.append("!")
                    temp_num_holder = ""

                else:
                    data_list.append("!")

        if len(negative_to_be_added_later) == 1:
            if "(" in data_list[0]:
                data_list.pop(0)
                data_list.insert(0, "-")
                data_list.insert(1, "(")

            else:
                data_list[0] = "-" + data_list[0]
                data_list = data_list[0: -1]

        else:
            data_list = data_list[0: -1]

        if data_list[-1] == "+":
            data_list.pop(-1)

        temp_data_list = []
        for _ in data_list:
            if _ == '':
                pass

            else:
                temp_data_list.append(_)

        data_list = temp_data_list.copy()
        del temp_data_list

        all_parenthesis = ("(", ")")
        temp_counter = -1
        for data_list_remaker in data_list:
            temp_counter += 1

            if data_list_remaker == "(":
                if data_list[temp_counter + 1] == "-":
                    data_list[temp_counter + 1: temp_counter + 3] = [f"-{data_list[temp_counter + 2]}"]

        temp_index = -1
        for plus_zero_adder in data_list:
            temp_index += 1

            if plus_zero_adder == ")":
                if data_list[temp_index + 1] == ")":
                    data_list.insert(temp_index + 1, "+")
                    data_list.insert(temp_index + 2, "0")

        temp_index = -1
        for open_parenthesis_adder_to_begininig in data_list:
            temp_index += 1

            if open_parenthesis_adder_to_begininig == ")":
                if "(" not in data_list[temp_index:: -1]:
                    data_list.insert(0, "(")

        if data_list[0] == "-":
            if data_list[1] == "(":
                data_list.pop(0)
                data_list.insert(0, "-1")
                data_list.insert(1, "*")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-sin":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "sin")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cos":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cos")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-tan":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "tan")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cot":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cot")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-log":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "log")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        open_count = 0
        close_count = 0
        for _ in data_list:
            if _ == "(":
                open_count += 1

            if _ == ")":
                close_count += 1

        if open_count > close_count:
            for i in range(open_count - close_count):
                data_list.append(")")

        if close_count > open_count:
            for j in range(close_count - open_count):
                data_list.insert(0, "(")

        counter = 0
        for i in data_list:
            if i == "(":
                counter += 1

        for u in range(counter):
            temp_index = -1
            end_point = 0
            for _ in data_list:
                temp_index += 1

                if _ == ")":
                    end_point = temp_index
                    break

            temp_index = 0
            start_point = 0
            for __ in data_list[end_point:: -1]:
                temp_index += 1

                if __ == "(":
                    start_point = end_point - temp_index + 1
                    break

            calculate_zone = data_list[start_point + 1: end_point]

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            parenthesis_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in calculate_zone:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "(":
                    parenthesis_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            counter = 0
            for i in data_list:
                if i == "(":
                    counter += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in calculate_zone:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(calculate_zone[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:
                            calculation_answer = "Invalid input!"

                        calculate_zone[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in calculate_zone:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        temp_answer = float(calculate_zone[sqrt_index + 1])
                        temp_answer = sqrt(temp_answer)

                        calculate_zone[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in calculate_zone:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = calculate_zone[power_index - 1]
                        second_number = calculate_zone[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            calculation_answer = "Invalid input!"

                            calculate_zone.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:
                            calculation_answer = "Over Flow!"

                        if "^" in calculate_zone[power_index + 1:] or "*" in calculate_zone[power_index + 1:] \
                                or "/" in calculate_zone[power_index + 1:] or "+" in calculate_zone[power_index + 1:] \
                                or "-" in calculate_zone[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in calculate_zone:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        division_zero_count = 0
                        try:
                            temp_answer = first_number / second_number

                        except ZeroDivisionError:
                            calculation_answer = "Can't divide to zero!"

                            division_zero_count += 1

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if division_zero_count == 0:
                                try:
                                    calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]

                                except ZeroDivisionError:
                                    calculation_answer = "Can't divide to zero!"


                            else:
                                calculate_zone = []

                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in calculate_zone:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

                    if plus_or_mines_finder == "-":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

            for remover in range(x_count):
                calculate_zone.pop(0)

            if data_list[start_point - 1] == "sin" or data_list[start_point - 1] == "-sin":
                try:
                    calculate_zone = sin(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            elif data_list[start_point - 1] == "cos" or data_list[start_point - 1] == "-cos":
                try:
                    calculate_zone = cos(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            elif data_list[start_point - 1] == "tan" or data_list[start_point - 1] == "-tan":
                try:
                    calculate_zone = tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            elif data_list[start_point - 1] == "cot" or data_list[start_point - 1] == "-cot":
                try:
                    calculate_zone = 1 / tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            elif data_list[start_point - 1] == "log" or data_list[start_point - 1] == "-log":
                try:
                    calculate_zone = log10(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            else:
                data_list[start_point: end_point + 1] = calculate_zone

        if "(" not in data_list:

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in data_list:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in data_list:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(data_list[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:

                            calculation_answer = "Invalid input!"

                        data_list[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in data_list:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        try:
                            temp_answer = float(data_list[sqrt_index + 1])
                            temp_answer = sqrt(temp_answer)

                        except:

                            calculation_answer = "Invalid input!"

                        data_list[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in data_list:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = data_list[power_index - 1]
                        second_number = data_list[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            calculation_answer = "Invalid input!"

                            data_list.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:

                            calculation_answer = "Over Flow!"

                        if "^" in data_list[power_index + 1:] or "*" in data_list[power_index + 1:] \
                                or "/" in data_list[power_index + 1:] or "+" in data_list[power_index + 1:] \
                                or "-" in data_list[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            data_list[starting_point: ending_point] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in data_list:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        division_zero_count = 0
                        try:
                            temp_answer = first_number / second_number

                        except ZeroDivisionError:
                            calculation_answer = "Can't divide to zero!"

                            division_zero_count += 1

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if division_zero_count == 0:
                                try:
                                    data_list[starting_point: ending_point + 1] = [str(temp_answer)]

                                except ZeroDivisionError:
                                    calculation_answer = "Can't divide to zero!"

                                    break

                            else:
                                data_list = []

                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in data_list:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point:] = [temp_answer]

                    if plus_or_mines_finder == "-":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point:] = [temp_answer]

            for remover in range(x_count):
                data_list.pop(0)

            final_answer = ""
            if data_list:
                final_answer = data_list[0]

            if final_answer == "+":
                calculation_answer = ""

            else:
                if final_answer == "-0":
                    final_answer = "0"
                    calculation_answer = final_answer


                else:
                    calculation_answer = final_answer

    def calculation_with_out_printings(data):
        global final_answer

        all_operators = ("^", "*", "/", "+", "-")
        all_parenthesis = ("(", ")")
        all_trigonometry_and_log = ("sin", "cos", "tan", "cot", "log", "-sin", "-cos", "-tan", "-cot", "-log")
        all_first_alphabet_of_sin_cos_tan_cot_log = ("s", "c", "t", "l")

        temp = []
        for o in data:
            temp.append(o)

        if temp[-1] == "n" or temp[-1] == "s" or temp[-1] == "s" or temp[-1] == "g":
            temp.append("(")
            temp.append("0")

        temp.append("+")
        temp.append("0")

        temp_index_0 = -1
        for remaker_0 in temp:
            temp_index_0 += 1

            if remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "t" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "g" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "n" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "t":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "c":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "l":
                temp.insert(temp_index_0 + 1, "(")

            elif remaker_0 == "s" and temp[temp_index_0 + 1] == "s":
                temp.insert(temp_index_0 + 1, "(")

        temp.append("+")
        temp_index_1 = -1
        for remaker_1 in temp:
            temp_index_1 += 1

            if remaker_1.isdigit():

                if temp[temp_index_1 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_1 + 1, "(")

        temp.pop(-1)

        temp_index_2 = -1
        for remaker_2 in temp:
            temp_index_2 += 1

            if remaker_2 == "n" or remaker_2 == "s" or remaker_2 == "t" or remaker_2 == "g":

                if temp[temp_index_2 + 1] == "-" or temp[temp_index_2 + 1].isdigit():
                    temp.insert(temp_index_2 + 1, "(")

        temp_index_4 = -1
        for remaker_4 in temp:
            temp_index_4 += 1

            if remaker_4 == "(":
                if temp[temp_index_4 - 1] in all_parenthesis:
                    temp.insert(temp_index_4, "*")

        temp_index_5 = -1
        for remaker_5 in temp:
            temp_index_5 += 1

            if remaker_5 == "(":
                if temp[temp_index_5 - 1].isdigit():
                    temp.insert(temp_index_5, "*")

        temp_index_6 = -1
        for remaker_6 in temp:
            temp_index_6 += 1

            if remaker_6 == "(":
                if temp[temp_index_6 - 1] == "*" and temp[temp_index_6 - 2] == "(":
                    temp.insert(temp_index_6 - 1, "1")

        temp_index_7 = -1
        for remaker_7 in temp:
            temp_index_7 += 1

            if remaker_7 == ")":
                if temp[temp_index_7 + 1] in all_first_alphabet_of_sin_cos_tan_cot_log:
                    temp.insert(temp_index_7 + 1, "*")

        temp_index_8 = -1
        for remaker_8 in temp:
            temp_index_8 += 1

            if remaker_8 == "√":
                if temp[temp_index_8 - 1].isdigit():
                    temp.insert(temp_index_8, "*")

        temp_index_10 = -1
        for remaker_10 in temp:
            temp_index_10 += 1

            if remaker_10 == "!":
                if temp[temp_index_10 + 1] not in all_operators:
                    temp.insert(temp_index_10 + 1, "*")

        temp_index_11 = -1
        for remaker_11 in temp:
            temp_index_11 += 1

            if remaker_11 == "!":
                if temp[temp_index_11 + 1] == "*" and temp[temp_index_11 + 2] == ")":
                    temp.pop(temp_index_11 + 1)

        if temp[0] == "*":
            temp.insert(0, "1")

        data = "".join(map(str, temp))
        del temp

        if data[0] == "-":
            negative_to_be_added_later = "-"
            data = data[1:]

        else:
            negative_to_be_added_later = ""

        if data[0] == "+":
            posetive_to_be_added_later = "-+"
            data = data[1:]

        else:
            posetive_to_be_added_later = ""

        data = data + "+"
        data_list = []
        all_operators = ("^", "*", "/", "+", "-")

        temp_num_holder = ""
        temp_counter = -1

        for data_list_adder in data:
            temp_counter += 1

            if data_list_adder.isdigit() or data_list_adder == ".":
                temp_num_holder = temp_num_holder + data_list_adder

            elif data_list_adder == "s":
                if data[temp_counter - 1] != "o":
                    data_list.append("sin")

            elif data_list_adder == "c":
                if data[temp_counter + 2] == "s":
                    data_list.append("cos")

                if data[temp_counter + 2] == "t":
                    data_list.append("cot")

            elif data_list_adder == "t":
                if data[temp_counter - 1] != "o":
                    data_list.append("tan")

            elif data_list_adder == "l":
                data_list.append("log")

            elif data_list_adder == "-":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""

            elif data_list_adder == "+":
                if data[temp_counter - 1] in all_operators:
                    temp_num_holder = data_list_adder + temp_num_holder
                else:
                    data_list.append(temp_num_holder)
                    data_list.append(data_list_adder)
                    temp_num_holder = ""


            elif data_list_adder in all_operators:
                data_list.append(temp_num_holder)
                data_list.append(data_list_adder)
                temp_num_holder = ""


            elif data_list_adder == "(":
                if temp_counter == 0:
                    data_list.append("(")

                elif data[temp_counter - 1] == "-" and data[temp_counter - 2] in all_operators:
                    data_list.append("-")
                    data_list.append("(")
                    temp_num_holder = ""

                else:
                    data_list.append("(")


            elif data_list_adder == ")":
                if data[temp_counter - 1].isdigit():
                    if len(temp_num_holder) != 0:
                        data_list.append(temp_num_holder)
                        data_list.append(")")
                        temp_num_holder = ""

                    else:
                        data_list.append(")")

                elif data[temp_counter - 1] == ")":
                    data_list.append(")")

                elif data[temp_counter - 1] == "!":
                    data_list.append(")")


            elif data_list_adder == "√":
                data_list.append("√")


            elif data_list_adder == "!":
                if len(temp_num_holder) != 0:
                    data_list.append(temp_num_holder)
                    data_list.append("!")
                    temp_num_holder = ""

                else:
                    data_list.append("!")

        if len(negative_to_be_added_later) == 1:
            if "(" in data_list[0]:
                data_list.pop(0)
                data_list.insert(0, "-")
                data_list.insert(1, "(")

            else:

                data_list[0] = "-" + data_list[0]
                data_list = data_list[0: -1]

        else:
            data_list = data_list[0: -1]

        if data_list[-1] == "+":
            data_list.pop(-1)

        temp_data_list = []
        for _ in data_list:
            if _ == '':
                pass

            else:
                temp_data_list.append(_)

        data_list = temp_data_list.copy()
        del temp_data_list

        all_parenthesis = ("(", ")")
        temp_counter = -1
        for data_list_remaker in data_list:
            temp_counter += 1

            if data_list_remaker == "(":
                if data_list[temp_counter + 1] == "-":
                    data_list[temp_counter + 1: temp_counter + 3] = [f"-{data_list[temp_counter + 2]}"]

        temp_index = -1
        for plus_zero_adder in data_list:
            temp_index += 1

            if plus_zero_adder == ")":
                if data_list[temp_index + 1] == ")":
                    data_list.insert(temp_index + 1, "+")
                    data_list.insert(temp_index + 2, "0")

        temp_index = -1
        for open_parenthesis_adder_to_begininig in data_list:
            temp_index += 1

            if open_parenthesis_adder_to_begininig == ")":
                if "(" not in data_list[temp_index:: -1]:
                    data_list.insert(0, "(")

        if data_list[0] == "-":
            if data_list[1] == "(":
                data_list.pop(0)
                data_list.insert(0, "-1")
                data_list.insert(1, "*")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-sin":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "sin")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cos":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cos")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-tan":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "tan")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-cot":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "cot")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        temp_index = -1
        for neg_remover in data_list:
            temp_index += 1

            if neg_remover == "-log":
                data_list.pop(temp_index)
                data_list.insert(temp_index, "log")
                data_list.insert(temp_index, "(")
                data_list.insert(temp_index, "*")
                data_list.insert(temp_index, "-1")

        open_count = 0
        close_count = 0
        for _ in data_list:
            if _ == "(":
                open_count += 1

            if _ == ")":
                close_count += 1

        if open_count > close_count:
            for i in range(open_count - close_count):
                data_list.append(")")

        if close_count > open_count:
            for j in range(close_count - open_count):
                data_list.insert(0, "(")

        counter = 0
        for i in data_list:
            if i == "(":
                counter += 1

        for u in range(counter):
            temp_index = -1
            end_point = 0
            for _ in data_list:
                temp_index += 1

                if _ == ")":
                    end_point = temp_index
                    break

            temp_index = 0
            start_point = 0
            for __ in data_list[end_point:: -1]:
                temp_index += 1

                if __ == "(":
                    start_point = end_point - temp_index + 1
                    break

            calculate_zone = data_list[start_point + 1: end_point]

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            parenthesis_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in calculate_zone:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "(":
                    parenthesis_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            counter = 0
            for i in data_list:
                if i == "(":
                    counter += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in calculate_zone:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(calculate_zone[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:

                            calculation_answer = "Invalid input!"

                        calculate_zone[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in calculate_zone:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        temp_answer = float(calculate_zone[sqrt_index + 1])
                        temp_answer = sqrt(temp_answer)

                        calculate_zone[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in calculate_zone:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = calculate_zone[power_index - 1]
                        second_number = calculate_zone[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            calculation_answer = "Invalid input!"

                            calculate_zone.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:

                            calculation_answer = "Over Flow!"

                        if "^" in calculate_zone[power_index + 1:] or "*" in calculate_zone[power_index + 1:] \
                                or "/" in calculate_zone[power_index + 1:] or "+" in calculate_zone[power_index + 1:] \
                                or "-" in calculate_zone[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in calculate_zone:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = calculate_zone[times_or_fraction_index - 1]
                        second_number = calculate_zone[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        division_zero_count = 0
                        try:
                            temp_answer = first_number / second_number

                        except ZeroDivisionError:
                            calculation_answer = "Can't divide to zero!"

                            division_zero_count += 1

                        if "^" in calculate_zone[times_or_fraction_index:] or "*" in calculate_zone[
                                                                                     times_or_fraction_index:] \
                                or "/" in calculate_zone[times_or_fraction_index:] or "+" in calculate_zone[
                                                                                             times_or_fraction_index:] \
                                or "-" in calculate_zone[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if division_zero_count == 0:
                                try:
                                    calculate_zone[starting_point: ending_point + 1] = [str(temp_answer)]

                                except ZeroDivisionError:
                                    calculation_answer = "Can't divide to zero!"

                            else:
                                calculate_zone = []

                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1
                            calculate_zone.insert(0, "x")
                            calculate_zone.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            calculate_zone[starting_point:] = [str(temp_answer)]
                            calculate_zone.append("+")
                            calculate_zone.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    calculate_zone.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in calculate_zone:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

                    if plus_or_mines_finder == "-":
                        first_number = calculate_zone[plus_or_mines_index - 1]
                        second_number = calculate_zone[plus_or_mines_index + 1]

                        if "^" in calculate_zone[plus_or_mines_index + 1:] or "*" in calculate_zone[
                                                                                     plus_or_mines_index + 1:] \
                                or "/" in calculate_zone[plus_or_mines_index + 1:] or "+" in calculate_zone[
                                                                                             plus_or_mines_index + 1:] \
                                or "-" in calculate_zone[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point: ending_point] = [str(temp_answer)]
                            calculate_zone.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            calculate_zone[starting_point:] = [str(temp_answer)]

            for remover in range(x_count):
                calculate_zone.pop(0)

            if data_list[start_point - 1] == "sin" or data_list[start_point - 1] == "-sin":
                try:
                    calculate_zone = sin(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"



            elif data_list[start_point - 1] == "cos" or data_list[start_point - 1] == "-cos":
                try:
                    calculate_zone = cos(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"



            elif data_list[start_point - 1] == "tan" or data_list[start_point - 1] == "-tan":
                try:
                    calculate_zone = tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"



            elif data_list[start_point - 1] == "cot" or data_list[start_point - 1] == "-cot":
                try:
                    calculate_zone = 1 / tan(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"



            elif data_list[start_point - 1] == "log" or data_list[start_point - 1] == "-log":
                try:
                    calculate_zone = log10(float(calculate_zone[0]))
                    calculate_zone = str(calculate_zone)
                    data_list[start_point - 1: end_point + 1] = [calculate_zone]
                except:

                    calculation_answer = "Invalid input!"


            else:
                data_list[start_point: end_point + 1] = calculate_zone

        if "(" not in data_list:

            power_count = 0
            times_count = 0
            fraction_count = 0
            plus_count = 0
            mines_count = 0
            sqrt_count = 0
            fact_count = 0

            for how_many_of_each_operators in data_list:
                if how_many_of_each_operators == "^":
                    power_count += 1

                if how_many_of_each_operators == "*":
                    times_count += 1

                if how_many_of_each_operators == "/":
                    fraction_count += 1

                if how_many_of_each_operators == "+":
                    plus_count += 1

                if how_many_of_each_operators == "-":
                    mines_count += 1

                if how_many_of_each_operators == "√":
                    sqrt_count += 1

                if how_many_of_each_operators == "!":
                    fact_count += 1

            for fact_calculations in range(fact_count):

                fact_index = -1
                for fact_finder in data_list:
                    fact_index += 1

                    if fact_finder.isdigit() or fact_finder == ".":
                        pass

                    if fact_finder == "!":
                        try:
                            temp_answer = int(data_list[fact_index - 1])
                            temp_answer = factorial(temp_answer)

                        except:

                            calculation_answer = "Invalid input!"

                        data_list[fact_index - 1: fact_index + 1] = [str(temp_answer)]

            for sqrt_calculations in range(sqrt_count):

                sqrt_index = -1
                for sqrt_finder in data_list:
                    sqrt_index += 1

                    if sqrt_finder.isdigit() or sqrt_finder == ".":
                        pass

                    if sqrt_finder == "√":
                        try:
                            temp_answer = float(data_list[sqrt_index + 1])
                            temp_answer = sqrt(temp_answer)

                        except:

                            calculation_answer = "Invalid input!"

                        data_list[sqrt_index: sqrt_index + 2] = [str(temp_answer)]

            zero_plus = 0
            to_be_removed_from_the_begining_later_count = 0
            for power_calculations in range(power_count):

                power_index = -1
                for power_finder in data_list:
                    power_index += 1

                    if power_finder.isdigit() or power_finder == ".":
                        pass

                    if power_finder == "^":
                        first_number = data_list[power_index - 1]
                        second_number = data_list[power_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        if "-" in str(first_number) and "." in str(second_number):
                            calculation_answer = "Invalid input!"

                            data_list.clear()
                            break

                        try:
                            temp_answer = first_number ** second_number

                        except:

                            calculation_answer = "Over Flow!"

                        if "^" in data_list[power_index + 1:] or "*" in data_list[power_index + 1:] \
                                or "/" in data_list[power_index + 1:] or "+" in data_list[power_index + 1:] \
                                or "-" in data_list[power_index + 1:]:

                            starting_point = power_index - 1
                            ending_point = power_index + 2
                            data_list[starting_point: ending_point] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2


                        else:
                            starting_point = power_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            to_be_removed_from_the_begining_later_count = 0
            for times_and_fraction_calculations in range(times_count + fraction_count):

                times_or_fraction_index = -1

                for times_or_fraction_finder in data_list:

                    times_or_fraction_index += 1
                    if times_or_fraction_finder.isdigit() or times_or_fraction_finder == ".":
                        pass

                    if times_or_fraction_finder == "*":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)

                        temp_answer = first_number * second_number

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            data_list[starting_point: ending_point + 1] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

                    if times_or_fraction_finder == "/":
                        first_number = data_list[times_or_fraction_index - 1]
                        second_number = data_list[times_or_fraction_index + 1]

                        first_number = Decimal(first_number)
                        second_number = Decimal(second_number)
                        division_zero_count = 0
                        try:
                            temp_answer = first_number / second_number

                        except ZeroDivisionError:
                            calculation_answer = "Can't divide to zero!"

                            division_zero_count += 1

                        if "^" in data_list[times_or_fraction_index:] or "*" in data_list[times_or_fraction_index:] \
                                or "/" in data_list[times_or_fraction_index:] or "+" in data_list[
                                                                                        times_or_fraction_index:] \
                                or "-" in data_list[times_or_fraction_index:]:

                            starting_point = times_or_fraction_index - 1
                            ending_point = times_or_fraction_index + 1
                            if division_zero_count == 0:
                                try:
                                    data_list[starting_point: ending_point + 1] = [str(temp_answer)]

                                except ZeroDivisionError:
                                    calculation_answer = "Can't divide to zero!"
                                    break

                            else:
                                data_list = []

                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1
                            data_list.insert(0, "x")
                            data_list.insert(1, "+")
                            to_be_removed_from_the_begining_later_count += 2

                        else:
                            starting_point = times_or_fraction_index - 1
                            data_list[starting_point:] = [str(temp_answer)]
                            data_list.append("+")
                            data_list.append("0")
                            zero_plus += 1

            if to_be_removed_from_the_begining_later_count:
                for _ in range(to_be_removed_from_the_begining_later_count):
                    data_list.pop(0)

            x_count = 0
            for plus_and_mines_calculation in range(plus_count + mines_count):

                plus_or_mines_index = -1

                for plus_or_mines_finder in data_list:
                    plus_or_mines_index += 1

                    if plus_or_mines_finder != "-" or plus_or_mines_finder != "+":
                        pass

                    if plus_or_mines_finder == "+":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number + second_number

                            data_list[starting_point:] = [temp_answer]

                    if plus_or_mines_finder == "-":
                        first_number = data_list[plus_or_mines_index - 1]
                        second_number = data_list[plus_or_mines_index + 1]

                        if "^" in data_list[plus_or_mines_index + 1:] or "*" in data_list[plus_or_mines_index + 1:] \
                                or "/" in data_list[plus_or_mines_index + 1:] or "+" in data_list[
                                                                                        plus_or_mines_index + 1:] \
                                or "-" in data_list[plus_or_mines_index + 1:]:

                            starting_point = plus_or_mines_index - 1
                            ending_point = plus_or_mines_index + 2

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point: ending_point] = [temp_answer]
                            data_list.insert(0, "x")
                            x_count += 1


                        else:
                            starting_point = plus_or_mines_index - 1

                            first_number = Decimal(first_number)
                            second_number = Decimal(second_number)
                            temp_answer = first_number - second_number

                            data_list[starting_point:] = [temp_answer]

            for remover in range(x_count):
                data_list.pop(0)

            final_answer = ""
            if data_list:
                final_answer = data_list[0]

            if final_answer == "+":

                calculation_answer = ""


            else:
                if final_answer == "-0":
                    final_answer = "0"

    def fib_solver(data):
        try:
            data = data[4:-1:]
            calculation_with_out_printings(data=data)
            data = int(final_answer)
            n1 = 0
            n2 = 1
            if data < 0:
                calculation_answer = "More than zero is needed!"

            if data == 1:
                calculation_answer = "0"

            if data == 2:
                calculation_answer = "1"

            for _ in range(2, int(data) + 1):
                summation = n1 + n2
                n1 = n2
                n2 = summation

                calculation_answer = f"{n2} "

        except:
            calculation_answer = "Invalid input!"

    if "fib" in data:
        fib_solver(data)

    else:
        calculation(data)


    try:
        if float(calculation_answer).is_integer():
            calculation_answer = int(calculation_answer)

    except:
        pass

    if calculation_answer == "":
        user_language = get_user_current_language(user_id=user_id)

        calculation_answer = languages[user_language]['invalid_input']

    return calculation_answer
