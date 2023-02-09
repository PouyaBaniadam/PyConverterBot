from math import pi
from aiogram import Bot, Dispatcher, executor
from Calculation.BMI.bmi import bmi_calculator
from Calculation.Calculator.calculator import calculator
from UnitConversion.Data.data_converter import data_converter
from UnitConversion.Length.length_converter import length_converter
from UnitConversion.Mass.mass_converter import mass_converter
from UnitConversion.Numeral.numeral_converter import numeral_converter
from UnitConversion.Temperature.temperature_converter import temperature_converter
from UnitConversion.Time.time_converter import time_converter
from keyboards_and_callbacks_data_list import *

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

calculator_mode = False
numeral_system_flag = False
bmi_calculator_flag = False


@dp.message_handler(commands="help")
async def welcome(message: types.Message):
    await message.reply(
        """This bot is made for some handy math stuff such as calculator , or popular conversions such as length , mass , data and much more.
The bot is easy to use.🤖 You just have to follow the correct directions.
for example , if you wanna use the calculator , all you have to do is to stick to buttons related to calculator.😀

Hope that helped , but if you can't find your way in , you can still choose help button for each part individually in the next update of the bot.😁
""")

    await bot.send_video(video=open('Assets/Videos/Tutorial/MainTutorial.mp4', 'rb'), chat_id=message.chat.id)


@dp.message_handler(commands="about")
async def welcome(message: types.Message):
    await message.reply(
        """100000100111011111010011001101101100111111101101001
        
I'm PouyaLj. I'm not allowed to call myself a programmer yet ; but still , love to code.👨🏻‍💻

100000100111011111010011001101101100111111101101001""")


@dp.message_handler(commands="start")
async def welcome(message: types.Message):
    await message.reply("""Please select bot mode from the list below.👇🏻""", reply_markup=bot_options_keyboard())


@dp.message_handler()
async def options_keyboard_answer(message: types.Message):
    global calculator_mode

    if message.text == "BMI":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your weight-number (kg) : ",
                               reply_markup=bmi__conversion_weight_inline_keyboard())

    if message.text == "Calculation":
        await bot.send_message(chat_id=message.chat.id,
                               text="""Please choose one of the calculators from the list below.👇🏻""",
                               reply_markup=calculation__options_keyboard())

    if message.text == "Calculator":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your phrase : ",
                               reply_markup=calculator__inline_keyboard())
        calculator_mode = True

    if message.text == "Unit Conversion":
        await message.answer("Which of the following conversions do you prefer to use ?👇🏻",
                             reply_markup=unit_conversion_options_keyboard())

    if message.text == "Data":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your data-number : ",
                               reply_markup=data_conversion_numbers_inline_keyboard())

    if message.text == "Length":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your length-number : ",
                               reply_markup=length_conversion_numbers_inline_keyboard())

    if message.text == "Mass":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your mass-number : ",
                               reply_markup=mass_conversion_numbers_inline_keyboard())

    if message.text == "Numeral":
        await message.answer("Please enter your numeral-number : ",
                             reply_markup=numeral_conversion_numbers_inline_keyboard())

    if message.text == "Temperature":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your temperature-number : ",
                               reply_markup=temperature_conversion_numbers_inline_keyboard())

    if message.text == "Time":
        await bot.send_message(chat_id=message.chat.id, text="Please enter your time-number : ",
                               reply_markup=time_conversion_numbers_inline_keyboard())

    if message.text == "⬅️ Back ⬅️":
        await bot.send_message(chat_id=message.chat.id, text="""Please select bot mode from the list below.👇🏻""",
                               reply_markup=bot_options_keyboard())


@dp.callback_query_handler()
async def query_handler(call: types.CallbackQuery):
    global from_base, to_base, weight_unit, height_unit, first_symbol, number, numeral_data
    global weight, height
    global phrase, numeral_system_flag

    chat_id = call.from_user.id
    message_id = call.message.message_id
    message = call.data

    if message in bmi_conversion_weight_callback_data_list:
        text = call.message.text

        if "weight" in text:
            text = ""

        if message == "0_weight_bmi":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "1_weight_bmi":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "2_weight_bmi":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "3_weight_bmi":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "4_weight_bmi":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "5_weight_bmi":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "6_weight_bmi":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "7_weight_bmi":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "8_weight_bmi":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "9_weight_bmi":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())
        if message == "dot_weight_bmi":
            if "." not in call.message.text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=bmi__conversion_weight_inline_keyboard())

        if message == "clear_weight_bmi":
            text = "Please enter your weight-number (kg) : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())

        if message == "backward_weight_bmi":
            text = text[:-1]
            if text == "":
                text = "Please enter your weight-number (kg) : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())

        if message == "done_weight_bmi":
            weight = call.message.text
            if "weight" not in weight:
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text="Please enter your height-number (cm) : ",
                                            reply_markup=bmi__conversion_height_inline_keyboard())

    if message in bmi_conversion_height_callback_data_list:
        text = call.message.text

        if "height" in text:
            text = ""

        if message == "0_height_bmi":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "1_height_bmi":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "2_height_bmi":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "3_height_bmi":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "4_height_bmi":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "5_height_bmi":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "6_height_bmi":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "7_height_bmi":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "8_height_bmi":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "9_height_bmi":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())
        if message == "dot_height_bmi":
            if "." not in call.message.text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=bmi__conversion_height_inline_keyboard())

        if message == "backward_height_bmi":
            text = text[:-1]
            if text == "":
                text = "Please enter your height-number (cm) : "

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())

        if message == "clear_height_bmi":
            text = "Please enter your height-number (cm) : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())

        if message == "done_height_bmi":
            height = call.message.text
            if "height" not in height:
                await bot.edit_message_text(text=f"""Weight : {weight} kg
Height : {height} cm

BMI : {bmi_calculator(weight=float(weight), height=float(height))[0]}

BMI Status : {bmi_calculator(weight=float(weight), height=float(height))[1]}""", chat_id=chat_id, message_id=message_id,
                                            reply_markup=bmi__conversion_see_bmi_chart_inline_keyboard())

    if message in bmi__conversion_see_bmi_chart_callback_data_list:
        if message == "see_chart_bmi":
            await bot.send_photo(photo=open('Assets/Images/BMI/BMIChart.jpg', 'rb'), chat_id=chat_id,
                                 caption="BMI chart")

    if message in calculator_callback_data_list:
        digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        text = call.message.text

        if "phrase" in text:
            text = ""

        if message == "0_calculator":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "1_calculator":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "2_calculator":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "3_calculator":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "4_calculator":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "5_calculator":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "6_calculator":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "7_calculator":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "8_calculator":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "9_calculator":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "dot_calculator":
            text += "."
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "plus_calculator":
            text += "+"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "mines_calculator":
            text += "-"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "times_calculator":
            text += "×"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "fraction_calculator":
            text += "÷"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "sin_calculator":
            text += "sin"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "cos_calculator":
            text += "cos"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "tan_calculator":
            text += "tan"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "cot_calculator":
            text += "cot"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "pi_calculator":
            try:
                if text[-1] in digits:
                    text += f"×{str(pi)[:8]}"
                else:
                    text += f"{str(pi)[:8]}"
            except IndexError:
                text += f"{str(pi)[:8]}"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "opening_parentheses_calculator":
            text += "("
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "closing_parentheses_calculator":
            text += ")"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "factorial_calculator":
            text += "!"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "power_calculator":
            text += "^"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "sqrt_calculator":
            text += "√"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "log_calculator":
            text += "log"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "neg_or_pos_maker_calculator":
            if text[0] == "-":
                text = text[1:]
            elif text[0] in digits:
                text = f"-{text}"
            elif text[0] == "+":
                text = f"-{text}"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "backward_calculator":
            text = text[:-1]
            if text == "":
                text = "Please enter your phrase : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "clear_calculator":
            text = "Please enter your phrase : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "done_calculator":
            data_to_be_calculate = call.message.text

            await bot.edit_message_text(text=f"""{data_to_be_calculate} = {calculator(data_to_be_calculate)}""",
                                        chat_id=chat_id, message_id=message_id)

    if message in data_conversion_callback_data_list:
        text = call.message.text

        if "data" in text:
            text = ""

        if message == "0_data_converter":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "1_data_converter":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "2_data_converter":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "3_data_converter":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "4_data_converter":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "5_data_converter":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "6_data_converter":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "7_data_converter":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "8_data_converter":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "9_data_converter":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "dot_data_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "clear_data_converter":
            text = "Please enter your data-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "backward_data_converter":
            text = text[:-1]
            if text == "":
                text = "Please enter your data-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "done_data_converter":
            number = text
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please enter the data-unit that you want to start the conversion with : ",
                                        reply_markup=data_conversion_starter_inline_keyboard())

        if message == "bit_data_conversion_starter":
            first_symbol = "b"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "byte_data_conversion_starter":
            first_symbol = "B"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "kilo_byte_data_conversion_starter":
            first_symbol = "KB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "mega_byte_data_conversion_starter":
            first_symbol = "MB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "giga_byte_data_conversion_starter":
            first_symbol = "GB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "tera_byte_data_conversion_starter":
            first_symbol = "TB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "peta_byte_data_conversion_starter":
            first_symbol = "PB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "exa_byte_data_conversion_starter":
            first_symbol = "EB"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=data_conversion_destination_inline_keyboard())

        if message == "bit_data_conversion_destination":
            second_symbol = "b"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "byte_data_conversion_destination":
            second_symbol = "B"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "kilo_byte_data_conversion_destination":
            second_symbol = "KB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "mega_byte_data_conversion_destination":
            second_symbol = "MB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "giga_byte_data_conversion_destination":
            second_symbol = "GB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "tera_byte_data_conversion_destination":
            second_symbol = "TB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "peta_byte_data_conversion_destination":
            second_symbol = "PB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "exa_byte_data_conversion_destination":
            second_symbol = "EB"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {data_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

    if message in length_conversion_callback_data_list:
        text = call.message.text

        if "length" in text:
            text = ""

        if message == "0_length_converter":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "1_length_converter":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "2_length_converter":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "3_length_converter":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "4_length_converter":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "5_length_converter":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "6_length_converter":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "7_length_converter":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "8_length_converter":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "9_length_converter":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "dot_length_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "clear_length_converter":
            text = "Please enter your length-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "backward_length_converter":
            text = text[:-1]
            if text == "":
                text = "Please enter your length-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "done_length_converter":
            number = text
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please enter the length-unit that you want to start the conversion with : "
                                        , reply_markup=length_conversion_starter_inline_keyboard())

        if message == "pico_meter_length_conversion_starter":
            first_symbol = "pm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "nano_meter_length_conversion_starter":
            first_symbol = "nm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "micro_meter_length_conversion_starter":
            first_symbol = "μm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "milli_meter_length_conversion_starter":
            first_symbol = "mm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "centi_meter_length_conversion_starter":
            first_symbol = "cm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "desi_meter_length_conversion_starter":
            first_symbol = "dm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "meter_length_conversion_starter":
            first_symbol = "m"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "kilo_meter_length_conversion_starter":
            first_symbol = "Km"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "mile_length_conversion_starter":
            first_symbol = "mi"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "nautical_mile_length_conversion_starter":
            first_symbol = "nmi"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "foot_length_conversion_starter":
            first_symbol = "ft"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "inch_length_conversion_starter":
            first_symbol = "in"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "yard_length_conversion_starter":
            first_symbol = "yd"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "femara_length_conversion_starter":
            first_symbol = "fur"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "fathom_length_conversion_starter":
            first_symbol = "ftm"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "chi_length_conversion_starter":
            first_symbol = "chi"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "gongli_length_conversion_starter":
            first_symbol = "gongli"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "light_year_length_conversion_starter":
            first_symbol = "ly"
            await bot.edit_message_text(
                text="Please enter the length-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=length_conversion_destination_inline_keyboard())

        if message == "pico_meter_length_conversion_destination":
            second_symbol = "pm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "nano_meter_length_conversion_destination":
            second_symbol = "nm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "micro_meter_length_conversion_destination":
            second_symbol = "μm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "milli_meter_length_conversion_destination":
            second_symbol = "mm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "centi_meter_length_conversion_destination":
            second_symbol = "cm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "desi_meter_length_conversion_destination":
            second_symbol = "dm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "meter_length_conversion_destination":
            second_symbol = "m"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "kilo_meter_length_conversion_destination":
            second_symbol = "Km"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "mile_length_conversion_destination":
            second_symbol = "mi"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "nautical_mile_length_conversion_starter":
            second_symbol = "nmi"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "foot_length_conversion_destination":
            second_symbol = "ft"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "inch_length_conversion_destination":
            second_symbol = "in"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "yard_length_conversion_destination":
            second_symbol = "yd"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "femara_length_conversion_destination":
            second_symbol = "fur"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "fathom_length_conversion_destination":
            second_symbol = "ftm"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "chi_length_conversion_destination":
            second_symbol = "chi"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "gongli_length_conversion_destination":
            second_symbol = "gongli"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "light_year_length_conversion_destination":
            second_symbol = "ly"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {length_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                    number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

    if message in mass_conversion_callback_data_list:
        text = call.message.text

        if "mass" in text:
            text = ""

        if message == "0_mass_converter":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "1_mass_converter":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "2_mass_converter":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "3_mass_converter":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "4_mass_converter":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "5_mass_converter":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "6_mass_converter":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "7_mass_converter":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "8_mass_converter":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "9_mass_converter":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "dot_mass_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "clear_mass_converter":
            text = "Please enter your mass-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "backward_mass_converter":
            text = text[:-1]
            if text == "":
                text = "Please enter your mass-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "done_mass_converter":
            number = text
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please enter the mass-unit that you want to start the conversion with : "
                                        , reply_markup=mass_conversion_starter_inline_keyboard())

        if message == "nano_gram_mass_conversion_starter":
            first_symbol = "ng"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "micro_gram_mass_conversion_starter":
            first_symbol = "μg"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "quintal_mass_conversion_starter":
            first_symbol = "q"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "mili_gram_mass_conversion_starter":
            first_symbol = "mg"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "centi_gram_mass_conversion_starter":
            first_symbol = "cg"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "desi_gram_mass_conversion_starter":
            first_symbol = "dg"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "gram_mass_conversion_starter":
            first_symbol = "g"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "kilo_gram_mass_conversion_starter":
            first_symbol = "Kg"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "tone_mass_conversion_starter":
            first_symbol = "t"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "pound_mass_conversion_starter":
            first_symbol = "lb"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "ounce_mass_conversion_starter":
            first_symbol = "oz"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "carat_mass_conversion_starter":
            first_symbol = "ct"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "grain_mass_conversion_starter":
            first_symbol = "gr"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "long_ton_mass_conversion_starter":
            first_symbol = "l.t"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "short_ton_mass_conversion_starter":
            first_symbol = "sh.t"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "stone_mass_conversion_starter":
            first_symbol = "st"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "dram_mass_conversion_starter":
            first_symbol = "dr"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "dan_mass_conversion_starter":
            first_symbol = "dan"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "sir_mass_conversion_starter":
            first_symbol = "sir"
            await bot.edit_message_text(
                text="Please enter the mass-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=mass_conversion_destination_inline_keyboard())

        if message == "nano_gram_mass_conversion_destination":
            second_symbol = "ng"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "micro_gram_mass_conversion_destination":
            second_symbol = "μg"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "quintal_mass_conversion_destination":
            second_symbol = "q"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "mili_gram_mass_conversion_destination":
            second_symbol = "mg"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "centi_gram_mass_conversion_destination":
            second_symbol = "cg"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "desi_gram_mass_conversion_destination":
            second_symbol = "dg"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "gram_mass_conversion_destination":
            second_symbol = "g"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "kilo_gram_mass_conversion_destination":
            second_symbol = "Kg"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "tone_mass_conversion_destination":
            second_symbol = "t"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "pound_mass_conversion_destination":
            second_symbol = "lb"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "ounce_mass_conversion_destination":
            second_symbol = "oz"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "carat_mass_conversion_destination":
            second_symbol = "ct"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "grain_mass_conversion_destination":
            second_symbol = "gr"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "long_ton_mass_conversion_destination":
            second_symbol = "l.t"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "short_ton_mass_conversion_destination":
            second_symbol = "sh.t"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "stone_mass_conversion_destination":
            second_symbol = "st"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "dram_mass_conversion_destination":
            second_symbol = "dr"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "dan_mass_conversion_destination":
            second_symbol = "dan"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

        if message == "sir_mass_conversion_destination":
            second_symbol = "sir"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {mass_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id,
                message_id=message_id)

    if message in numeral_conversion_callback_data_list:
        phrase = call.message.text

        if "numeral" in phrase:
            phrase = ""

        if message == "0_numeral_converter":
            phrase += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "1_numeral_converter":
            phrase += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "2_numeral_converter":
            phrase += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "3_numeral_converter":
            phrase += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "4_numeral_converter":
            phrase += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "5_numeral_converter":
            phrase += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "6_numeral_converter":
            phrase += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "7_numeral_converter":
            phrase += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "8_numeral_converter":
            phrase += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "9_numeral_converter":
            phrase += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "dot_numeral_converter":
            phrase += "."
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "clear_numeral_converter":
            phrase = "Please enter your numeral-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "backward_numeral_converter":
            phrase = phrase[:-1]
            if phrase == "":
                phrase = "Please enter your numeral-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "a_numeral_converter":
            phrase += "A"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "b_numeral_converter":
            phrase += "B"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "c_numeral_converter":
            phrase += "C"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "d_numeral_converter":
            phrase += "D"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "e_numeral_converter":
            phrase += "E"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "f_numeral_converter":
            phrase += "F"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "g_numeral_converter":
            phrase += "G"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "h_numeral_converter":
            phrase += "H"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "i_numeral_converter":
            phrase += "I"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "j_numeral_converter":
            phrase += "J"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "k_numeral_converter":
            phrase += "K"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "l_numeral_converter":
            phrase += "L"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "m_numeral_converter":
            phrase += "M"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "n_numeral_converter":
            phrase += "N"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "o_numeral_converter":
            phrase += "O"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "p_numeral_converter":
            phrase += "P"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "q_numeral_converter":
            phrase += "Q"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "r_numeral_converter":
            phrase += "R"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "s_numeral_converter":
            phrase += "S"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "t_numeral_converter":
            phrase += "T"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "u_numeral_converter":
            phrase += "U"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "v_numeral_converter":
            phrase += "V"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "w_numeral_converter":
            phrase += "W"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "x_numeral_converter":
            phrase += "X"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "y_numeral_converter":
            phrase += "Y"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "z_numeral_converter":
            phrase += "Z"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "done_numeral_converter":
            numeral_data = phrase
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select starting base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_from_base_inline_keyboard())

        if message == "2_from_base":
            from_base = "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "3_from_base":
            from_base = "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "4_from_base":
            from_base = "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "5_from_base":
            from_base = "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "6_from_base":
            from_base = "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "7_from_base":
            from_base = "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "8_from_base":
            from_base = "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "9_from_base":
            from_base = "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "10_from_base":
            from_base = "10"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "11_from_base":
            from_base = "11"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "12_from_base":
            from_base = "12"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "13_from_base":
            from_base = "13"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "14_from_base":
            from_base = "14"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "15_from_base":
            from_base = "15"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "16_from_base":
            from_base = "16"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "17_from_base":
            from_base = "17"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "18_from_base":
            from_base = "18"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "19_from_base":
            from_base = "19"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "20_from_base":
            from_base = "20"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "21_from_base":
            from_base = "21"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "22_from_base":
            from_base = "22"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "23_from_base":
            from_base = "23"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "24_from_base":
            from_base = "24"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "25_from_base":
            from_base = "25"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "26_from_base":
            from_base = "26"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "27_from_base":
            from_base = "27"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "28_from_base":
            from_base = "28"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "29_from_base":
            from_base = "29"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "30_from_base":
            from_base = "30"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "31_from_base":
            from_base = "31"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "32_from_base":
            from_base = "32"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "33_from_base":
            from_base = "33"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "34_from_base":
            from_base = "34"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "35_from_base":
            from_base = "35"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "36_from_base":
            from_base = "36"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please select ending base from the list below.👇🏻",
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "2_to_base":
            to_base = "2"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "3_to_base":
            to_base = "3"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "4_to_base":
            to_base = "4"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "5_to_base":
            to_base = "5"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "6_to_base":
            to_base = "6"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "7_to_base":
            to_base = "7"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "8_to_base":
            to_base = "8"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "9_to_base":
            to_base = "9"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "10_to_base":
            to_base = "10"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "11_to_base":
            to_base = "11"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "12_to_base":
            to_base = "12"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "13_to_base":
            to_base = "13"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "14_to_base":
            to_base = "14"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "15_to_base":
            to_base = "15"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "16_to_base":
            to_base = "16"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "17_to_base":
            to_base = "17"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "18_to_base":
            to_base = "18"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "19_to_base":
            to_base = "19"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "20_to_base":
            to_base = "20"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "21_to_base":
            to_base = "21"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "22_to_base":
            to_base = "22"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "23_to_base":
            to_base = "23"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "24_to_base":
            to_base = "24"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "25_to_base":
            to_base = "25"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "26_to_base":
            to_base = "26"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "27_to_base":
            to_base = "27"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "28_to_base":
            to_base = "28"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "29_to_base":
            to_base = "29"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "30_to_base":
            to_base = "30"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "31_to_base":
            to_base = "31"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "32_to_base":
            to_base = "32"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "33_to_base":
            to_base = "33"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "34_to_base":
            to_base = "34"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "35_to_base":
            to_base = "35"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

        if message == "36_to_base":
            to_base = "36"
            await bot.edit_message_text(
                text=f"""Phrase : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[1]}
From base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[2]}
To base : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[3]}

Answer : {numeral_converter(from_base=from_base, to_base=to_base, data=numeral_data)[0]}""", chat_id=chat_id,
                message_id=message_id)

    if message in temperature_conversion_callback_data_list:
        text = call.message.text

        if "temperature" in text:
            text = ""

        if message == "0_temperature_converter":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "1_temperature_converter":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "2_temperature_converter":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "3_temperature_converter":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "4_temperature_converter":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "5_temperature_converter":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "6_temperature_converter":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "7_temperature_converter":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "8_temperature_converter":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "9_temperature_converter":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "dot_temperature_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "clear_temperature_converter":
            text = "Please enter your temperature-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "backward_temperature_converter":
            text = text[:-1]
            if text == "":
                text = "Please enter your temperature-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "done_temperature_converter":
            number = text
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please enter the temperature-unit that you want to start the conversion with : ",
                                        reply_markup=temperature_conversion_starter_inline_keyboard())

        if message == "celsius_temperature_conversion_starter":
            first_symbol = "C°"
            await bot.edit_message_text(
                text="Please enter the temperature-unit that you want to finish the conversion with : ",
                chat_id=chat_id,
                message_id=message_id, reply_markup=temperature_conversion_destination_inline_keyboard())

        if message == "fahrenheit_temperature_conversion_starter":
            first_symbol = "F°"
            await bot.edit_message_text(
                text="Please enter the temperature-unit that you want to finish the conversion with : ",
                chat_id=chat_id,
                message_id=message_id, reply_markup=temperature_conversion_destination_inline_keyboard())

        if message == "kelvin_temperature_conversion_starter":
            first_symbol = "K"
            await bot.edit_message_text(
                text="Please enter the temperature-unit that you want to finish the conversion with : ",
                chat_id=chat_id,
                message_id=message_id, reply_markup=temperature_conversion_destination_inline_keyboard())

        if message == "celsius_temperature_conversion_destination":
            second_symbol = "C°"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {temperature_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                         number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "fahrenheit_temperature_conversion_destination":
            second_symbol = "F°"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {temperature_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                         number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "kelvin_temperature_conversion_destination":
            second_symbol = "K"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {temperature_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                         number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

    if message in time_conversion_callback_data_list:
        text = call.message.text

        if "time" in text:
            text = ""

        if message == "0_time_converter":
            text += "0"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "1_time_converter":
            text += "1"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "2_time_converter":
            text += "2"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "3_time_converter":
            text += "3"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "4_time_converter":
            text += "4"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "5_time_converter":
            text += "5"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "6_time_converter":
            text += "6"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "7_time_converter":
            text += "7"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "8_time_converter":
            text += "8"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "9_time_converter":
            text += "9"
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "dot_time_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "clear_time_converter":
            text = "Please enter your time-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "backward_time_converter":
            text = text[:-1]
            if text == "":
                text = "Please enter your time-number : "
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "done_time_converter":
            number = text
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text="Please enter the time-unit that you want to start the conversion with : "
                                        , reply_markup=time_conversion_starter_inline_keyboard())

        if message == "pico_second_time_conversion_starter":
            first_symbol = "ps"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "nano_second_time_conversion_starter":
            first_symbol = "ns"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "micro_second_time_conversion_starter":
            first_symbol = "μs"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "milli_second_time_conversion_starter":
            first_symbol = "ms"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "second_time_conversion_starter":
            first_symbol = "s"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "min_time_conversion_starter":
            first_symbol = "min"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "hour_time_conversion_starter":
            first_symbol = "h"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "day_time_conversion_starter":
            first_symbol = "d"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "month_time_conversion_starter":
            first_symbol = "mo"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "year_time_conversion_starter":
            first_symbol = "y"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "decade_time_conversion_starter":
            first_symbol = "dec"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "century_time_conversion_starter":
            first_symbol = "cent"
            await bot.edit_message_text(
                text="Please enter the time-unit that you want to finish the conversion with : ", chat_id=chat_id,
                message_id=message_id, reply_markup=time_conversion_destination_inline_keyboard())

        if message == "pico_second_time_conversion_destination":
            second_symbol = "ps"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "nano_second_time_conversion_destination":
            second_symbol = "ns"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "micro_second_time_conversion_destination":
            second_symbol = "μs"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "milli_second_time_conversion_destination":
            second_symbol = "ms"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "second_time_conversion_destination":
            second_symbol = "s"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "min_time_conversion_destination":
            second_symbol = "min"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "hour_time_conversion_destination":
            second_symbol = "h"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "day_time_conversion_destination":
            second_symbol = "d"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "month_time_conversion_destination":
            second_symbol = "mo"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "year_time_conversion_destination":
            second_symbol = "y"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "decade_time_conversion_destination":
            second_symbol = "dec"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)

        if message == "century_time_conversion_destination":
            second_symbol = "cent"
            await bot.edit_message_text(
                text=f"""{number}{first_symbol} = {time_converter(first_symbol=first_symbol, second_symbol=second_symbol,
                                                                  number=number)}{second_symbol}""",
                chat_id=chat_id, message_id=message_id)


executor.start_polling(dp)
