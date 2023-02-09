import decimal


def bmi_calculator(weight, height):
    height = float(height) / 100
    weight = float(weight)

    if height == 0.0 and weight == 0.0:
        bmi = "Invalid height and weight input!"
        bmi_status = "Something went wrong!"
        return f"{bmi}", bmi_status

    elif height == 0.0 and weight != 0.0:
        bmi = "Invalid height input!"
        bmi_status = "Something went wrong!"
        return f"{bmi}", bmi_status

    elif height != 0.0 and weight == 0.0:
        bmi = "Invalid weight input!"
        bmi_status = "Something went wrong!"
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
            bmi_status = """You are extremely obese!
Please see a doctor as soon as possible.🧑🏻‍⚕️"""
        elif 30 <= float(bmi) < 35:
            bmi_status = """You are obese!
Please see a doctor as soon as possible.🧑🏻‍⚕️"""
        elif 25 <= float(bmi) < 30:
            bmi_status = """You are a little overweight!
Consider seeing a doctor.🧑🏻‍⚕️"""
        elif 18.5 <= float(bmi) < 25:
            bmi_status = """You are absolutely healthy!
Keep that body.⛹🏻"""
        elif 16.5 <= float(bmi) < 18.5:
            bmi_status = """You are a little underweight!
Please see a doctor as soon as possible.🧑🏻‍⚕️"""
        elif float(bmi) < 16.5:
            bmi_status = """You are way underweight!
Please see a doctor as soon as possible.🧑🏻‍⚕️"""

        else:
            bmi_status = "Something went wrong!"

        return f"{bmi} Kg/m²", bmi_status
