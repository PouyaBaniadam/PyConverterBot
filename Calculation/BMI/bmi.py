import decimal
from Settings.languages.languages_dictionary import languages
from Settings.languages.users_languages import get_user_current_language


def bmi_calculator(weight, height, user_id):
    height = float(height) / 100
    weight = float(weight)

    user_language = get_user_current_language(user_id=user_id)

    if height == 0.0 and weight == 0.0:
        bmi = languages[user_language]['invalid_height_and_weight_bmi']
        bmi_status = languages[user_language]['something_went_wrong_bmi']
        return f"{bmi}", bmi_status

    elif height == 0.0 and weight != 0.0:
        bmi = languages[user_language]['invalid_height_input']
        bmi_status = languages[user_language]['something_went_wrong_bmi']
        return f"{bmi}", bmi_status

    elif height != 0.0 and weight == 0.0:
        bmi = languages[user_language]['invalid_weight_input']
        bmi_status = languages[user_language]['something_went_wrong_bmi']
        return f"{bmi}", bmi_status

    else:
        bmi = weight / (height ** 2)
        if str(bmi).isdecimal():
            bmi = decimal.Decimal(bmi)

        try:
            bmi = round(float(bmi), 6)
        except:
            pass

        if float(bmi) >= 35:
            bmi_status = languages[user_language]['extremely_obese']

        elif 30 <= float(bmi) < 35:
            bmi_status = languages[user_language]['obese']

        elif 25 <= float(bmi) < 30:
            bmi_status = languages[user_language]['little_overweight']

        elif 18.5 <= float(bmi) < 25:
            bmi_status = languages[user_language]['healthy']

        elif 16.5 <= float(bmi) < 18.5:
            bmi_status = languages[user_language]['little_underweight']

        elif float(bmi) < 16.5:
            bmi_status = languages[user_language]['way_underweight']

        else:
            bmi_status = languages[user_language]['something_went_wrong_bmi']

        return f"{bmi} Kg/m²", bmi_status
