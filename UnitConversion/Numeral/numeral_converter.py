import string

from Settings.languages.languages_dictionary import languages


def numeral_converter(from_base, to_base, data, user_language):
    global global_answer, global_phrase, global_from_base, global_to_base
    if len(from_base) == 12:
        from_base = from_base[:2]
    if len(from_base) == 11:
        from_base = from_base[:1]

    if len(to_base) == 10:
        to_base = to_base[:2]
    if len(to_base) == 9:
        to_base = to_base[:1]

    global_from_base = int(from_base)
    global_to_base = int(to_base)
    number = data.replace(" ", "")
    global_phrase = number

    if global_from_base in range(2, 11) and not str(number).isdigit():
        global_answer = languages[user_language]['only_digits_in_this_starting_base']
        return global_answer, data, from_base, to_base,

    else:
        def base_2__9_10(global_from_base):
            global global_answer
            integer_list = []
            float_list = []
            integer_sum = 0
            float_sum = 0
            integer_power = 0
            float_power = 0

            num = number
            if "." not in num:
                num = num + "." + str(0)

            integer_num, float_num = num.split(".")

            for lenght_integer in integer_num:
                integer_list.append(int(lenght_integer))

            for lenght_decimal in float_num:
                float_list.append(int(lenght_decimal))

            if float_list == ["0"]:
                float_list = []

            while len(integer_list) != 0:
                integer_sum = (integer_list[-1]) * (
                        global_from_base ** integer_power) + integer_sum
                integer_power += 1
                integer_list.pop()

            if len(float_list) != 0:
                float_power = -abs(len(float_list))
                while len(float_list) != 0:
                    float_sum = (float_list[-1]) * (global_from_base ** float_power) + float_sum
                    float_power += 1
                    float_list.pop()

            if float_sum == 0:
                global_answer = integer_sum
                return global_answer
            else:
                global_answer = integer_sum + float_sum
                return global_answer

        def base_10_2__9(global_to_base):
            global global_answer
            integer_part_of_reversed_remainders_list = []
            float_num_in_row_list = []
            reversed_remainders = []
            first_part_of_float_list = []
            remainders = []

            num = number

            if "." not in num:
                num = num + "." + str(0)

            integer_num, float_num = num.split(".")

            float_num = str(0) + "." + str(float_num)

            while True:
                integer_remainder = int(integer_num) % global_to_base
                integer_num = int(integer_num) / global_to_base
                remainders.append(integer_remainder)
                if integer_num / global_to_base == 0:
                    break

            remainders.pop()

            for reverse in reversed(remainders):
                reversed_remainders.append(reverse)

            float_num = float(float_num)

            for repetation in range(15):
                float_num = float_num * global_to_base
                float_num = str(float_num)
                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                first_part_of_float_list.append(int(first_part_of_float_num))
                float_num = str(0) + "." + second_part_of_float_num
                second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                float_num = float(float_num)

            for integer_part_of_reversed_remainders in reversed_remainders:
                integer_part_of_reversed_remainders_list.append(str(integer_part_of_reversed_remainders))
            integer_part_of_reversed_remainders_list.append(".")

            for float_num_in_row in first_part_of_float_list:
                float_num_in_row_list.append(float_num_in_row)

            if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                integer_part_of_reversed_remainders_list.pop()

                x_list = []

                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                    x_list.append(integer_part_of_reversed_remainders_in_row)
                global_answer = "".join(map(str, x_list))
                return global_answer

            else:
                y_list = []
                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                    y_list.append(integer_part_of_reversed_remainders_in_row)

                for float_num_in_row in float_num_in_row_list:
                    y_list.append(float_num_in_row)

                global_answer = "".join(map(str, y_list))
                return global_answer

        def base_2__9_9__2(global_from_base, global_to_base):
            global global_answer
            remainders = []
            integer_list = []
            float_list = []
            integer_sum = 0
            float_sum = 0
            integer_power = 0
            float_power = 0

            num = number
            if "." not in num:
                num = num + "." + str(0)

            integer_num, float_num = num.split(".")

            for lenght_integer in integer_num:
                integer_list.append(int(lenght_integer))

            for lenght_decimal in float_num:
                float_list.append(int(lenght_decimal))

            if float_list == ["0"]:
                float_list = []

            while len(integer_list) != 0:
                integer_sum = (integer_list[-1]) * (
                        global_from_base ** integer_power) + integer_sum
                integer_power += 1
                integer_list.pop()

            if len(float_list) != 0:
                float_power = -abs(len(float_list))
                while len(float_list) != 0:
                    float_sum = (float_list[-1]) * (global_from_base ** float_power) + float_sum
                    float_power += 1
                    float_list.pop()

            if float_sum == 0:
                base_2__9_10_global_answer = integer_sum
            else:
                base_2__9_10_global_answer = integer_sum + float_sum

            if isinstance(base_2__9_10_global_answer, int):
                num = base_2__9_10_global_answer
                while True:
                    remainder = int(num % global_to_base)
                    num = int(num / global_to_base)
                    remainders.append(remainder)
                    if num / global_to_base == 0:
                        break

                x_list = []
                for reverse in reversed(remainders):
                    x_list.append(reverse)

                global_answer = "".join(map(str, x_list))
                return global_answer

            else:
                base_2__9_10_global_answer = str(base_2__9_10_global_answer)
                integer_part_of_reversed_remainders_list = []
                float_num_in_row_list = []
                reversed_remainders = []
                first_part_of_float_list = []
                remainders = []

                num = base_2__9_10_global_answer

                if "." not in num:
                    num = num + "." + str(0)

                integer_num, float_num = num.split(".")

                float_num = str(0) + "." + str(float_num)

                while True:
                    integer_remainder = int(integer_num) % global_to_base
                    integer_num = int(integer_num) / global_to_base
                    remainders.append(integer_remainder)
                    if integer_num / global_to_base == 0:
                        break

                remainders.pop()

                for reverse in reversed(remainders):
                    reversed_remainders.append(reverse)

                float_num = float(float_num)

                for repetation in range(15):
                    float_num = float_num * global_to_base
                    float_num = str(float_num)
                    first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                    first_part_of_float_list.append(int(first_part_of_float_num))
                    float_num = str(0) + "." + second_part_of_float_num
                    second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                    float_num = float(float_num)

                for integer_part_of_reversed_remainders in reversed_remainders:
                    integer_part_of_reversed_remainders_list.append(str(integer_part_of_reversed_remainders))
                integer_part_of_reversed_remainders_list.append(".")

                for float_num_in_row in first_part_of_float_list:
                    float_num_in_row_list.append(float_num_in_row)

                if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                    integer_part_of_reversed_remainders_list.pop()

                    x_list = []

                    for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                        x_list.append(integer_part_of_reversed_remainders_in_row)
                    global_answer = "".join(map(str, x_list))
                    return global_answer

                else:
                    y_list = []
                    for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                        y_list.append(integer_part_of_reversed_remainders_in_row)

                    for float_num_in_row in float_num_in_row_list:
                        y_list.append(float_num_in_row)

                    global_answer = "".join(map(str, y_list))
                    return global_answer

        def base_36__11_10(global_from_base):
            global global_answer
            integer_list_1 = []
            integer_list_2 = []
            integer_list_3 = []
            float_list_1 = []
            float_list_2 = []
            float_list_3 = []
            integer_sum = 0
            integer_power = 0
            float_sum = 0
            float_power = 0
            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10

            for i in range(0, 10):
                numbers_dictionary.update({int(i): int(numbers_values)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({str(j): int(alphabets_values)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = number
            num = num.upper()

            if "." not in num:
                for i in num:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                global_answer = integer_sum
                return global_answer

            else:
                integer_part, float_part = num.split(".")

                for i in integer_part:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                for x in float_part:
                    float_list_1.append(x)

                for y in float_list_1:
                    if y.isalpha():
                        float_list_2.append(y)

                    if y.isnumeric():
                        float_list_2.append(int(y))

                for z in float_list_2:
                    for t in final_dictionary:
                        if z == t:
                            float_list_3.append(final_dictionary[t])

                float_power = -abs(len(float_list_3))

                while len(float_list_3) != 0:
                    float_sum = float_sum + (float_list_3[-1]) * (
                            global_from_base ** float_power)
                    float_power += 1
                    float_list_3.pop()

                global_answer = integer_sum + float_sum
                return global_answer

        def base_11__36_36__11(global_from_base, global_to_base):
            global global_answer
            integer_list_1 = []
            integer_list_2 = []
            integer_list_3 = []
            float_list_1 = []
            float_list_2 = []
            float_list_3 = []
            integer_sum = 0
            integer_power = 0
            float_sum = 0
            float_power = 0
            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10

            for i in range(0, 10):
                numbers_dictionary.update({int(i): int(numbers_values)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({str(j): int(alphabets_values)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = number
            num = num.upper()

            if "." not in num:
                for i in num:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                global_answer = integer_sum

            else:
                integer_part, float_part = num.split(".")

                for i in integer_part:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                for x in float_part:
                    float_list_1.append(x)

                for y in float_list_1:
                    if y.isalpha():
                        float_list_2.append(y)

                    if y.isnumeric():
                        float_list_2.append(int(y))

                for z in float_list_2:
                    for t in final_dictionary:
                        if z == t:
                            float_list_3.append(final_dictionary[t])

                float_power = -abs(len(float_list_3))

                while len(float_list_3) != 0:
                    float_sum = float_sum + (float_list_3[-1]) * (
                            global_from_base ** float_power)
                    float_power += 1
                    float_list_3.pop()

                global_answer = integer_sum + float_sum

            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10
            remainders = []
            reversed_remainders = []
            none_dot_final_list = []
            first_part_of_float_num_list = []
            int_first_part_of_float_num_list = []
            value_of_first_part_of_float_num_list = []
            integer_remainders = []
            final_integer_remainders_list = []
            value_of_final_integer_remainders_list = []

            for i in range(0, 10):
                numbers_dictionary.update({int(numbers_values): int(i)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({int(alphabets_values): str(j)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = str(global_answer)

            if "." not in num:
                while True:
                    remainder = int(num) % global_to_base
                    num = int(num) / global_to_base
                    remainders.append(remainder)
                    if num / global_to_base == 0:
                        break
                remainders.pop()

                for i in reversed(remainders):
                    reversed_remainders.append(i)

                for j in reversed_remainders:
                    for t in final_dictionary:
                        if j == t:
                            none_dot_final_list.append(final_dictionary[t])

                x_list = []
                for x in none_dot_final_list:
                    x_list.append(x)

                global_answer = "".join((map(str, x_list)))
                return global_answer

            else:
                integer_num, float_num = num.split(".")
                integer_num = int(integer_num)
                float_num = str("0") + "." + float_num
                float_num = float(float_num)

                while True:
                    integer_remainder = int(integer_num) % global_to_base
                    integer_num = int(integer_num) / global_to_base
                    integer_remainders.append(integer_remainder)
                    if integer_num / global_to_base == 0:
                        break
                integer_remainders.pop()

                for k in reversed(integer_remainders):
                    final_integer_remainders_list.append(k)

                for h in final_integer_remainders_list:
                    for n in final_dictionary:
                        if h == n:
                            value_of_final_integer_remainders_list.append(final_dictionary[n])
                value_of_final_integer_remainders_list.append(".")

                for i in range(15):
                    float_num = float_num * global_to_base
                    float_num = str(float_num)
                    first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                    second_part_of_float_num = str(second_part_of_float_num)
                    second_part_of_float_num = str("0") + "." + second_part_of_float_num
                    first_part_of_float_num_list.append(first_part_of_float_num)
                    float_num = second_part_of_float_num
                    float_num = float(float_num)

                for j in first_part_of_float_num_list:
                    int_first_part_of_float_num_list.append(int(j))

                for x in int_first_part_of_float_num_list:
                    for y in final_dictionary:
                        if x == y:
                            value_of_first_part_of_float_num_list.append(final_dictionary[y])

                global_answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                y_list = []

                for f in global_answer_list:
                    y_list.append(f)

                global_answer = "".join((map(str, y_list)))
                return global_answer

        def base_10_11__36(global_to_base):
            global global_answer
            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10
            remainders = []
            reversed_remainders = []
            none_dot_final_list = []
            first_part_of_float_num_list = []
            int_first_part_of_float_num_list = []
            value_of_first_part_of_float_num_list = []
            integer_remainders = []
            final_integer_remainders_list = []
            value_of_final_integer_remainders_list = []

            for i in range(0, 10):
                numbers_dictionary.update({int(numbers_values): int(i)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({int(alphabets_values): str(j)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = number

            if "." not in num:
                while True:
                    remainder = int(num) % global_to_base
                    num = int(num) / global_to_base
                    remainders.append(remainder)
                    if num / global_to_base == 0:
                        break
                remainders.pop()

                for i in reversed(remainders):
                    reversed_remainders.append(i)

                for j in reversed_remainders:
                    for t in final_dictionary:
                        if j == t:
                            none_dot_final_list.append(final_dictionary[t])

                x_list = []
                for x in none_dot_final_list:
                    x_list.append(x)

                global_answer = "".join(map(str, x_list))
                return global_answer

            else:
                integer_num, float_num = num.split(".")
                integer_num = int(integer_num)
                float_num = str("0") + "." + float_num
                float_num = float(float_num)

                while True:
                    integer_remainder = int(integer_num) % global_to_base
                    integer_num = int(integer_num) / global_to_base
                    integer_remainders.append(integer_remainder)
                    if integer_num / global_to_base == 0:
                        break
                integer_remainders.pop()

                for k in reversed(integer_remainders):
                    final_integer_remainders_list.append(k)

                for h in final_integer_remainders_list:
                    for n in final_dictionary:
                        if h == n:
                            value_of_final_integer_remainders_list.append(final_dictionary[n])
                value_of_final_integer_remainders_list.append(".")

                for i in range(15):
                    float_num = float_num * global_to_base
                    float_num = str(float_num)
                    first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                    second_part_of_float_num = str(second_part_of_float_num)
                    second_part_of_float_num = str("0") + "." + second_part_of_float_num
                    first_part_of_float_num_list.append(first_part_of_float_num)
                    float_num = second_part_of_float_num
                    float_num = float(float_num)

                for j in first_part_of_float_num_list:
                    int_first_part_of_float_num_list.append(int(j))

                for x in int_first_part_of_float_num_list:
                    for y in final_dictionary:
                        if x == y:
                            value_of_first_part_of_float_num_list.append(final_dictionary[y])

                global_answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                y_list = []
                for f in global_answer_list:
                    y_list.append(f)

                global_answer = "".join(map(str, y_list))
                return global_answer

        def base_2__9_11__36(global_from_base, global_to_base):
            global global_answer
            integer_list = []
            float_list = []
            integer_sum = 0
            float_sum = 0
            integer_power = 0
            float_power = 0

            num = number
            if "." not in num:
                num = num + "." + str(0)

            integer_num, float_num = num.split(".")

            for lenght_integer in integer_num:
                integer_list.append(int(lenght_integer))

            for lenght_decimal in float_num:
                float_list.append(int(lenght_decimal))

            if float_list == ["0"]:
                float_list = []

            while len(integer_list) != 0:
                integer_sum = (integer_list[-1]) * (
                        global_from_base ** integer_power) + integer_sum
                integer_power += 1
                integer_list.pop()

            if len(float_list) != 0:
                float_power = -abs(len(float_list))
                while len(float_list) != 0:
                    float_sum = (float_list[-1]) * (global_from_base ** float_power) + float_sum
                    float_power += 1
                    float_list.pop()

            if float_sum == 0:
                global_answer = integer_sum
            else:
                global_answer = integer_sum + float_sum

            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10
            remainders = []
            reversed_remainders = []
            none_dot_final_list = []
            first_part_of_float_num_list = []
            int_first_part_of_float_num_list = []
            value_of_first_part_of_float_num_list = []
            integer_remainders = []
            final_integer_remainders_list = []
            value_of_final_integer_remainders_list = []

            for i in range(0, 10):
                numbers_dictionary.update({int(numbers_values): int(i)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({int(alphabets_values): str(j)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = global_answer
            num = str(num)

            if "." not in num:
                while True:
                    remainder = int(num) % global_to_base
                    num = int(num) / global_to_base
                    remainders.append(remainder)
                    if num / global_to_base == 0:
                        break
                remainders.pop()

                for i in reversed(remainders):
                    reversed_remainders.append(i)

                for j in reversed_remainders:
                    for t in final_dictionary:
                        if j == t:
                            none_dot_final_list.append(final_dictionary[t])

                x_list = []
                for x in none_dot_final_list:
                    x_list.append(x)

                global_answer = "".join(map(str, x_list))
                return global_answer

            else:
                integer_num, float_num = num.split(".")
                integer_num = int(integer_num)
                float_num = str("0") + "." + float_num
                float_num = float(float_num)

                while True:
                    integer_remainder = int(integer_num) % global_to_base
                    integer_num = int(integer_num) / global_to_base
                    integer_remainders.append(integer_remainder)
                    if integer_num / global_to_base == 0:
                        break
                integer_remainders.pop()

                for k in reversed(integer_remainders):
                    final_integer_remainders_list.append(k)

                for h in final_integer_remainders_list:
                    for n in final_dictionary:
                        if h == n:
                            value_of_final_integer_remainders_list.append(final_dictionary[n])
                value_of_final_integer_remainders_list.append(".")

                for i in range(15):
                    float_num = float_num * global_to_base
                    float_num = str(float_num)
                    first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                    second_part_of_float_num = str(second_part_of_float_num)
                    second_part_of_float_num = str("0") + "." + second_part_of_float_num
                    first_part_of_float_num_list.append(first_part_of_float_num)
                    float_num = second_part_of_float_num
                    float_num = float(float_num)

                for j in first_part_of_float_num_list:
                    int_first_part_of_float_num_list.append(int(j))

                for x in int_first_part_of_float_num_list:
                    for y in final_dictionary:
                        if x == y:
                            value_of_first_part_of_float_num_list.append(final_dictionary[y])

                global_answer_list = value_of_final_integer_remainders_list + value_of_first_part_of_float_num_list

                y_list = []
                for f in global_answer_list:
                    y_list.append(f)

                global_answer = "".join(map(str, y_list))
                return global_answer

        def base_36__11_9__2(global_from_base, global_to_base):
            global global_answer
            integer_list_1 = []
            integer_list_2 = []
            integer_list_3 = []
            float_list_1 = []
            float_list_2 = []
            float_list_3 = []
            integer_sum = 0
            integer_power = 0
            float_sum = 0
            float_power = 0
            numbers_dictionary = {}
            numbers_values = 0
            alphabets_dictionary = {}
            alphabets_values = 10

            for i in range(0, 10):
                numbers_dictionary.update({int(i): int(numbers_values)})
                numbers_values += 1

            for j in string.ascii_uppercase:
                alphabets_dictionary.update({str(j): int(alphabets_values)})
                alphabets_values += 1

            final_dictionary = {**numbers_dictionary, **alphabets_dictionary}

            num = number
            num = num.upper()

            if "." not in num:
                for i in num:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                global_answer = integer_sum

            else:
                integer_part, float_part = num.split(".")

                for i in integer_part:
                    integer_list_1.append(i)

                for j in integer_list_1:
                    if j.isalpha():
                        integer_list_2.append(j)

                    if j.isnumeric():
                        integer_list_2.append(int(j))

                for a in integer_list_2:
                    for b in final_dictionary:
                        if a == b:
                            integer_list_3.append(final_dictionary[b])

                while len(integer_list_3) != 0:
                    integer_sum = integer_sum + (
                            integer_list_3[-1] * (global_from_base ** integer_power))
                    integer_power += 1
                    integer_list_3.pop()

                for x in float_part:
                    float_list_1.append(x)

                for y in float_list_1:
                    if y.isalpha():
                        float_list_2.append(y)

                    if y.isnumeric():
                        float_list_2.append(int(y))

                for z in float_list_2:
                    for t in final_dictionary:
                        if z == t:
                            float_list_3.append(final_dictionary[t])

                float_power = -abs(len(float_list_3))

                while len(float_list_3) != 0:
                    float_sum = float_sum + (float_list_3[-1]) * (
                            global_from_base ** float_power)
                    float_power += 1
                    float_list_3.pop()

                global_answer = integer_sum + float_sum

            integer_part_of_reversed_remainders_list = []
            float_num_in_row_list = []
            reversed_remainders = []
            first_part_of_float_list = []
            remainders = []

            num = global_answer
            num = str(num)

            if "." not in num:
                num = num + "." + str(0)

            integer_num, float_num = num.split(".")

            float_num = str(0) + "." + str(float_num)

            while True:
                integer_remainder = int(integer_num) % global_to_base
                integer_num = int(integer_num) / global_to_base
                remainders.append(integer_remainder)
                if integer_num / global_to_base == 0:
                    break

            remainders.pop()

            for reverse in reversed(remainders):
                reversed_remainders.append(reverse)

            float_num = float(float_num)

            for repetation in range(15):
                float_num = float_num * global_to_base
                float_num = str(float_num)
                first_part_of_float_num, second_part_of_float_num = float_num.split(".")
                first_part_of_float_list.append(int(first_part_of_float_num))
                float_num = str(0) + "." + second_part_of_float_num
                second_part_of_float_num = str(0) + "." + str(second_part_of_float_num)
                float_num = float(float_num)

            for integer_part_of_reversed_remainders in reversed_remainders:
                integer_part_of_reversed_remainders_list.append(str(integer_part_of_reversed_remainders))
            integer_part_of_reversed_remainders_list.append(".")

            for float_num_in_row in first_part_of_float_list:
                float_num_in_row_list.append(float_num_in_row)

            if float_num_in_row_list and all(elements == 0 for elements in float_num_in_row_list):
                integer_part_of_reversed_remainders_list.pop()

                x_list = []
                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                    x_list.append(integer_part_of_reversed_remainders_in_row)

                global_answer = "".join(map(str, x_list))
                return global_answer

            else:
                y_list = []
                for integer_part_of_reversed_remainders_in_row in integer_part_of_reversed_remainders_list:
                    y_list.append(integer_part_of_reversed_remainders_in_row)

                for float_num_in_row in float_num_in_row_list:
                    y_list.append(float_num_in_row)

                global_answer = "".join(map(str, y_list))
                return global_answer

        if global_from_base in range(2, 11) and global_to_base == 10:
            base_2__9_10(global_from_base)

        if global_from_base == 10 and global_to_base in range(2, 11):
            base_10_2__9(global_to_base)

        if global_from_base in range(2, 10) and global_to_base in range(2,
                                                                        10):
            base_2__9_9__2(global_from_base, global_to_base)

        if global_from_base in range(11, 37) and global_to_base == 10:
            base_36__11_10(global_from_base)

        if global_from_base == 10 and global_to_base in range(11, 37):
            base_10_11__36(global_to_base)

        if global_from_base in range(2, 10) and global_to_base in range(
                11, 37):
            base_2__9_11__36(global_from_base, global_to_base)

        if global_from_base in range(11, 37) and global_to_base in range(
                2, 10):
            base_36__11_9__2(global_from_base, global_to_base)

        if global_from_base in range(11, 37) and global_to_base in range(
                11, 37):
            base_11__36_36__11(global_from_base, global_to_base)

        if global_answer == "":
            global_answer = "0"

        return global_answer, data, from_base, to_base,
