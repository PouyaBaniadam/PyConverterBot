import time
from random import randint
import tracemalloc
from math import pi
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ChatActions
from Assets.AnimatedStickers.animated import animated_dictionary
from Calculation.BMI.bmi import bmi_calculator
from Calculation.Calculator.calculator import calculator
from Currency.currency import momentarily_currency_rate
from DataBase.Users.users_info import add_id_to_sql, fetch_id_from_sql
from Date.date import jalali_getter, gregorian_getter, current_time_getter, jalali_to_gregorian, gregorian_to_jalali
from Settings.languages.users_languages import users_first_language, user_language_update, get_user_current_language
from UnitConversion.Data.data_converter import data_converter
from UnitConversion.Length.length_converter import length_converter
from UnitConversion.Mass.mass_converter import mass_converter
from UnitConversion.Numeral.numeral_converter import numeral_converter
from UnitConversion.Temperature.temperature_converter import temperature_converter
from UnitConversion.Time.time_converter import time_converter
from keyboards_and_callbacks_data_list import *

tracemalloc.start()

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

user_ids = []
states = {}
bmi_status = {}
data_status = {}
length_status = {}
mass_status = {}
numeral_status = {}
temperature_status = {}
time_status = {}
date_status = {}
currency_status = {}
last_current_currency_message_time = {}


def currencies_are_allowed(user_id):
    try:
        if time.time() - last_current_currency_message_time[user_id] < 60:
            currency_is_allowed = False
            return currency_is_allowed

    except KeyError:
        last_current_currency_message_time.update({user_id: time.time() - 60})
        currency_is_allowed = True
        return currency_is_allowed

    currency_is_allowed = True
    return currency_is_allowed


@dp.message_handler(commands="start")
async def welcome(message: types.Message):
    user_ids.append(message.chat.id)
    user_exists = fetch_id_from_sql(user_id=message.from_user.id)

    if user_exists is None:
        users_first_language(user_id=message.chat.id)
    add_id_to_sql(user_id=message.from_user.id)

    states.update({message.chat.id: "start"})

    user_language = get_user_current_language(user_id=message.chat.id)

    random_greet_sticker = randint(1, 3)

    if random_greet_sticker == 1:
        await bot.send_animation(chat_id=message.chat.id, animation=animated_dictionary['UtyaDuck']['Greeting'])
    elif random_greet_sticker == 2:
        await bot.send_animation(chat_id=message.chat.id, animation=animated_dictionary['CherryBlack']['Greeting'])
    elif random_greet_sticker == 3:
        await bot.send_animation(chat_id=message.chat.id, animation=animated_dictionary['TonyStar']['Greeting'])

    await message.reply(text=f"""{languages[user_language]['start_command']} {message.from_user.full_name}.😀
{languages[user_language]['start_command_choose_button']}""",
                        reply_markup=bot_options_keyboard(user_language=user_language))


# @dp.message_handler(commands="broadcast", user_id="ADMIN_ID")
# async def send_to_all_users(message: types.Message):
#     users_ids = fetch_data_for_update_broadcast()[0]
#     text = fetch_data_for_update_broadcast()[1]
#
#     for user_id in users_ids:
#         await bot.send_message(chat_id=user_id[0], text=text, parse_mode='HTML')
#
#     await message.answer("Message sent to all users.")


@dp.message_handler(commands="help")
async def welcome(message: types.Message):
    try:
        user_language = get_user_current_language(user_id=message.chat.id)
    except:
        users_first_language(user_id=message.from_user.id)
        user_language = get_user_current_language(user_id=message.chat.id)

    await message.reply(text=languages[user_language]["help_command"])

    await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.UPLOAD_VIDEO)

    await bot.send_video(video=open('Assets/Videos/Tutorial/MainTutorial.mp4', 'rb'), chat_id=message.chat.id)


@dp.message_handler(commands="about")
async def welcome(message: types.Message):
    try:
        user_language = get_user_current_language(user_id=message.chat.id)
    except:
        users_first_language(user_id=message.from_user.id)
        user_language = get_user_current_language(user_id=message.chat.id)

    await message.reply(text=languages[user_language]["about_command"])


# To know the sticker info that the user sends to you.
@dp.message_handler(content_types=types.ContentType.STICKER)
async def handle_sticker(message: types.Message):
    if message.sticker.is_animated:
        sticker = message.sticker
        print(f"Sticker: {sticker}")


@dp.message_handler()
async def options_keyboard_answer(message: types.Message):
    global last_current_currency_message_time

    try:
        user_language = get_user_current_language(user_id=message.chat.id)
    except:
        users_first_language(user_id=message.from_user.id)
        user_language = get_user_current_language(user_id=message.chat.id)

    if message.text == languages[user_language]['BMI']:

        try:
            user_language = get_user_current_language(user_id=message.chat.id)
        except:
            users_first_language(user_id=message.from_user.id)
            user_language = get_user_current_language(user_id=message.chat.id)

        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['enter_weight_bmi'],
                               reply_markup=bmi__conversion_weight_inline_keyboard())
        states.update({message.chat.id: "bmi"})

    if message.text == languages[user_language]["date"]:

        try:
            user_language = get_user_current_language(user_id=message.chat.id)
        except:
            users_first_language(user_id=message.from_user.id)
            user_language = get_user_current_language(user_id=message.chat.id)

        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['date_option'],
                               reply_markup=date__options_keyboard(user_language=user_language))
        states.update({message.chat.id: "date"})

    if message.text == languages[user_language]['today']:
        current_time = current_time_getter()
        today_in_gregorian = gregorian_getter()
        today_in_jalali = jalali_getter()

        user_language = get_user_current_language(user_id=message.chat.id)

        await bot.send_message(text=f"""{languages[user_language]['current_time']} : <code> {current_time} </code>
{languages[user_language]['jalali_date']} : <code> {today_in_jalali} </code>
{languages[user_language]['gregorian_date']} : <code> {today_in_gregorian} </code>""", chat_id=message.chat.id,
                               parse_mode="HTML",
                               reply_markup=date_calender_inline_keyboard(user_language=user_language))

    if message.text == languages[user_language]["date_convert"]:
        await bot.send_message(text=languages[user_language]['choose_date_convert_option'], chat_id=message.chat.id,
                               reply_markup=date__date_conversion_options_inline_keyboard(user_language=user_language))

    if message.text == languages[user_language]['currency']:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""{languages[user_language]['currency_converter_select']}""",
                               reply_markup=currency_options_keyboard(user_language=user_language))
        states.update({message.chat.id: "currency"})

    if message.text == languages[user_language]['currency_conversion']:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""{languages[user_language]['currency_converter_enter_currency_amount']}""",
                               reply_markup=currency_conversion_numbers_inline_keyboard())

    if message.text == languages[user_language]["now_currency"]:
        user_language = get_user_current_language(user_id=message.chat.id)

        currency_is_allowed = currencies_are_allowed(user_id=message.from_user.id)
        if not currency_is_allowed:
            await message.answer(languages[user_language]['1_min_currency_limitation'])

        else:
            await bot.send_animation(chat_id=message.chat.id,
                                     animation=animated_dictionary['AnimatedEmojies']['Currency'])

            await bot.send_chat_action(chat_id=message.from_user.id, action=ChatActions.TYPING)

            answer = await momentarily_currency_rate(user_language=user_language)

            if answer[1]:
                await bot.send_message(chat_id=message.from_user.id, text=answer[0], parse_mode="HTML")
                await bot.send_animation(chat_id=message.chat.id,
                                         animation=animated_dictionary['HotCherry']['Shrugging'])
                await bot.send_message(chat_id=message.from_user.id,
                                       text=languages[user_language]['question_mark_count_exceeded_error'])

            else:
                await bot.send_message(chat_id=message.from_user.id, text=answer[0], parse_mode="HTML")
            last_current_currency_message_time.update({message.chat.id: time.time()})

    if message.text == languages[user_language]['calculation']:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""{languages[user_language]['calculation_option_selection']}""",
                               reply_markup=calculation__options_keyboard(user_language=user_language))
        states.update({message.chat.id: "calculation"})

    if message.text == languages[user_language]['calculator']:
        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['enter_phrase_calculator'],
                               reply_markup=calculator__inline_keyboard())
        states.update({message.chat.id: "calculator"})

    if message.text == languages[user_language]['unit_conversion']:
        await message.answer(text=f"{languages[user_language]['unit_conversion_option_selection']}",
                             reply_markup=unit_conversion_options_keyboard(user_language=user_language))
        states.update({message.chat.id: "unit_conversion"})

    if message.text == languages[user_language]['data']:
        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['data_converter_enter_number'],
                               reply_markup=data_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "data_converter"})

    if message.text == languages[user_language]['length']:
        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['length_converter_enter_number'],
                               reply_markup=length_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "length_converter"})

    if message.text == languages[user_language]['mass']:
        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['mass_converter_enter_number'],
                               reply_markup=mass_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "mass_converter"})

    if message.text == languages[user_language]['numeral']:
        await message.answer(text=languages[user_language]['numeral_converter_enter_number'],
                             reply_markup=numeral_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "numeral_converter"})

    if message.text == languages[user_language]['temperature']:
        await bot.send_message(chat_id=message.chat.id,
                               text=languages[user_language]['temperature_converter_enter_number'],
                               reply_markup=temperature_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "temperature_converter"})

    if message.text == languages[user_language]['time']:
        await bot.send_message(chat_id=message.chat.id, text=languages[user_language]['time_converter_enter_number'],
                               reply_markup=time_conversion_numbers_inline_keyboard())
        states.update({message.chat.id: "time_converter"})

    if message.text == languages[user_language]['settings_option_selection']:
        user_language = get_user_current_language(user_id=message.from_user.id)

        await bot.send_message(chat_id=message.chat.id,
                               text=f"{languages[user_language]['choose_setting_option']}",
                               reply_markup=settings__options_keyboard(user_language=user_language))
        states.update({message.chat.id: "settings"})

    if message.text == languages[user_language]['language_option_selection']:
        await bot.send_message(chat_id=message.chat.id,
                               text=languages[user_language]['choose_language'],
                               reply_markup=languages_inline_keyboard())
        states.update({message.chat.id: "select_language"})

    if message.text == languages[user_language]['back_option_selection']:
        try:
            user_state = states[message.from_user.id]
        except:
            states.update({message.from_user.id: "start"})
            user_state = states[message.from_user.id]

        if user_state == "start":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{languages[user_language]['start_command_choose_button']}",
                                   reply_markup=bot_options_keyboard(user_language=user_language))

        if user_state == "date":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{languages[user_language]['start_command_choose_button']}",
                                   reply_markup=bot_options_keyboard(user_language=user_language))

        if user_state == "currency":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{languages[user_language]['start_command_choose_button']}",
                                   reply_markup=bot_options_keyboard(user_language=user_language))

        if user_state == "calculation":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{languages[user_language]['start_command_choose_button']}",
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "calculator":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "calculation"})

        if user_state == "bmi":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "calculation"})

        if user_state == "unit_conversion":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{languages[user_language]['start_command_choose_button']}",
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "mass_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "data_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "length_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "time_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "numeral_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))

            states.update({message.chat.id: "start"})

        if user_state == "temperature_converter":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))
            states.update({message.chat.id: "start"})

        if user_state == "settings":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))
            states.update({message.chat.id: "start"})

        if user_state == "select_language":
            user_language = get_user_current_language(user_id=message.from_user.id)

            await bot.send_message(chat_id=message.chat.id,
                                   text=languages[user_language]['start_command_choose_button'],
                                   reply_markup=bot_options_keyboard(user_language=user_language))
            states.update({message.chat.id: "settings"})


@dp.callback_query_handler()
async def query_handler(call: types.CallbackQuery):
    global from_base, to_base, weight_unit, height_unit, first_symbol, number, numeral_data, bmi_status, data_status, temp_flag
    global weight, height
    global phrase, numeral_system_flag

    chat_id = call.from_user.id
    message_id = call.message.message_id
    message = call.data

    if message in bmi_conversion_weight_callback_data_list:
        text = call.message.text

        if "weight" in text or "وزن" in text:
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
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['enter_weight_bmi']

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())

        if message == "backward_weight_bmi":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['enter_weight_bmi']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_weight_inline_keyboard())

        if message == "done_weight_bmi":
            weight = call.message.text

            if "weight" not in weight or "قد" not in height:
                bmi_status.update(
                    {call.from_user.id: {"weight": weight, "message_id": call.message.message_id}})

                user_language = get_user_current_language(user_id=call.from_user.id)

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=languages[user_language]['enter_height_bmi'],
                                            reply_markup=bmi__conversion_height_inline_keyboard())

    if message in bmi_conversion_height_callback_data_list:
        text = call.message.text

        if "height" in text or "قد" in text:
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

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['enter_height_bmi']

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())

        if message == "clear_height_bmi":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['enter_height_bmi']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=bmi__conversion_height_inline_keyboard())

        if message == "done_height_bmi":

            height = call.message.text
            if "height" not in height or "قد" not in height:
                bmi_status.update(
                    {call.from_user.id: {"weight": bmi_status[call.from_user.id]["weight"], "height": height,
                                         "message_id": bmi_status[call.from_user.id]["message_id"]}})

            try:
                for chat_id, weight_and_height_and_message_id in bmi_status.items():
                    try:
                        if len(bmi_status[call.from_user.id]) == 3:
                            user_language = get_user_current_language(user_id=chat_id)

                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['weight']} : {weight_and_height_and_message_id["weight"]} kg
{languages[user_language]['height']} : {weight_and_height_and_message_id["height"]} cm

{languages[user_language]['BMI']} : <code>{bmi_calculator(weight=float(weight_and_height_and_message_id["weight"]), height=float(weight_and_height_and_message_id["height"]), user_id=chat_id)[0]}</code>

{languages[user_language]['BMI_status']} : {bmi_calculator(weight=float(weight_and_height_and_message_id["weight"]), height=float(weight_and_height_and_message_id["height"]), user_id=chat_id)[1]}""",
                                chat_id=chat_id, message_id=weight_and_height_and_message_id["message_id"],
                                reply_markup=bmi__conversion_see_bmi_chart_inline_keyboard(user_language=user_language),
                                parse_mode="HTML")

                            bmi_status.pop(chat_id)
                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in bmi__conversion_see_bmi_chart_callback_data_list:
        if message == "see_chart_bmi":
            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.send_animation(chat_id=call.from_user.id,
                                     animation=animated_dictionary['AnimatedEmojies']['Chart'])

            await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_PHOTO)

            await bot.send_photo(photo=open('Assets/Images/BMI/BMIChart.jpg', 'rb'), chat_id=chat_id,
                                 caption=languages[user_language]['bmi_chart'])

    if message in calculator_callback_data_list:

        text = call.message.text

        if "phrase" in text or "عبارت" in text:
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
                if text[-1].isdigit():
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
            elif text[0].isdigit():
                text = f"-{text}"
            elif text[0] == "+":
                text = f"-{text}"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "backward_calculator":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['enter_phrase_calculator']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "clear_calculator":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['enter_phrase_calculator']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=calculator__inline_keyboard())

        if message == "done_calculator":
            data_to_be_calculate = call.message.text

            await bot.edit_message_text(
                text=f"""{data_to_be_calculate} = <code>{calculator(data_to_be_calculate, user_id=call.from_user.id)}</code>""",
                chat_id=chat_id, message_id=message_id, parse_mode="HTML")

    if message in currency_callback_date_list:
        text = call.message.text

        if "currency" in text or "پول" in text:
            text = ""

        if message == "0_currency_converter":
            text += "0"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "1_currency_converter":
            text += "1"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "2_currency_converter":
            text += "2"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "3_currency_converter":
            text += "3"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "4_currency_converter":
            text += "4"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "5_currency_converter":
            text += "5"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "6_currency_converter":
            text += "6"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "7_currency_converter":
            text += "7"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "8_currency_converter":
            text += "8"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "9_currency_converter":
            text += "9"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "dot_currency_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "clear_currency_converter":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['currency_converter_enter_currency_amount']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "backward_currency_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['currency_converter_enter_currency_amount']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=currency_conversion_numbers_inline_keyboard())

        if message == "done_currency_converter":
            amount = text
            currency_status.update({call.from_user.id: {"amount": amount, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['currency_converter_start'],
                                        reply_markup=currency_conversion_starter_inline_keyboard(
                                            user_language=user_language))

        if message == "dollar_currency_conversion_starter":
            source_currency = "USD"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "tooman_currency_conversion_starter":
            source_currency = "IRR"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "euro_currency_conversion_starter":
            source_currency = "EUR"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "pound_currency_conversion_starter":
            source_currency = "GBP"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "swiss_franc_currency_conversion_starter":
            source_currency = "CHF"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "lir_currency_conversion_starter":
            source_currency = "LIR"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        if message == "dirham_currency_conversion_starter":
            source_currency = "AED"
            currency_status.update(
                {call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
                                     "source_currency": source_currency,
                                     "message_id": currency_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(text=languages[user_language]['currency_converter_destination'],
                                        chat_id=chat_id, message_id=message_id,
                                        reply_markup=currency_conversion_destination_inline_keyboard(
                                            user_language=user_language))

        # if message == "dollar_currency_conversion_destination":
        #     target_currency = "USD"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "tooman_currency_conversion_destination":
        #     target_currency = "IRR"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "euro_currency_conversion_destination":
        #     target_currency = "EUR"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "pound_currency_conversion_destination":
        #     target_currency = "GBP"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "swiss_franc_currency_conversion_destination":
        #     target_currency = "CHF"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "lir_currency_conversion_destination":
        #     target_currency = "LIR"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass
        #
        # if message == "dirham_currency_conversion_destination":
        #     target_currency = "AED"
        #     currency_status.update({call.from_user.id: {"amount": currency_status[call.from_user.id]["amount"],
        #                                                 "source_currency": currency_status[call.from_user.id][
        #                                                     "source_currency"],
        #                                                 "target_currency": target_currency,
        #                                                 "message_id": call.message.message_id}})
        #     try:
        #         for chat_id, amount_and_source_currency_and_target_currency_and_message_id in currency_status.items():
        #             amount = amount_and_source_currency_and_target_currency_and_message_id['amount']
        #             source_currency = amount_and_source_currency_and_target_currency_and_message_id['source_currency']
        #             target_currency = amount_and_source_currency_and_target_currency_and_message_id['target_currency']
        #
        #             answer = currency_converter(amount=amount, source_currency=source_currency,
        #                                         target_currency=target_currency)
        #             await bot.edit_message_text(
        #                 text=answer,
        #                 chat_id=chat_id,
        #                 message_id=amount_and_source_currency_and_target_currency_and_message_id["message_id"],
        #                 parse_mode="HTML")
        #
        #             currency_status.pop(chat_id)
        #     except RuntimeError:
        #         pass

    if message in date_conversion_callback_date_list:
        text = call.message.text

        if "day" in text or "روز" in text:
            text = ""

        if "month" in text or "ماه" in text:
            text = ""

        if "year" in text or "سال" in text:
            text = ""

        def is_all_zeroes(s):
            for c in s:
                if c != "0":
                    return False
            return True

        if message == "jalali_to_gregorian":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]["enter_day"]
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

            date_status.update({call.from_user.id: {"date_conversion_type": "jalali_to_gregorian",
                                                    "message_id": call.message.message_id}})

        if message == "gregorian_to_jalali":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]["enter_day"]
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

            date_status.update({call.from_user.id: {"date_conversion_type": "gregorian_to_jalali",
                                                    "message_id": call.message.message_id}})

        if message == "0_date_conversion_day":
            text += "0"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "1_date_conversion_day":
            text += "1"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "2_date_conversion_day":
            text += "2"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "3_date_conversion_day":
            text += "3"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "4_date_conversion_day":
            text += "4"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "5_date_conversion_day":
            text += "5"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "6_date_conversion_day":
            text += "6"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "7_date_conversion_day":
            text += "7"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "8_date_conversion_day":
            text += "8"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "9_date_conversion_day":
            text += "9"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "backward_date_conversion_day":
            text = text[:-1]
            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]["enter_day"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "clear_date_conversion_day":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]["enter_day"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_day_numbers_inline_keyboard())

        if message == "done_date_conversion_day":
            day = call.message.text

            user_language = get_user_current_language(user_id=call.from_user.id)

            if len(day) > 2:
                await bot.edit_message_text(text=languages[user_language]["date_conversion_day_max_2_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_day_numbers_inline_keyboard())

            elif int(day) > 31:
                await bot.edit_message_text(text=languages[user_language]["date_conversion_day_max_31_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_day_numbers_inline_keyboard())

            elif is_all_zeroes(day):
                await bot.edit_message_text(text=languages[user_language]["date_conversion_day_value_0_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_day_numbers_inline_keyboard())
            else:
                if len(day) == 1:
                    day = f"0{day}"

                date_status.update(
                    {call.from_user.id: {"date_conversion_type": date_status[call.from_user.id]["date_conversion_type"],
                                         "day": day, "message_id": call.message.message_id}})

                user_language = get_user_current_language(user_id=call.from_user.id)

                await bot.edit_message_text(text=languages[user_language]["enter_month"], chat_id=chat_id,
                                            message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "0_date_conversion_month":
            text += "0"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "1_date_conversion_month":
            text += "1"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "2_date_conversion_month":
            text += "2"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "3_date_conversion_month":
            text += "3"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "4_date_conversion_month":
            text += "4"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "5_date_conversion_month":
            text += "5"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "6_date_conversion_month":
            text += "6"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "7_date_conversion_month":
            text += "7"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "8_date_conversion_month":
            text += "8"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "9_date_conversion_month":
            text += "9"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "backward_date_conversion_month":
            text = text[:-1]
            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]["enter_month"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "clear_date_conversion_month":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]["enter_month"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_month_numbers_inline_keyboard())

        if message == "done_date_conversion_month":
            month = call.message.text

            user_language = get_user_current_language(user_id=call.from_user.id)

            if len(month) > 2:
                await bot.edit_message_text(text=languages[user_language]["date_conversion_month_max_2_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_month_numbers_inline_keyboard())

            elif int(month) > 12:
                await bot.edit_message_text(text=languages[user_language]["date_conversion_month_max_12_error"],
                                            chat_id=chat_id,
                                            message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_month_numbers_inline_keyboard())

            elif is_all_zeroes(month):
                await bot.edit_message_text(text=languages[user_language]["date_conversion_month_value_0_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_month_numbers_inline_keyboard())

            else:
                if len(month) == 1:
                    month = f"0{month}"

                date_status.update(
                    {call.from_user.id: {"date_conversion_type": date_status[call.from_user.id]["date_conversion_type"],
                                         "day": date_status[call.from_user.id]["day"], "month": month,
                                         "message_id": call.message.message_id}})

                user_language = get_user_current_language(user_id=call.from_user.id)

                await bot.edit_message_text(text=languages[user_language]["enter_year"], chat_id=chat_id,
                                            message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "0_date_conversion_year":
            text += "0"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "1_date_conversion_year":
            text += "1"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "2_date_conversion_year":
            text += "2"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "3_date_conversion_year":
            text += "3"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "4_date_conversion_year":
            text += "4"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "5_date_conversion_year":
            text += "5"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "6_date_conversion_year":
            text += "6"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "7_date_conversion_year":
            text += "7"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "8_date_conversion_year":
            text += "8"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "9_date_conversion_year":
            text += "9"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "backward_date_conversion_year":
            text = text[:-1]
            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]["enter_year"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "clear_date_conversion_year":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]["enter_year"]

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=date__date_conversion_year_numbers_inline_keyboard())

        if message == "done_date_conversion_year":
            year = call.message.text

            user_language = get_user_current_language(user_id=call.from_user.id)

            if len(year) == 1:
                year = f"000{year}"

            if len(year) == 2:
                year = f"00{year}"

            if len(year) == 3:
                year = f"0{year}"

            if len(year) > 4:
                await bot.edit_message_text(text=languages[user_language]["date_conversion_year_max_4_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_year_numbers_inline_keyboard())

            elif int(year) < 622 and date_status[call.from_user.id]["date_conversion_type"] == "gregorian_to_jalali":
                await bot.edit_message_text(text=languages[user_language]["date_conversion_year_min_622_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_year_numbers_inline_keyboard())

            elif is_all_zeroes(year):
                await bot.edit_message_text(text=languages[user_language]["date_conversion_year_value_0_error"],
                                            chat_id=chat_id, message_id=call.message.message_id,
                                            reply_markup=date__date_conversion_year_numbers_inline_keyboard())

            else:
                date_status.update(
                    {call.from_user.id: {"date_conversion_type": date_status[call.from_user.id]["date_conversion_type"],
                                         "day": date_status[call.from_user.id]["day"],
                                         "month": date_status[call.from_user.id]["month"], "year": year,
                                         "message_id": call.message.message_id}})

                user_language = get_user_current_language(user_id=call.from_user.id)

                try:
                    for chat_id, date_conversion_type_and_day_and_month_and_year_and_message_id in date_status.items():
                        if len(date_status[chat_id]) == 5:
                            if date_conversion_type_and_day_and_month_and_year_and_message_id[
                                "date_conversion_type"] == "jalali_to_gregorian":
                                jalali_date = f'{date_conversion_type_and_day_and_month_and_year_and_message_id["year"]}/{date_conversion_type_and_day_and_month_and_year_and_message_id["month"]}/{date_conversion_type_and_day_and_month_and_year_and_message_id["day"]}'
                                gregorian_date = jalali_to_gregorian(jalali_date)

                                await bot.edit_message_text(
                                    text=f"""{languages[user_language]['jalali_date']} : <code> {jalali_date} </code>
{languages[user_language]['gregorian_date']} : <code> {gregorian_date} </code>""", chat_id=chat_id,
                                    message_id=date_conversion_type_and_day_and_month_and_year_and_message_id[
                                        "message_id"],
                                    parse_mode="HTML")

                            if date_conversion_type_and_day_and_month_and_year_and_message_id[
                                "date_conversion_type"] == "gregorian_to_jalali":
                                gregorian_date = f'{date_conversion_type_and_day_and_month_and_year_and_message_id["year"]}/{date_conversion_type_and_day_and_month_and_year_and_message_id["month"]}/{date_conversion_type_and_day_and_month_and_year_and_message_id["day"]}'
                                jalali_date = gregorian_to_jalali(gregorian_date)

                                await bot.edit_message_text(
                                    text=f"""{languages[user_language]['gregorian_date']} : <code> {gregorian_date} </code>
{languages[user_language]['jalali_date']} : <code> {jalali_date} </code>""", chat_id=chat_id,
                                    message_id=date_conversion_type_and_day_and_month_and_year_and_message_id[
                                        "message_id"],
                                    parse_mode="HTML")

                            date_status.pop(chat_id)

                except RuntimeError:
                    pass

    if message in date__calender_callback_data_list:
        user_language = get_user_current_language(user_id=call.from_user.id)

        await bot.send_animation(chat_id=call.from_user.id,
                                 animation=animated_dictionary['AnimatedEmojies']['Calender'])

        await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_DOCUMENT)

        if message == "jalali_calender":
            await bot.send_document(document=open('Assets/Documents/Date/JalaliCalender.pdf', 'rb'), chat_id=chat_id,
                                    caption=languages[user_language]['jalali_calender'])

        if message == "gregorian_calender":
            await bot.send_document(document=open('Assets/Documents/Date/GregorianCalender.pdf', 'rb'), chat_id=chat_id,
                                    caption=languages[user_language]['gregorian_calender'])

    if message in data_conversion_callback_data_list:
        text = call.message.text

        if "data" in text or "داده" in text:
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
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['data_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "backward_data_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['data_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=data_conversion_numbers_inline_keyboard())

        if message == "done_data_converter":
            number = text
            data_status.update({call.from_user.id: {"number": number, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['data_converter_start'],
                                        reply_markup=data_conversion_starter_inline_keyboard(
                                            user_language=get_user_current_language(user_id=call.from_user.id)))

        if message == "bit_data_conversion_starter":
            first_symbol = "b"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "byte_data_conversion_starter":
            first_symbol = "B"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "kilo_byte_data_conversion_starter":
            first_symbol = "KB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "mega_byte_data_conversion_starter":
            first_symbol = "MB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "giga_byte_data_conversion_starter":
            first_symbol = "GB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "tera_byte_data_conversion_starter":
            first_symbol = "TB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "peta_byte_data_conversion_starter":
            first_symbol = "PB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "exa_byte_data_conversion_starter":
            first_symbol = "EB"
            data_status.update(
                {call.from_user.id: {"number": data_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": data_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['data_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=data_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "bit_data_conversion_destination":
            second_symbol = "b"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "byte_data_conversion_destination":
            second_symbol = "B"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "kilo_byte_data_conversion_destination":
            second_symbol = "KB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "mega_byte_data_conversion_destination":
            second_symbol = "MB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "giga_byte_data_conversion_destination":
            second_symbol = "GB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "tera_byte_data_conversion_destination":
            second_symbol = "TB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "peta_byte_data_conversion_destination":
            second_symbol = "PB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "exa_byte_data_conversion_destination":
            second_symbol = "EB"
            data_status.update({call.from_user.id: {"number": data_status[call.from_user.id]["number"],
                                                    "first_symbol": data_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in data_status.items():
                    try:
                        if len(data_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{data_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            data_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in length_conversion_callback_data_list:
        text = call.message.text

        if "length" in text or "طول" in text:
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
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['length_converter_enter_number']

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "backward_length_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['length_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=length_conversion_numbers_inline_keyboard())

        if message == "done_length_converter":
            number = text
            length_status.update({call.from_user.id: {"number": number, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['length_converter_start']
                                        , reply_markup=length_conversion_starter_inline_keyboard(
                    user_language=user_language))

        if message == "pico_meter_length_conversion_starter":
            first_symbol = "pm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "nano_meter_length_conversion_starter":
            first_symbol = "nm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "micro_meter_length_conversion_starter":
            first_symbol = "μm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "milli_meter_length_conversion_starter":
            first_symbol = "mm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "centi_meter_length_conversion_starter":
            first_symbol = "cm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "desi_meter_length_conversion_starter":
            first_symbol = "dm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "meter_length_conversion_starter":
            first_symbol = "m"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "kilo_meter_length_conversion_starter":
            first_symbol = "Km"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "mile_length_conversion_starter":
            first_symbol = "mi"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "nautical_mile_length_conversion_starter":
            first_symbol = "nmi"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "foot_length_conversion_starter":
            first_symbol = "ft"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "inch_length_conversion_starter":
            first_symbol = "in"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "yard_length_conversion_starter":
            first_symbol = "yd"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "fathom_length_conversion_starter":
            first_symbol = "ftm"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "light_year_length_conversion_starter":
            first_symbol = "ly"
            length_status.update(
                {call.from_user.id: {"number": length_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": length_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['length_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=length_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "pico_meter_length_conversion_destination":
            second_symbol = "pm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "nano_meter_length_conversion_destination":
            second_symbol = "nm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "micro_meter_length_conversion_destination":
            second_symbol = "μm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "milli_meter_length_conversion_destination":
            second_symbol = "mm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "centi_meter_length_conversion_destination":
            second_symbol = "cm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "desi_meter_length_conversion_destination":
            second_symbol = "dm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "meter_length_conversion_destination":
            second_symbol = "m"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "kilo_meter_length_conversion_destination":
            second_symbol = "Km"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "mile_length_conversion_destination":
            second_symbol = "mi"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "nautical_mile_length_conversion_destination":
            second_symbol = "nmi"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "foot_length_conversion_destination":
            second_symbol = "ft"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "inch_length_conversion_destination":
            second_symbol = "in"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "yard_length_conversion_destination":
            second_symbol = "yd"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "fathom_length_conversion_destination":
            second_symbol = "ftm"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "light_year_length_conversion_destination":
            second_symbol = "ly"
            length_status.update({call.from_user.id: {"number": length_status[call.from_user.id]["number"],
                                                      "first_symbol": length_status[call.from_user.id]["first_symbol"],
                                                      "second_symbol": second_symbol,
                                                      "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in length_status.items():
                    try:
                        if len(length_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{length_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            length_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in mass_conversion_callback_data_list:
        text = call.message.text

        if "mass" in text or "جرم" in text:
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
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['mass_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "backward_mass_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['mass_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=mass_conversion_numbers_inline_keyboard())

        if message == "done_mass_converter":
            number = text
            mass_status.update({call.from_user.id: {"number": number, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['mass_converter_start'],
                                        reply_markup=mass_conversion_starter_inline_keyboard(
                                            user_language=user_language))

        if message == "nano_gram_mass_conversion_starter":
            first_symbol = "ng"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "micro_gram_mass_conversion_starter":
            first_symbol = "μg"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "quintal_mass_conversion_starter":
            first_symbol = "q"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "milli_gram_mass_conversion_starter":
            first_symbol = "mg"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))
        if message == "centi_gram_mass_conversion_starter":
            first_symbol = "cg"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "desi_gram_mass_conversion_starter":
            first_symbol = "dg"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "gram_mass_conversion_starter":
            first_symbol = "g"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "kilo_gram_mass_conversion_starter":
            first_symbol = "Kg"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "tone_mass_conversion_starter":
            first_symbol = "t"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "pound_mass_conversion_starter":
            first_symbol = "lb"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "ounce_mass_conversion_starter":
            first_symbol = "oz"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "carat_mass_conversion_starter":
            first_symbol = "ct"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "grain_mass_conversion_starter":
            first_symbol = "gr"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "long_ton_mass_conversion_starter":
            first_symbol = "l.t"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "short_ton_mass_conversion_starter":
            first_symbol = "sh.t"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "stone_mass_conversion_starter":
            first_symbol = "st"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "dram_mass_conversion_starter":
            first_symbol = "dr"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "sir_mass_conversion_starter":
            first_symbol = "sir"
            mass_status.update(
                {call.from_user.id: {"number": mass_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": mass_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['mass_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=mass_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "nano_gram_mass_conversion_destination":
            second_symbol = "ng"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "micro_gram_mass_conversion_destination":
            second_symbol = "μg"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "quintal_mass_conversion_destination":
            second_symbol = "q"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "milli_gram_mass_conversion_destination":
            second_symbol = "mg"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "centi_gram_mass_conversion_destination":
            second_symbol = "cg"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "desi_gram_mass_conversion_destination":
            second_symbol = "dg"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "gram_mass_conversion_destination":
            second_symbol = "g"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "kilo_gram_mass_conversion_destination":
            second_symbol = "Kg"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "tone_mass_conversion_destination":
            second_symbol = "t"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "pound_mass_conversion_destination":
            second_symbol = "lb"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "ounce_mass_conversion_destination":
            second_symbol = "oz"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "carat_mass_conversion_destination":
            second_symbol = "ct"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "grain_mass_conversion_destination":
            second_symbol = "gr"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "long_ton_mass_conversion_destination":
            second_symbol = "l.t"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "short_ton_mass_conversion_destination":
            second_symbol = "sh.t"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "stone_mass_conversion_destination":
            second_symbol = "st"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "dram_mass_conversion_destination":
            second_symbol = "dr"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "dan_mass_conversion_destination":
            second_symbol = "dan"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "sir_mass_conversion_destination":
            second_symbol = "sir"
            mass_status.update({call.from_user.id: {"number": mass_status[call.from_user.id]["number"],
                                                    "first_symbol": mass_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in mass_status.items():
                    try:
                        if len(mass_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{mass_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            mass_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in numeral_conversion_callback_data_list:
        phrase = call.message.text

        if "numeral" in phrase or "مبنا" in phrase:
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
            if "." not in phrase:
                phrase += "."
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "clear_numeral_converter":
            user_language = get_user_current_language(user_id=call.from_user.id)

            phrase = languages[user_language]['numeral_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=phrase,
                                        reply_markup=numeral_conversion_numbers_inline_keyboard())

        if message == "backward_numeral_converter":
            phrase = phrase[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if phrase == "":
                phrase = languages[user_language]['numeral_converter_enter_number']

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
            numeral_status.update({call.from_user.id: {"data": numeral_data, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_from_base'],
                                        reply_markup=numeral_conversion_from_base_inline_keyboard())

        if message == "2_from_base":
            from_base = "2"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "3_from_base":
            from_base = "3"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})
            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "4_from_base":
            from_base = "4"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "5_from_base":
            from_base = "5"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "6_from_base":
            from_base = "6"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "7_from_base":
            from_base = "7"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "8_from_base":
            from_base = "8"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "9_from_base":
            from_base = "9"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "10_from_base":
            from_base = "10"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "11_from_base":
            from_base = "11"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "12_from_base":
            from_base = "12"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "13_from_base":
            from_base = "13"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "14_from_base":
            from_base = "14"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "15_from_base":
            from_base = "15"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "16_from_base":
            from_base = "16"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "17_from_base":
            from_base = "17"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "18_from_base":
            from_base = "18"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "19_from_base":
            from_base = "19"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "20_from_base":
            from_base = "20"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "21_from_base":
            from_base = "21"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "22_from_base":
            from_base = "22"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "23_from_base":
            from_base = "23"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "24_from_base":
            from_base = "24"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "25_from_base":
            from_base = "25"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "26_from_base":
            from_base = "26"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "27_from_base":
            from_base = "27"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "28_from_base":
            from_base = "28"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "29_from_base":
            from_base = "29"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "30_from_base":
            from_base = "30"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "31_from_base":
            from_base = "31"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "32_from_base":
            from_base = "32"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "33_from_base":
            from_base = "33"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "34_from_base":
            from_base = "34"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "35_from_base":
            from_base = "35"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "36_from_base":
            from_base = "36"
            numeral_status.update(
                {call.from_user.id: {"data": numeral_status[call.from_user.id]["data"], "from_base": from_base,
                                     "message_id": numeral_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['numeral_converter_to_base'],
                                        reply_markup=numeral_conversion_to_base_inline_keyboard())

        if message == "2_to_base":
            to_base = "2"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "3_to_base":
            to_base = "3"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "4_to_base":
            to_base = "4"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "5_to_base":
            to_base = "5"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "6_to_base":
            to_base = "6"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "7_to_base":
            to_base = "7"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "8_to_base":
            to_base = "8"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "9_to_base":
            to_base = "9"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "10_to_base":
            to_base = "10"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "11_to_base":
            to_base = "11"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "12_to_base":
            to_base = "12"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "13_to_base":
            to_base = "13"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "14_to_base":
            to_base = "14"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "15_to_base":
            to_base = "15"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "16_to_base":
            to_base = "16"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "17_to_base":
            to_base = "17"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "18_to_base":
            to_base = "18"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "19_to_base":
            to_base = "19"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "20_to_base":
            to_base = "20"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "21_to_base":
            to_base = "21"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "22_to_base":
            to_base = "22"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "23_to_base":
            to_base = "23"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "24_to_base":
            to_base = "24"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "25_to_base":
            to_base = "25"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "26_to_base":
            to_base = "26"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "27_to_base":
            to_base = "27"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "28_to_base":
            to_base = "28"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "29_to_base":
            to_base = "29"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "30_to_base":
            to_base = "30"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "31_to_base":
            to_base = "31"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "32_to_base":
            to_base = "32"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "33_to_base":
            to_base = "33"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "34_to_base":
            to_base = "34"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "35_to_base":
            to_base = "35"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
{languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
{languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}

{languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "36_to_base":
            to_base = "36"
            numeral_status.update({call.from_user.id: {"data": numeral_status[call.from_user.id]["data"],
                                                       "from_base": numeral_status[call.from_user.id]["from_base"],
                                                       "to_base": to_base,
                                                       "message_id": call.message.message_id}})

            try:
                for chat_id, data_and_from_base_and_to_base_and_message_id in numeral_status.items():
                    try:
                        if len(numeral_status[call.from_user.id]) == 4:
                            user_language = get_user_current_language(user_id=chat_id)
                            await bot.edit_message_text(
                                text=f"""{languages[user_language]['phrase']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[1]}
            {languages[user_language]['from_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[2]}
            {languages[user_language]['to_base']} : {numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[3]}
            {languages[user_language]['answer']} : <code>{numeral_converter(from_base=data_and_from_base_and_to_base_and_message_id["from_base"], to_base=data_and_from_base_and_to_base_and_message_id["to_base"], data=data_and_from_base_and_to_base_and_message_id["data"])[0]}</code>""",
                                chat_id=chat_id, message_id=data_and_from_base_and_to_base_and_message_id["message_id"],
                                parse_mode="HTML")

                            numeral_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in temperature_conversion_callback_data_list:
        text = call.message.text

        if "temperature" in text or "دما" in text:
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

        if message == "neg_or_pos_maker_temperature_converter":

            user_language = get_user_current_language(user_id=call.from_user.id)
            text = call.message.text

            if text != "":
                temp_flag = False
                if text[0].isdigit():
                    text = f"-{text}"
                elif text[0] == "-":
                    text = text[1:]

                    if text == "":
                        text = languages[user_language]['temperature_converter_enter_number']
                        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                                    reply_markup=temperature_conversion_numbers_inline_keyboard())
                        temp_flag = True

            if text == languages[user_language]['temperature_converter_enter_number']:
                if not temp_flag:
                    text = "-"

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "dot_temperature_converter":
            if "." not in text:
                text += "."
                await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                            reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "clear_temperature_converter":
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['temperature_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "backward_temperature_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['temperature_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=temperature_conversion_numbers_inline_keyboard())

        if message == "done_temperature_converter":
            number = text

            user_language = get_user_current_language(user_id=call.from_user.id)

            temperature_status.update({call.from_user.id: {"number": number, "message_id": call.message.message_id}})

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['temperature_converter_start'],
                                        reply_markup=temperature_conversion_starter_inline_keyboard(
                                            user_language=user_language))

        if message == "celsius_temperature_conversion_starter":
            first_symbol = "C°"
            temperature_status.update(
                {call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                     "first_symbol": first_symbol,
                                     "message_id": temperature_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['temperature_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=temperature_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "fahrenheit_temperature_conversion_starter":
            first_symbol = "F°"
            temperature_status.update(
                {call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                     "first_symbol": first_symbol,
                                     "message_id": temperature_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['temperature_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=temperature_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "kelvin_temperature_conversion_starter":
            first_symbol = "K"
            temperature_status.update(
                {call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                     "first_symbol": first_symbol,
                                     "message_id": temperature_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['temperature_converter_destination'],
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=temperature_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "celsius_temperature_conversion_destination":
            second_symbol = "C°"
            temperature_status.update({call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                                           "first_symbol": temperature_status[call.from_user.id][
                                                               "first_symbol"],
                                                           "second_symbol": second_symbol,
                                                           "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in temperature_status.items():
                    try:
                        if len(temperature_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{temperature_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            temperature_status.pop(chat_id)

                    except KeyError:
                        pass
            except KeyError:
                pass

        if message == "fahrenheit_temperature_conversion_destination":
            second_symbol = "F°"
            temperature_status.update({call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                                           "first_symbol": temperature_status[call.from_user.id][
                                                               "first_symbol"],
                                                           "second_symbol": second_symbol,
                                                           "message_id": call.message.message_id}})
            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in temperature_status.items():
                    try:
                        if len(temperature_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{temperature_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            temperature_status.pop(chat_id)

                    except KeyError:
                        pass
            except KeyError:
                pass

        if message == "kelvin_temperature_conversion_destination":
            second_symbol = "K"
            temperature_status.update({call.from_user.id: {"number": temperature_status[call.from_user.id]["number"],
                                                           "first_symbol": temperature_status[call.from_user.id][
                                                               "first_symbol"],
                                                           "second_symbol": second_symbol,
                                                           "message_id": call.message.message_id}})

        try:
            for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in temperature_status.items():
                try:
                    if len(temperature_status[call.from_user.id]) == 4:
                        await bot.edit_message_text(
                            text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{temperature_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                            chat_id=chat_id,
                            message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                            parse_mode="HTML")

                        temperature_status.pop(chat_id)

                except KeyError:
                    pass
        except KeyError:
            pass

    if message in time_conversion_callback_data_list:
        text = call.message.text

        if "time" in text or "زمان" in text:
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
            user_language = get_user_current_language(user_id=call.from_user.id)

            text = languages[user_language]['time_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "backward_time_converter":
            text = text[:-1]

            user_language = get_user_current_language(user_id=call.from_user.id)

            if text == "":
                text = languages[user_language]['time_converter_enter_number']
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text,
                                        reply_markup=time_conversion_numbers_inline_keyboard())

        if message == "done_time_converter":
            number = text
            time_status.update({call.from_user.id: {"number": number, "message_id": call.message.message_id}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=languages[user_language]['time_converter_start'],
                                        reply_markup=time_conversion_starter_inline_keyboard(
                                            user_language=user_language))

        if message == "pico_second_time_conversion_starter":
            first_symbol = "ps"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "nano_second_time_conversion_starter":
            first_symbol = "ns"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "micro_second_time_conversion_starter":
            first_symbol = "μs"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "milli_second_time_conversion_starter":
            first_symbol = "ms"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "second_time_conversion_starter":
            first_symbol = "s"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "min_time_conversion_starter":
            first_symbol = "min"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "hour_time_conversion_starter":
            first_symbol = "h"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "day_time_conversion_starter":
            first_symbol = "d"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "month_time_conversion_starter":
            first_symbol = "mo"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "year_time_conversion_starter":
            first_symbol = "y"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "decade_time_conversion_starter":
            first_symbol = "dec"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "century_time_conversion_starter":
            first_symbol = "cent"
            time_status.update(
                {call.from_user.id: {"number": time_status[call.from_user.id]["number"], "first_symbol": first_symbol,
                                     "message_id": time_status[call.from_user.id]["message_id"]}})

            user_language = get_user_current_language(user_id=call.from_user.id)

            await bot.edit_message_text(
                text=languages[user_language]['time_converter_destination'], chat_id=chat_id,
                message_id=message_id,
                reply_markup=time_conversion_destination_inline_keyboard(user_language=user_language))

        if message == "pico_second_time_conversion_destination":
            second_symbol = "ps"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "nano_second_time_conversion_destination":
            second_symbol = "ns"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "micro_second_time_conversion_destination":
            second_symbol = "μs"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "milli_second_time_conversion_destination":
            second_symbol = "ms"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "second_time_conversion_destination":
            second_symbol = "s"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "min_time_conversion_destination":
            second_symbol = "min"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "hour_time_conversion_destination":
            second_symbol = "h"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "day_time_conversion_destination":
            second_symbol = "d"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "month_time_conversion_destination":
            second_symbol = "mo"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "year_time_conversion_destination":
            second_symbol = "y"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "decade_time_conversion_destination":
            second_symbol = "dec"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

        if message == "century_time_conversion_destination":
            second_symbol = "cent"
            time_status.update({call.from_user.id: {"number": time_status[call.from_user.id]["number"],
                                                    "first_symbol": time_status[call.from_user.id]["first_symbol"],
                                                    "second_symbol": second_symbol,
                                                    "message_id": call.message.message_id}})

            try:
                for chat_id, number_and_first_symbol_and_last_symbol_and_message_id in time_status.items():
                    try:
                        if len(time_status[call.from_user.id]) == 4:
                            await bot.edit_message_text(
                                text=f"""{number_and_first_symbol_and_last_symbol_and_message_id["number"]} {number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"]} = <code>{time_converter(first_symbol=number_and_first_symbol_and_last_symbol_and_message_id["first_symbol"], second_symbol=number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"], number=number_and_first_symbol_and_last_symbol_and_message_id["number"])} {number_and_first_symbol_and_last_symbol_and_message_id["second_symbol"]}</code>""",
                                chat_id=chat_id,
                                message_id=number_and_first_symbol_and_last_symbol_and_message_id["message_id"],
                                parse_mode="HTML")

                            time_status.pop(chat_id)

                    except KeyError:
                        pass
            except RuntimeError:
                pass

    if message in languages_callback_data_list:
        user_language_update(user_id=call.from_user.id, language=call.data)
        text = languages[message]["successful_language_change"]

        user_language = get_user_current_language(user_id=call.from_user.id)

        await bot.send_message(text=text,
                               chat_id=chat_id, reply_markup=settings__options_keyboard(user_language=user_language))

        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


executor.start_polling(dp, skip_updates=True)
