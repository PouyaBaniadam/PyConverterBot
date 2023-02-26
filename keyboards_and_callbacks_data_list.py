from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import unicodedata
from Settings.languages.languages_dictionary import languages


def bot_options_keyboard(user_language):
    bot__unit_conversion_option_button = KeyboardButton(languages[user_language]["unit_conversion"])
    bot__calculation_option_button = KeyboardButton(languages[user_language]["calculation"])
    bot__date_option_button = KeyboardButton(languages[user_language]["date"])
    bot__currency_option_button = KeyboardButton(languages[user_language]["currency"])
    bot__settings_option_button = KeyboardButton(languages[user_language]["settings_option_selection"])
    bot_options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    bot_options_keyboard.add(bot__unit_conversion_option_button, bot__calculation_option_button,
                             bot__date_option_button, bot__currency_option_button).add(
        bot__settings_option_button)

    return bot_options_keyboard


def currency_options_keyboard(user_language):
    now_currency_option_button = KeyboardButton(languages[user_language]["now_currency"])
    # currency_conversion_option_button = KeyboardButton(languages[user_language]["currency_conversion"])
    currency__back_option_button = KeyboardButton(languages[user_language]["back_option_selection"])

    currency_options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    currency_options_keyboard.add(now_currency_option_button).add(
        currency__back_option_button)

    return currency_options_keyboard


def currency_conversion_numbers_inline_keyboard():
    padding = 19
    currency_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                              callback_data="0_currency_converter")
    currency_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                              callback_data="1_currency_converter")
    currency_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                              callback_data="2_currency_converter")
    currency_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                              callback_data="3_currency_converter")
    currency_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                              callback_data="4_currency_converter")
    currency_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                              callback_data="5_currency_converter")
    currency_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                              callback_data="6_currency_converter")
    currency_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                              callback_data="7_currency_converter")
    currency_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                              callback_data="8_currency_converter")
    currency_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                              callback_data="9_currency_converter")
    currency_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                                callback_data="dot_currency_converter")
    currency_converter__clear_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "C".center(padding)),
        callback_data="clear_currency_converter")
    currency_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)),
        callback_data="backward_currency_converter")
    currency_converter__done_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "✅".center(padding)), callback_data="done_currency_converter")
    currency_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(
        currency_converter__1_button,
        currency_converter__2_button,
        currency_converter__3_button,
        currency_converter__4_button,
        currency_converter__5_button,
        currency_converter__6_button,
        currency_converter__7_button,
        currency_converter__8_button,
        currency_converter__9_button,
        currency_converter__dot_button,
        currency_converter__0_button).add(
        currency_converter__clear_button, currency_converter__backward_button, currency_converter__done_button)

    return currency_conversion_numbers_inline_keyboard


def currency_conversion_starter_inline_keyboard(user_language):
    dollar_symbol_button = types.InlineKeyboardButton(
        text=f"$ {languages[user_language]['dollar_currency_converter']} $",
        callback_data="dollar_currency_conversion_starter")

    tooman_symbol_button = types.InlineKeyboardButton(
        text=f"T {languages[user_language]['tooman_currency_converter']} T",
        callback_data="tooman_currency_conversion_starter")

    euro_symbol_button = types.InlineKeyboardButton(
        text=f"€ {languages[user_language]['euro_currency_converter']} €",
        callback_data="euro_currency_conversion_starter")

    pound_symbol_button = types.InlineKeyboardButton(
        text=f"£ {languages[user_language]['pound_currency_converter']} £",
        callback_data="pound_currency_conversion_starter")

    swiss_franc_symbol_button = types.InlineKeyboardButton(
        text=f"₣ {languages[user_language]['swiss_franc_currency_converter']} ₣",
        callback_data="swiss_franc_currency_conversion_starter")

    lir_symbol_button = types.InlineKeyboardButton(
        text=f"₺ {languages[user_language]['lir_currency_converter']} ₺",
        callback_data="lir_currency_conversion_starter")

    arab_emirates_dirham_symbol_button = types.InlineKeyboardButton(
        text=f"dh {languages[user_language]['dirham_currency_converter']} dh",
        callback_data="dirham_currency_conversion_starter")

    currency_conversion_starter_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(dollar_symbol_button,
                                                                                              tooman_symbol_button,
                                                                                              euro_symbol_button,
                                                                                              pound_symbol_button,
                                                                                              lir_symbol_button,
                                                                                              swiss_franc_symbol_button,
                                                                                              arab_emirates_dirham_symbol_button)

    return currency_conversion_starter_inline_keyboard


def currency_conversion_destination_inline_keyboard(user_language):
    dollar_symbol_button = types.InlineKeyboardButton(
        text=f"$ {languages[user_language]['dollar_currency_converter']} $",
        callback_data="dollar_currency_conversion_destination")

    tooman_symbol_button = types.InlineKeyboardButton(
        text=f"T {languages[user_language]['tooman_currency_converter']} T",
        callback_data="tooman_currency_conversion_destination")

    euro_symbol_button = types.InlineKeyboardButton(
        text=f"€ {languages[user_language]['euro_currency_converter']} €",
        callback_data="euro_currency_conversion_destination")

    pound_symbol_button = types.InlineKeyboardButton(
        text=f"£ {languages[user_language]['pound_currency_converter']} £",
        callback_data="pound_currency_conversion_destination")

    swiss_franc_symbol_button = types.InlineKeyboardButton(
        text=f"₣ {languages[user_language]['swiss_franc_currency_converter']} ₣",
        callback_data="swiss_franc_currency_conversion_destination")

    lir_symbol_button = types.InlineKeyboardButton(
        text=f"₺ {languages[user_language]['lir_currency_converter']} ₺",
        callback_data="lir_currency_conversion_destination")

    arab_emirates_dirham_symbol_button = types.InlineKeyboardButton(
        text=f"dh {languages[user_language]['dirham_currency_converter']} dh",
        callback_data="dirham_currency_conversion_destination")

    currency_conversion_destination_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(dollar_symbol_button,
                                                                                                  tooman_symbol_button,
                                                                                                  euro_symbol_button,
                                                                                                  pound_symbol_button,
                                                                                                  lir_symbol_button,
                                                                                                  swiss_franc_symbol_button,
                                                                                                  arab_emirates_dirham_symbol_button)

    return currency_conversion_destination_inline_keyboard


def date__options_keyboard(user_language):
    date__today_option_button = KeyboardButton(languages[user_language]["today"])
    date__date_convert_option_button = KeyboardButton(languages[user_language]["date_convert"])
    date__back_option_button = KeyboardButton(languages[user_language]["back_option_selection"])

    date__options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    date__options_keyboard.add(date__today_option_button, date__date_convert_option_button).add(
        date__back_option_button)

    return date__options_keyboard


def date__date_conversion_options_inline_keyboard(user_language):
    jalali_to_gregorian = types.InlineKeyboardButton(text=languages[user_language]['jalali_to_gregorian'],
                                                     callback_data="jalali_to_gregorian")

    gregorian_to_jalali = types.InlineKeyboardButton(text=languages[user_language]['gregorian_to_jalali'],
                                                     callback_data="gregorian_to_jalali")

    date__date_conversion_options_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
    date__date_conversion_options_inline_keyboard.add(jalali_to_gregorian, gregorian_to_jalali)

    return date__date_conversion_options_inline_keyboard


def date__date_conversion_day_numbers_inline_keyboard():
    padding = 21

    date_conversion__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                           callback_data="0_date_conversion_day")
    date_conversion__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                           callback_data="1_date_conversion_day")
    date_conversion__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                           callback_data="2_date_conversion_day")
    date_conversion__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                           callback_data="3_date_conversion_day")
    date_conversion__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                           callback_data="4_date_conversion_day")
    date_conversion__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                           callback_data="5_date_conversion_day")
    date_conversion__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                           callback_data="6_date_conversion_day")
    date_conversion__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                           callback_data="7_date_conversion_day")
    date_conversion__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                           callback_data="8_date_conversion_day")
    date_conversion__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                           callback_data="9_date_conversion_day")
    date_conversion__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_date_conversion_day")
    date_conversion__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                               callback_data="clear_date_conversion_day")
    date_conversion__done_weight_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "✅".center(padding)), callback_data="done_date_conversion_day")

    date__date_conversion_day_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)

    date__date_conversion_day_numbers_inline_keyboard.add(date_conversion__1_button, date_conversion__2_button,
                                                          date_conversion__3_button, date_conversion__4_button,
                                                          date_conversion__5_button, date_conversion__6_button,
                                                          date_conversion__7_button, date_conversion__8_button,
                                                          date_conversion__9_button, date_conversion__backward_button,
                                                          date_conversion__0_button,
                                                          date_conversion__clear_button).add(
        date_conversion__done_weight_button)

    return date__date_conversion_day_numbers_inline_keyboard


def date__date_conversion_month_numbers_inline_keyboard():
    padding = 21

    date_conversion__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                           callback_data="0_date_conversion_month")
    date_conversion__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                           callback_data="1_date_conversion_month")
    date_conversion__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                           callback_data="2_date_conversion_month")
    date_conversion__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                           callback_data="3_date_conversion_month")
    date_conversion__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                           callback_data="4_date_conversion_month")
    date_conversion__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                           callback_data="5_date_conversion_month")
    date_conversion__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                           callback_data="6_date_conversion_month")
    date_conversion__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                           callback_data="7_date_conversion_month")
    date_conversion__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                           callback_data="8_date_conversion_month")
    date_conversion__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                           callback_data="9_date_conversion_month")
    date_conversion__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_date_conversion_month")
    date_conversion__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                               callback_data="clear_date_conversion_month")
    date_conversion__done_weight_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "✅".center(padding)),
        callback_data="done_date_conversion_month")

    date__date_conversion_month_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)

    date__date_conversion_month_numbers_inline_keyboard.add(date_conversion__1_button, date_conversion__2_button,
                                                            date_conversion__3_button, date_conversion__4_button,
                                                            date_conversion__5_button, date_conversion__6_button,
                                                            date_conversion__7_button, date_conversion__8_button,
                                                            date_conversion__9_button, date_conversion__backward_button,
                                                            date_conversion__0_button,
                                                            date_conversion__clear_button).add(
        date_conversion__done_weight_button)

    return date__date_conversion_month_numbers_inline_keyboard


def date__date_conversion_year_numbers_inline_keyboard():
    padding = 21

    date_conversion__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                           callback_data="0_date_conversion_year")
    date_conversion__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                           callback_data="1_date_conversion_year")
    date_conversion__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                           callback_data="2_date_conversion_year")
    date_conversion__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                           callback_data="3_date_conversion_year")
    date_conversion__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                           callback_data="4_date_conversion_year")
    date_conversion__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                           callback_data="5_date_conversion_year")
    date_conversion__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                           callback_data="6_date_conversion_year")
    date_conversion__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                           callback_data="7_date_conversion_year")
    date_conversion__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                           callback_data="8_date_conversion_year")
    date_conversion__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                           callback_data="9_date_conversion_year")
    date_conversion__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_date_conversion_year")
    date_conversion__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                               callback_data="clear_date_conversion_year")
    date_conversion__done_weight_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "✅".center(padding)),
        callback_data="done_date_conversion_year")

    date__date_conversion_year_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)

    date__date_conversion_year_numbers_inline_keyboard.add(date_conversion__1_button, date_conversion__2_button,
                                                           date_conversion__3_button, date_conversion__4_button,
                                                           date_conversion__5_button, date_conversion__6_button,
                                                           date_conversion__7_button, date_conversion__8_button,
                                                           date_conversion__9_button, date_conversion__backward_button,
                                                           date_conversion__0_button,
                                                           date_conversion__clear_button).add(
        date_conversion__done_weight_button)

    return date__date_conversion_year_numbers_inline_keyboard


def date_calender_inline_keyboard(user_language):
    gregorian_calender = types.InlineKeyboardButton(text=languages[user_language]["gregorian_calender"],
                                                    callback_data="gregorian_calender")
    jalali_calender = types.InlineKeyboardButton(text=languages[user_language]["jalali_calender"],
                                                 callback_data="jalali_calender")
    date_calender_inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    date_calender_inline_keyboard.add(gregorian_calender, jalali_calender)

    return date_calender_inline_keyboard


def calculation__options_keyboard(user_language):
    calculation__calculator_option_button = KeyboardButton(languages[user_language]["calculator"])
    calculation__bmi_option_button = KeyboardButton(languages[user_language]["BMI"])
    calculation__back_option_button = KeyboardButton(languages[user_language]["back_option_selection"])
    calculation_options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    calculation_options_keyboard.add(calculation__bmi_option_button, calculation__calculator_option_button).add(
        calculation__back_option_button)

    return calculation_options_keyboard


def bmi__conversion_weight_inline_keyboard():
    padding = 21

    bmi__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                               callback_data="0_weight_bmi")
    bmi__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                               callback_data="1_weight_bmi")
    bmi__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                               callback_data="2_weight_bmi")
    bmi__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                               callback_data="3_weight_bmi")
    bmi__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                               callback_data="4_weight_bmi")
    bmi__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                               callback_data="5_weight_bmi")
    bmi__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                               callback_data="6_weight_bmi")
    bmi__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                               callback_data="7_weight_bmi")
    bmi__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                               callback_data="8_weight_bmi")
    bmi__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                               callback_data="9_weight_bmi")
    bmi__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                 callback_data="dot_weight_bmi")
    bmi__backward_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "«".center(padding)),
                                                      callback_data="backward_weight_bmi")
    bmi__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                   callback_data="clear_weight_bmi")
    bmi__done_weight_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                         callback_data="done_weight_bmi")
    bmi__conversion_weight_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
    bmi__conversion_weight_inline_keyboard.add(bmi__1_button, bmi__2_button, bmi__3_button, bmi__4_button,
                                               bmi__5_button, bmi__6_button, bmi__7_button, bmi__8_button,
                                               bmi__9_button, bmi__dot_button, bmi__0_button).add(bmi__backward_button,
                                                                                                  bmi__clear_button,
                                                                                                  bmi__done_weight_button)

    return bmi__conversion_weight_inline_keyboard


def bmi__conversion_height_inline_keyboard():
    padding = 21

    bmi__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                               callback_data="0_height_bmi")
    bmi__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                               callback_data="1_height_bmi")
    bmi__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                               callback_data="2_height_bmi")
    bmi__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                               callback_data="3_height_bmi")
    bmi__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                               callback_data="4_height_bmi")
    bmi__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                               callback_data="5_height_bmi")
    bmi__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                               callback_data="6_height_bmi")
    bmi__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                               callback_data="7_height_bmi")
    bmi__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                               callback_data="8_height_bmi")
    bmi__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                               callback_data="9_height_bmi")
    bmi__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                 callback_data="dot_height_bmi")
    bmi__backward_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "«".center(padding)),
                                                      callback_data="backward_height_bmi")
    bmi__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                   callback_data="clear_height_bmi")
    bmi__done_height_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                         callback_data="done_height_bmi")
    bmi__conversion_height_inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
    bmi__conversion_height_inline_keyboard.add(bmi__1_button, bmi__2_button, bmi__3_button, bmi__4_button,
                                               bmi__5_button, bmi__6_button, bmi__7_button, bmi__8_button,
                                               bmi__9_button, bmi__dot_button, bmi__0_button).add(bmi__backward_button,
                                                                                                  bmi__clear_button,
                                                                                                  bmi__done_height_button)

    return bmi__conversion_height_inline_keyboard


def bmi__conversion_see_bmi_chart_inline_keyboard(user_language):
    bmi__see_chart_button = types.InlineKeyboardButton(text=languages[user_language]["see_bmi_chart"],
                                                       callback_data="see_chart_bmi")
    bmi__conversion_see_bmi_chart_inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    bmi__conversion_see_bmi_chart_inline_keyboard.add(bmi__see_chart_button)

    return bmi__conversion_see_bmi_chart_inline_keyboard


def calculator__inline_keyboard():
    padding = 15

    calculator__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                      callback_data="0_calculator")
    calculator__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                      callback_data="1_calculator")
    calculator__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                      callback_data="2_calculator")
    calculator__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                      callback_data="3_calculator")
    calculator__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                      callback_data="4_calculator")
    calculator__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                      callback_data="5_calculator")
    calculator__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                      callback_data="6_calculator")
    calculator__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                      callback_data="7_calculator")
    calculator__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                      callback_data="8_calculator")
    calculator__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                      callback_data="9_calculator")
    calculator__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                        callback_data="dot_calculator")
    calculator__plus_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "+".center(padding)),
                                                         callback_data="plus_calculator")
    calculator__mines_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "-".center(padding)),
                                                          callback_data="mines_calculator")
    calculator__times_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "×".center(padding)),
                                                          callback_data="times_calculator")
    calculator__fraction_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "÷".center(padding)),
                                                             callback_data="fraction_calculator")
    calculator__sin_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "sin".center(padding)),
                                                        callback_data="sin_calculator")
    calculator__cos_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "cos".center(padding)),
                                                        callback_data="cos_calculator")
    calculator__tan_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "tan".center(padding)),
                                                        callback_data="tan_calculator")
    calculator__cot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "cot".center(padding)),
                                                        callback_data="cot_calculator")
    calculator__pi_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "π".center(padding)),
                                                       callback_data="pi_calculator")
    calculator__opening_parentheses_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "(".center(padding)),
        callback_data="opening_parentheses_calculator")
    calculator__closing_parentheses_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', ")".center(padding)),
        callback_data="closing_parentheses_calculator")
    calculator__factorial_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "!".center(padding)),
                                                              callback_data="factorial_calculator")
    calculator__power_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "^".center(padding)),
                                                          callback_data="power_calculator")
    calculator__sqrt_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "√".center(padding)),
                                                         callback_data="sqrt_calculator")
    calculator__log_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "log".center(padding)),
                                                        callback_data="log_calculator")
    calculator__backward_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "«".center(padding)),
                                                             callback_data="backward_calculator")
    calculator__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                          callback_data="clear_calculator")
    calculator__equal_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "=".center(padding)),
                                                          callback_data="done_calculator")
    calculator__neg_or_pos_maker_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "+/₋".center(padding)),
        callback_data="neg_or_pos_maker_calculator")
    calculator_inline_keyboard = types.InlineKeyboardMarkup(row_width=4).add(calculator__sin_button,
                                                                             calculator__cos_button,
                                                                             calculator__tan_button,
                                                                             calculator__cot_button,
                                                                             calculator__opening_parentheses_button,
                                                                             calculator__closing_parentheses_button,
                                                                             calculator__sqrt_button,
                                                                             calculator__power_button,
                                                                             calculator__7_button,
                                                                             calculator__8_button,
                                                                             calculator__9_button,
                                                                             calculator__fraction_button,
                                                                             calculator__4_button,
                                                                             calculator__5_button,
                                                                             calculator__6_button,
                                                                             calculator__times_button,
                                                                             calculator__1_button,
                                                                             calculator__2_button,
                                                                             calculator__3_button,
                                                                             calculator__mines_button,
                                                                             calculator__dot_button,
                                                                             calculator__0_button,
                                                                             calculator__pi_button,
                                                                             calculator__plus_button).add(
        calculator__log_button, calculator__neg_or_pos_maker_button, calculator__backward_button,
        calculator__clear_button).add(calculator__equal_button)

    return calculator_inline_keyboard


def unit_conversion_options_keyboard(user_language):
    conversion__numeral_system_option_button = KeyboardButton(languages[user_language]["numeral"])
    conversion__length_option_button = KeyboardButton(languages[user_language]["length"])
    conversion__mass_option_button = KeyboardButton(languages[user_language]["mass"])
    conversion__temperature_option_button = KeyboardButton(languages[user_language]["temperature"])
    conversion__time_option_button = KeyboardButton(languages[user_language]["time"])
    conversion__data_option_button = KeyboardButton(languages[user_language]["data"])
    conversion__back_option_button = KeyboardButton(languages[user_language]["back_option_selection"])
    conversion_options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    conversion_options_keyboard.add(conversion__numeral_system_option_button, conversion__length_option_button,
                                    conversion__mass_option_button, conversion__temperature_option_button,
                                    conversion__time_option_button, conversion__data_option_button).add(
        conversion__back_option_button)

    return conversion_options_keyboard


def data_conversion_numbers_inline_keyboard():
    padding = 23

    data_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                          callback_data="0_data_converter")
    data_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                          callback_data="1_data_converter")
    data_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                          callback_data="2_data_converter")
    data_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                          callback_data="3_data_converter")
    data_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                          callback_data="4_data_converter")
    data_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                          callback_data="5_data_converter")
    data_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                          callback_data="6_data_converter")
    data_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                          callback_data="7_data_converter")
    data_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                          callback_data="8_data_converter")
    data_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                          callback_data="9_data_converter")
    data_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                            callback_data="dot_data_converter")
    data_converter__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                              callback_data="clear_data_converter")
    data_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_data_converter")
    data_converter__done_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                             callback_data="done_data_converter")
    data_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(data_converter__1_button,
                                                                                          data_converter__2_button,
                                                                                          data_converter__3_button,
                                                                                          data_converter__4_button,
                                                                                          data_converter__5_button,
                                                                                          data_converter__6_button,
                                                                                          data_converter__7_button,
                                                                                          data_converter__8_button,
                                                                                          data_converter__9_button,
                                                                                          data_converter__dot_button,
                                                                                          data_converter__0_button).add(
        data_converter__clear_button, data_converter__backward_button, data_converter__done_button)

    return data_conversion_numbers_inline_keyboard


def data_conversion_starter_inline_keyboard(user_language):
    bit_symbol_button = types.InlineKeyboardButton(text=f"b {languages[user_language]['bit_data_converter']}",
                                                   callback_data="bit_data_conversion_starter")

    byte_symbol_button = types.InlineKeyboardButton(text=f"B {languages[user_language]['byte_data_converter']}",
                                                    callback_data="byte_data_conversion_starter")

    kilo_byte_symbol_button = types.InlineKeyboardButton(
        text=f"KB {languages[user_language]['kilo_byte_data_converter']}",
        callback_data="kilo_byte_data_conversion_starter")

    mega_byte_symbol_button = types.InlineKeyboardButton(
        text=f"MB {languages[user_language]['mega_byte_data_converter']}",
        callback_data="mega_byte_data_conversion_starter")

    giga_byte_symbol_button = types.InlineKeyboardButton(
        text=f"GB {languages[user_language]['giga_byte_data_converter']}",
        callback_data="giga_byte_data_conversion_starter")

    tera_byte_symbol_button = types.InlineKeyboardButton(
        text=f"TB {languages[user_language]['tera_byte_data_converter']}",
        callback_data="tera_byte_data_conversion_starter")

    peta_byte_symbol_button = types.InlineKeyboardButton(
        text=f"PB {languages[user_language]['peta_byte_data_converter']}",
        callback_data="peta_byte_data_conversion_starter")

    exa_byte_symbol_button = types.InlineKeyboardButton(
        text=f"EB {languages[user_language]['exa_byte_data_converter']}",
        callback_data="exa_byte_data_conversion_starter")

    data_conversion_starter_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(bit_symbol_button,
                                                                                          byte_symbol_button,
                                                                                          kilo_byte_symbol_button,
                                                                                          mega_byte_symbol_button,
                                                                                          giga_byte_symbol_button,
                                                                                          tera_byte_symbol_button,
                                                                                          peta_byte_symbol_button,
                                                                                          exa_byte_symbol_button)

    return data_conversion_starter_inline_keyboard


def data_conversion_destination_inline_keyboard(user_language):
    bit_symbol_button = types.InlineKeyboardButton(text=f"b {languages[user_language]['bit_data_converter']}",
                                                   callback_data="bit_data_conversion_destination")

    byte_symbol_button = types.InlineKeyboardButton(text=f"B {languages[user_language]['byte_data_converter']}",
                                                    callback_data="byte_data_conversion_destination")

    kilo_byte_symbol_button = types.InlineKeyboardButton(
        text=f"KB {languages[user_language]['kilo_byte_data_converter']}",
        callback_data="kilo_byte_data_conversion_destination")

    mega_byte_symbol_button = types.InlineKeyboardButton(
        text=f"MB {languages[user_language]['mega_byte_data_converter']}",
        callback_data="mega_byte_data_conversion_destination")

    giga_byte_symbol_button = types.InlineKeyboardButton(
        text=f"GB {languages[user_language]['giga_byte_data_converter']}",
        callback_data="giga_byte_data_conversion_destination")

    tera_byte_symbol_button = types.InlineKeyboardButton(
        text=f"TB {languages[user_language]['tera_byte_data_converter']}",
        callback_data="tera_byte_data_conversion_destination")

    peta_byte_symbol_button = types.InlineKeyboardButton(
        text=f"PB {languages[user_language]['peta_byte_data_converter']}",
        callback_data="peta_byte_data_conversion_destination")

    exa_byte_symbol_button = types.InlineKeyboardButton(
        text=f"EB {languages[user_language]['exa_byte_data_converter']}",
        callback_data="exa_byte_data_conversion_destination")

    data_conversion_destination_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(bit_symbol_button,
                                                                                              byte_symbol_button,
                                                                                              kilo_byte_symbol_button,
                                                                                              mega_byte_symbol_button,
                                                                                              giga_byte_symbol_button,
                                                                                              tera_byte_symbol_button,
                                                                                              peta_byte_symbol_button,
                                                                                              exa_byte_symbol_button)

    return data_conversion_destination_inline_keyboard


def length_conversion_numbers_inline_keyboard():
    padding = 23

    length_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                            callback_data="0_length_converter")
    length_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                            callback_data="1_length_converter")
    length_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                            callback_data="2_length_converter")
    length_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                            callback_data="3_length_converter")
    length_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                            callback_data="4_length_converter")
    length_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                            callback_data="5_length_converter")
    length_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                            callback_data="6_length_converter")
    length_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                            callback_data="7_length_converter")
    length_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                            callback_data="8_length_converter")
    length_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                            callback_data="9_length_converter")

    length_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                              callback_data="dot_length_converter")
    length_converter__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                                callback_data="clear_length_converter")
    length_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_length_converter")
    length_converter__done_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                               callback_data="done_length_converter")
    length_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(length_converter__1_button,
                                                                                            length_converter__2_button,
                                                                                            length_converter__3_button,
                                                                                            length_converter__4_button,
                                                                                            length_converter__5_button,
                                                                                            length_converter__6_button,
                                                                                            length_converter__7_button,
                                                                                            length_converter__8_button,
                                                                                            length_converter__9_button,
                                                                                            length_converter__dot_button,
                                                                                            length_converter__0_button).add(
        length_converter__clear_button, length_converter__backward_button, length_converter__done_button)

    return length_conversion_numbers_inline_keyboard


def length_conversion_starter_inline_keyboard(user_language):
    pico_meter_symbol_button = types.InlineKeyboardButton(
        text=f"pm {languages[user_language]['pico_meter_length_converter']}",
        callback_data="pico_meter_length_conversion_starter")

    nano_meter_symbol_button = types.InlineKeyboardButton(
        text=f"nm {languages[user_language]['nano_meter_length_converter']}",
        callback_data="nano_meter_length_conversion_starter")

    micro_meter_symbol_button = types.InlineKeyboardButton(
        text=f"μm {languages[user_language]['micro_meter_length_converter']}",
        callback_data="micro_meter_length_conversion_starter")

    milli_meter_symbol_button = types.InlineKeyboardButton(
        text=f"mm {languages[user_language]['milli_meter_length_converter']}",
        callback_data="milli_meter_length_conversion_starter")

    centi_meter_symbol_button = types.InlineKeyboardButton(
        text=f"cm {languages[user_language]['centi_meter_length_converter']}",
        callback_data="centi_meter_length_conversion_starter")

    desi_meter_symbol_button = types.InlineKeyboardButton(
        text=f"dm {languages[user_language]['desi_meter_length_converter']}",
        callback_data="desi_meter_length_conversion_starter")

    meter_symbol_button = types.InlineKeyboardButton(text=f"m {languages[user_language]['meter_length_converter']}",
                                                     callback_data="meter_length_conversion_starter")

    kilo_meter_symbol_button = types.InlineKeyboardButton(
        text=f"Km {languages[user_language]['kilo_meter_length_converter']}",
        callback_data="kilo_meter_length_conversion_starter")

    mile_symbol_button = types.InlineKeyboardButton(text=f"mi {languages[user_language]['mile_length_converter']}",
                                                    callback_data="mile_length_conversion_starter")

    nautical_mile_symbol_button = types.InlineKeyboardButton(
        text=f"nmi {languages[user_language]['nautical_mile_length_converter']}",
        callback_data="nautical_mile_length_conversion_starter")

    foot_symbol_button = types.InlineKeyboardButton(text=f"ft {languages[user_language]['foot_length_converter']}",
                                                    callback_data="foot_length_conversion_starter")

    inch_symbol_button = types.InlineKeyboardButton(text=f"in {languages[user_language]['inch_length_converter']}",
                                                    callback_data="inch_length_conversion_starter")

    yard_symbol_button = types.InlineKeyboardButton(text=f"yd {languages[user_language]['yard_length_converter']}",
                                                    callback_data="yard_length_conversion_starter")

    fathom_symbol_button = types.InlineKeyboardButton(text=f"ftm {languages[user_language]['fathom_length_converter']}",
                                                      callback_data="fathom_length_conversion_starter")

    light_year_symbol_button = types.InlineKeyboardButton(
        text=f"ly {languages[user_language]['light_year_length_converter']}",
        callback_data="light_year_length_conversion_starter")

    length_conversion_starter_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(
        pico_meter_symbol_button, nano_meter_symbol_button, micro_meter_symbol_button, milli_meter_symbol_button,
        centi_meter_symbol_button, desi_meter_symbol_button, meter_symbol_button, kilo_meter_symbol_button,
        mile_symbol_button, nautical_mile_symbol_button, foot_symbol_button, inch_symbol_button, yard_symbol_button,
        fathom_symbol_button, light_year_symbol_button)

    return length_conversion_starter_inline_keyboard


def length_conversion_destination_inline_keyboard(user_language):
    pico_meter_symbol_button = types.InlineKeyboardButton(
        text=f"pm {languages[user_language]['pico_meter_length_converter']}",
        callback_data="pico_meter_length_conversion_destination")

    nano_meter_symbol_button = types.InlineKeyboardButton(
        text=f"nm {languages[user_language]['nano_meter_length_converter']}",
        callback_data="nano_meter_length_conversion_destination")

    micro_meter_symbol_button = types.InlineKeyboardButton(
        text=f"μm {languages[user_language]['micro_meter_length_converter']}",
        callback_data="micro_meter_length_conversion_destination")

    milli_meter_symbol_button = types.InlineKeyboardButton(
        text=f"mm {languages[user_language]['milli_meter_length_converter']}",
        callback_data="milli_meter_length_conversion_destination")

    centi_meter_symbol_button = types.InlineKeyboardButton(
        text=f"cm {languages[user_language]['centi_meter_length_converter']}",
        callback_data="centi_meter_length_conversion_destination")

    desi_meter_symbol_button = types.InlineKeyboardButton(
        text=f"dm {languages[user_language]['desi_meter_length_converter']}",
        callback_data="desi_meter_length_conversion_destination")

    meter_symbol_button = types.InlineKeyboardButton(text=f"m {languages[user_language]['meter_length_converter']}",
                                                     callback_data="meter_length_conversion_destination")

    kilo_meter_symbol_button = types.InlineKeyboardButton(
        text=f"Km {languages[user_language]['kilo_meter_length_converter']}",
        callback_data="kilo_meter_length_conversion_destination")

    mile_symbol_button = types.InlineKeyboardButton(text=f"mi {languages[user_language]['mile_length_converter']}",
                                                    callback_data="mile_length_conversion_destination")

    nautical_mile_symbol_button = types.InlineKeyboardButton(
        text=f"nmi {languages[user_language]['nautical_mile_length_converter']}",
        callback_data="nautical_mile_length_conversion_destination")

    foot_symbol_button = types.InlineKeyboardButton(text=f"ft {languages[user_language]['foot_length_converter']}",
                                                    callback_data="foot_length_conversion_destination")

    inch_symbol_button = types.InlineKeyboardButton(text=f"in {languages[user_language]['inch_length_converter']}",
                                                    callback_data="inch_length_conversion_destination")

    yard_symbol_button = types.InlineKeyboardButton(text=f"yd {languages[user_language]['yard_length_converter']}",
                                                    callback_data="yard_length_conversion_destination")

    fathom_symbol_button = types.InlineKeyboardButton(text=f"ftm {languages[user_language]['fathom_length_converter']}",
                                                      callback_data="fathom_length_conversion_destination")

    light_year_symbol_button = types.InlineKeyboardButton(
        text=f"ly {languages[user_language]['light_year_length_converter']}",
        callback_data="light_year_length_conversion_destination")

    length_conversion_destination_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(
        pico_meter_symbol_button, nano_meter_symbol_button, micro_meter_symbol_button, milli_meter_symbol_button,
        centi_meter_symbol_button, desi_meter_symbol_button, meter_symbol_button, kilo_meter_symbol_button,
        mile_symbol_button, nautical_mile_symbol_button, foot_symbol_button, inch_symbol_button, yard_symbol_button,
        fathom_symbol_button, light_year_symbol_button)

    return length_conversion_destination_inline_keyboard


def mass_conversion_numbers_inline_keyboard():
    padding = 23

    mass_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                          callback_data="0_mass_converter")
    mass_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                          callback_data="1_mass_converter")

    mass_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                          callback_data="2_mass_converter")
    mass_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                          callback_data="3_mass_converter")
    mass_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                          callback_data="4_mass_converter")
    mass_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                          callback_data="5_mass_converter")
    mass_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                          callback_data="6_mass_converter")
    mass_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                          callback_data="7_mass_converter")
    mass_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                          callback_data="8_mass_converter")
    mass_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                          callback_data="9_mass_converter")
    mass_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                            callback_data="dot_mass_converter")
    mass_converter__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                              callback_data="clear_mass_converter")
    mass_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)), callback_data="backward_mass_converter")
    mass_converter__done_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                             callback_data="done_mass_converter")
    mass_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(mass_converter__1_button,
                                                                                          mass_converter__2_button,
                                                                                          mass_converter__3_button,
                                                                                          mass_converter__4_button,
                                                                                          mass_converter__5_button,
                                                                                          mass_converter__6_button,
                                                                                          mass_converter__7_button,
                                                                                          mass_converter__8_button,
                                                                                          mass_converter__9_button,
                                                                                          mass_converter__dot_button,
                                                                                          mass_converter__0_button).add(
        mass_converter__clear_button, mass_converter__backward_button, mass_converter__done_button)

    return mass_conversion_numbers_inline_keyboard


def mass_conversion_starter_inline_keyboard(user_language):
    nano_gram_symbol_button = types.InlineKeyboardButton(
        text=f"ng {languages[user_language]['nano_gram_mass_converter']}",
        callback_data="nano_gram_mass_conversion_starter")

    micro_gram_symbol_button = types.InlineKeyboardButton(
        text=f"μg {languages[user_language]['micro_gram_mass_converter']}",
        callback_data="micro_gram_mass_conversion_starter")

    quintal_symbol_button = types.InlineKeyboardButton(text=f"q {languages[user_language]['quintal_mass_converter']}",
                                                       callback_data="quintal_mass_conversion_starter")

    milli_gram_symbol_button = types.InlineKeyboardButton(
        text=f"mg {languages[user_language]['milli_gram_mass_converter']}",
        callback_data="milli_gram_mass_conversion_starter")

    centi_gram_symbol_button = types.InlineKeyboardButton(
        text=f"cg {languages[user_language]['centi_gram_mass_converter']}",
        callback_data="centi_gram_mass_conversion_starter")

    desi_gram_symbol_button = types.InlineKeyboardButton(
        text=f"dg {languages[user_language]['desi_gram_mass_converter']}",
        callback_data="desi_gram_mass_conversion_starter")

    gram_symbol_button = types.InlineKeyboardButton(text=f"g {languages[user_language]['gram_mass_converter']}",
                                                    callback_data="gram_mass_conversion_starter")

    kilo_gram_symbol_button = types.InlineKeyboardButton(
        text=f"Kg {languages[user_language]['kilo_gram_mass_converter']}",
        callback_data="kilo_gram_mass_conversion_starter")

    tone_symbol_button = types.InlineKeyboardButton(text=f"t {languages[user_language]['tone_mass_converter']}",
                                                    callback_data="tone_mass_conversion_starter")

    pound_symbol_button = types.InlineKeyboardButton(text=f"lb {languages[user_language]['pound_mass_converter']}",
                                                     callback_data="pound_mass_conversion_starter")

    ounce_symbol_button = types.InlineKeyboardButton(text=f"oz {languages[user_language]['ounce_mass_converter']}",
                                                     callback_data="ounce_mass_conversion_starter")

    carat_symbol_button = types.InlineKeyboardButton(text=f"ct {languages[user_language]['carat_mass_converter']}",
                                                     callback_data="carat_mass_conversion_starter")

    grain_symbol_button = types.InlineKeyboardButton(text=f"gr {languages[user_language]['grain_mass_converter']}",
                                                     callback_data="grain_mass_conversion_starter")

    long_ton_symbol_button = types.InlineKeyboardButton(
        text=f"l.t {languages[user_language]['long_ton_mass_converter']}",
        callback_data="long_ton_mass_conversion_starter")

    short_ton_symbol_button = types.InlineKeyboardButton(
        text=f"sh.t {languages[user_language]['short_ton_mass_converter']}",
        callback_data="short_ton_mass_conversion_starter")

    stone_symbol_button = types.InlineKeyboardButton(text=f"st {languages[user_language]['stone_mass_converter']}",
                                                     callback_data="stone_mass_conversion_starter")

    dram_symbol_button = types.InlineKeyboardButton(text=f"dr {languages[user_language]['dram_mass_converter']}",
                                                    callback_data="dram_mass_conversion_starter")

    sir_symbol_button = types.InlineKeyboardButton(text=f"sir {languages[user_language]['sir_mass_converter']}",
                                                   callback_data="sir_mass_conversion_starter")

    mass_conversion_starter_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(nano_gram_symbol_button,
                                                                                          micro_gram_symbol_button,
                                                                                          quintal_symbol_button,
                                                                                          milli_gram_symbol_button,
                                                                                          centi_gram_symbol_button,
                                                                                          desi_gram_symbol_button,
                                                                                          gram_symbol_button,
                                                                                          kilo_gram_symbol_button,
                                                                                          tone_symbol_button,
                                                                                          pound_symbol_button,
                                                                                          ounce_symbol_button,
                                                                                          carat_symbol_button,
                                                                                          grain_symbol_button,
                                                                                          long_ton_symbol_button,
                                                                                          short_ton_symbol_button,
                                                                                          stone_symbol_button,
                                                                                          dram_symbol_button,
                                                                                          sir_symbol_button)

    return mass_conversion_starter_inline_keyboard


def mass_conversion_destination_inline_keyboard(user_language):
    nano_gram_symbol_button = types.InlineKeyboardButton(
        text=f"ng {languages[user_language]['nano_gram_mass_converter']}",
        callback_data="nano_gram_mass_conversion_destination")

    micro_gram_symbol_button = types.InlineKeyboardButton(
        text=f"μg {languages[user_language]['micro_gram_mass_converter']}",
        callback_data="micro_gram_mass_conversion_destination")

    quintal_symbol_button = types.InlineKeyboardButton(text=f"q {languages[user_language]['quintal_mass_converter']}",
                                                       callback_data="quintal_mass_conversion_destination")

    milli_gram_symbol_button = types.InlineKeyboardButton(
        text=f"mg {languages[user_language]['milli_gram_mass_converter']}",
        callback_data="milli_gram_mass_conversion_destination")

    centi_gram_symbol_button = types.InlineKeyboardButton(
        text=f"cg {languages[user_language]['centi_gram_mass_converter']}",
        callback_data="centi_gram_mass_conversion_destination")

    desi_gram_symbol_button = types.InlineKeyboardButton(
        text=f"dg {languages[user_language]['desi_gram_mass_converter']}",
        callback_data="desi_gram_mass_conversion_destination")

    gram_symbol_button = types.InlineKeyboardButton(text=f"g {languages[user_language]['gram_mass_converter']}",
                                                    callback_data="gram_mass_conversion_destination")

    kilo_gram_symbol_button = types.InlineKeyboardButton(
        text=f"Kg {languages[user_language]['kilo_gram_mass_converter']}",
        callback_data="kilo_gram_mass_conversion_destination")

    tone_symbol_button = types.InlineKeyboardButton(text=f"t {languages[user_language]['tone_mass_converter']}",
                                                    callback_data="tone_mass_conversion_destination")

    pound_symbol_button = types.InlineKeyboardButton(text=f"lb {languages[user_language]['pound_mass_converter']}",
                                                     callback_data="pound_mass_conversion_destination")

    ounce_symbol_button = types.InlineKeyboardButton(text=f"oz {languages[user_language]['ounce_mass_converter']}",
                                                     callback_data="ounce_mass_conversion_destination")

    carat_symbol_button = types.InlineKeyboardButton(text=f"ct {languages[user_language]['carat_mass_converter']}",
                                                     callback_data="carat_mass_conversion_destination")

    grain_symbol_button = types.InlineKeyboardButton(text=f"gr {languages[user_language]['grain_mass_converter']}",
                                                     callback_data="grain_mass_conversion_destination")

    long_ton_symbol_button = types.InlineKeyboardButton(
        text=f"l.t {languages[user_language]['long_ton_mass_converter']}",
        callback_data="long_ton_mass_conversion_destination")

    short_ton_symbol_button = types.InlineKeyboardButton(
        text=f"sh.t {languages[user_language]['short_ton_mass_converter']}",
        callback_data="short_ton_mass_conversion_destination")

    stone_symbol_button = types.InlineKeyboardButton(text=f"st {languages[user_language]['stone_mass_converter']}",
                                                     callback_data="stone_mass_conversion_destination")

    dram_symbol_button = types.InlineKeyboardButton(text=f"dr {languages[user_language]['dram_mass_converter']}",
                                                    callback_data="dram_mass_conversion_destination")

    sir_symbol_button = types.InlineKeyboardButton(text=f"sir {languages[user_language]['sir_mass_converter']}",
                                                   callback_data="sir_mass_conversion_destination")

    mass_conversion_destination_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(nano_gram_symbol_button,
                                                                                              micro_gram_symbol_button,
                                                                                              quintal_symbol_button,
                                                                                              milli_gram_symbol_button,
                                                                                              centi_gram_symbol_button,
                                                                                              desi_gram_symbol_button,
                                                                                              gram_symbol_button,
                                                                                              kilo_gram_symbol_button,
                                                                                              tone_symbol_button,
                                                                                              pound_symbol_button,
                                                                                              ounce_symbol_button,
                                                                                              carat_symbol_button,
                                                                                              grain_symbol_button,
                                                                                              long_ton_symbol_button,
                                                                                              short_ton_symbol_button,
                                                                                              stone_symbol_button,
                                                                                              dram_symbol_button,
                                                                                              sir_symbol_button)

    return mass_conversion_destination_inline_keyboard


def temperature_conversion_numbers_inline_keyboard():
    padding = 23

    temperature_converter__0_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "0".center(padding)), callback_data="0_temperature_converter")
    temperature_converter__1_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "1".center(padding)), callback_data="1_temperature_converter")
    temperature_converter__2_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "2".center(padding)), callback_data="2_temperature_converter")
    temperature_converter__3_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "3".center(padding)), callback_data="3_temperature_converter")
    temperature_converter__4_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "4".center(padding)), callback_data="4_temperature_converter")
    temperature_converter__5_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "5".center(padding)), callback_data="5_temperature_converter")
    temperature_converter__6_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "6".center(padding)), callback_data="6_temperature_converter")
    temperature_converter__7_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "7".center(padding)), callback_data="7_temperature_converter")
    temperature_converter__8_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "8".center(padding)), callback_data="8_temperature_converter")
    temperature_converter__9_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "9".center(padding)), callback_data="9_temperature_converter")

    temperature_converter__dot_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', ".".center(padding)), callback_data="dot_temperature_converter")

    temperature_converter__mines_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "+/₋".center(padding)),
        callback_data="neg_or_pos_maker_temperature_converter")

    temperature_converter__clear_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "C".center(padding)),
        callback_data="clear_temperature_converter")

    temperature_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)),
        callback_data="backward_temperature_converter")

    temperature_converter__done_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "✅".center(padding)),
        callback_data="done_temperature_converter")

    temperature_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(
        temperature_converter__1_button,
        temperature_converter__2_button,
        temperature_converter__3_button,
        temperature_converter__4_button,
        temperature_converter__5_button,
        temperature_converter__6_button,
        temperature_converter__7_button,
        temperature_converter__8_button,
        temperature_converter__9_button,
        temperature_converter__mines_button,
        temperature_converter__dot_button,
        temperature_converter__0_button).add(
        temperature_converter__clear_button, temperature_converter__backward_button, temperature_converter__done_button)

    return temperature_conversion_numbers_inline_keyboard


def temperature_conversion_starter_inline_keyboard(user_language):
    celsius_symbol_button = types.InlineKeyboardButton(
        text=f"C° {languages[user_language]['celsius_temperature_converter']}",
        callback_data="celsius_temperature_conversion_starter")

    fahrenheit_symbol_button = types.InlineKeyboardButton(
        text=f"F° {languages[user_language]['fahrenheit_temperature_converter']}",
        callback_data="fahrenheit_temperature_conversion_starter")

    kelvin_symbol_button = types.InlineKeyboardButton(
        text=f"K {languages[user_language]['kelvin_temperature_converter']}",
        callback_data="kelvin_temperature_conversion_starter")

    temperature_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(celsius_symbol_button,
                                                                                                 fahrenheit_symbol_button,
                                                                                                 kelvin_symbol_button)

    return temperature_conversion_numbers_inline_keyboard


def temperature_conversion_destination_inline_keyboard(user_language):
    celsius_symbol_button = types.InlineKeyboardButton(
        text=f"C° {languages[user_language]['celsius_temperature_converter']}",
        callback_data="celsius_temperature_conversion_destination")

    fahrenheit_symbol_button = types.InlineKeyboardButton(
        text=f"F° {languages[user_language]['fahrenheit_temperature_converter']}",
        callback_data="fahrenheit_temperature_conversion_destination")

    kelvin_symbol_button = types.InlineKeyboardButton(
        text=f"K {languages[user_language]['kelvin_temperature_converter']}",
        callback_data="kelvin_temperature_conversion_destination")

    temperature_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(celsius_symbol_button,
                                                                                                 fahrenheit_symbol_button,
                                                                                                 kelvin_symbol_button)

    return temperature_conversion_numbers_inline_keyboard


def time_conversion_numbers_inline_keyboard():
    padding = 23

    time_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                          callback_data="0_time_converter")
    time_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                          callback_data="1_time_converter")
    time_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                          callback_data="2_time_converter")
    time_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                          callback_data="3_time_converter")
    time_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                          callback_data="4_time_converter")
    time_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                          callback_data="5_time_converter")
    time_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                          callback_data="6_time_converter")
    time_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                          callback_data="7_time_converter")
    time_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                          callback_data="8_time_converter")
    time_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                          callback_data="9_time_converter")
    time_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                            callback_data="dot_time_converter")
    time_converter__clear_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                              callback_data="clear_time_converter")
    time_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)),
        callback_data="backward_time_converter")

    time_converter__done_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                             callback_data="done_time_converter")
    time_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(
        time_converter__1_button,
        time_converter__2_button,
        time_converter__3_button,
        time_converter__4_button,
        time_converter__5_button,
        time_converter__6_button,
        time_converter__7_button,
        time_converter__8_button,
        time_converter__9_button,
        time_converter__dot_button,
        time_converter__0_button).add(
        time_converter__clear_button, time_converter__backward_button, time_converter__done_button)

    return time_conversion_numbers_inline_keyboard


def time_conversion_starter_inline_keyboard(user_language):
    pico_second_symbol_button = types.InlineKeyboardButton(
        text=f"ps {languages[user_language]['pico_second_time_converter']}",
        callback_data="pico_second_time_conversion_starter")

    nano_second_symbol_button = types.InlineKeyboardButton(
        text=f"ns {languages[user_language]['nano_second_time_converter']}",
        callback_data="nano_second_time_conversion_starter")

    micro_second_symbol_button = types.InlineKeyboardButton(
        text=f"μs {languages[user_language]['micro_second_time_converter']}",
        callback_data="micro_second_time_conversion_starter")

    milli_second_symbol_button = types.InlineKeyboardButton(
        text=f"ms {languages[user_language]['milli_second_time_converter']}",
        callback_data="milli_second_time_conversion_starter")

    second_symbol_button = types.InlineKeyboardButton(text=f"s {languages[user_language]['second_time_converter']}",
                                                      callback_data="second_time_conversion_starter")

    min_symbol_button = types.InlineKeyboardButton(text=f"min {languages[user_language]['min_time_converter']}",
                                                   callback_data="min_time_conversion_starter")

    hour_symbol_button = types.InlineKeyboardButton(text=f"h {languages[user_language]['hour_time_converter']}",
                                                    callback_data="hour_time_conversion_starter")

    day_symbol_button = types.InlineKeyboardButton(text=f"d {languages[user_language]['day_time_converter']}",
                                                   callback_data="day_time_conversion_starter")

    month_symbol_button = types.InlineKeyboardButton(text=f"mo {languages[user_language]['month_time_converter']}",
                                                     callback_data="month_time_conversion_starter")

    year_symbol_button = types.InlineKeyboardButton(text=f"y {languages[user_language]['year_time_converter']}",
                                                    callback_data="year_time_conversion_starter")

    decade_symbol_button = types.InlineKeyboardButton(text=f"dec {languages[user_language]['decade_time_converter']}",
                                                      callback_data="decade_time_conversion_starter")

    century_symbol_button = types.InlineKeyboardButton(
        text=f"cent {languages[user_language]['century_time_converter']}",
        callback_data="century_time_conversion_starter")

    time_conversion_starter_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(pico_second_symbol_button,
                                                                                          nano_second_symbol_button,
                                                                                          micro_second_symbol_button,
                                                                                          milli_second_symbol_button,
                                                                                          second_symbol_button,
                                                                                          min_symbol_button,
                                                                                          hour_symbol_button,
                                                                                          day_symbol_button,
                                                                                          month_symbol_button,
                                                                                          year_symbol_button,
                                                                                          decade_symbol_button,
                                                                                          century_symbol_button)

    return time_conversion_starter_inline_keyboard


def time_conversion_destination_inline_keyboard(user_language):
    pico_second_symbol_button = types.InlineKeyboardButton(
        text=f"ps {languages[user_language]['pico_second_time_converter']}",
        callback_data="pico_second_time_conversion_destination")

    nano_second_symbol_button = types.InlineKeyboardButton(
        text=f"ns {languages[user_language]['nano_second_time_converter']}",
        callback_data="nano_second_time_conversion_destination")

    micro_second_symbol_button = types.InlineKeyboardButton(
        text=f"μs {languages[user_language]['micro_second_time_converter']}",
        callback_data="micro_second_time_conversion_destination")

    milli_second_symbol_button = types.InlineKeyboardButton(
        text=f"ms {languages[user_language]['milli_second_time_converter']}",
        callback_data="milli_second_time_conversion_destination")

    second_symbol_button = types.InlineKeyboardButton(text=f"s {languages[user_language]['second_time_converter']}",
                                                      callback_data="second_time_conversion_destination")

    min_symbol_button = types.InlineKeyboardButton(text=f"min {languages[user_language]['min_time_converter']}",
                                                   callback_data="min_time_conversion_destination")

    hour_symbol_button = types.InlineKeyboardButton(text=f"h {languages[user_language]['hour_time_converter']}",
                                                    callback_data="hour_time_conversion_destination")

    day_symbol_button = types.InlineKeyboardButton(text=f"d {languages[user_language]['day_time_converter']}",
                                                   callback_data="day_time_conversion_destination")

    month_symbol_button = types.InlineKeyboardButton(text=f"mo {languages[user_language]['month_time_converter']}",
                                                     callback_data="month_time_conversion_destination")

    year_symbol_button = types.InlineKeyboardButton(text=f"y {languages[user_language]['year_time_converter']}",
                                                    callback_data="year_time_conversion_destination")

    decade_symbol_button = types.InlineKeyboardButton(text=f"dec {languages[user_language]['decade_time_converter']}",
                                                      callback_data="decade_time_conversion_destination")

    century_symbol_button = types.InlineKeyboardButton(
        text=f"cent {languages[user_language]['century_time_converter']}",
        callback_data="century_time_conversion_destination")

    time_conversion_destination_inline_keyboard = types.InlineKeyboardMarkup(row_width=3).add(pico_second_symbol_button,
                                                                                              nano_second_symbol_button,
                                                                                              micro_second_symbol_button,
                                                                                              milli_second_symbol_button,
                                                                                              second_symbol_button,
                                                                                              min_symbol_button,
                                                                                              hour_symbol_button,
                                                                                              day_symbol_button,
                                                                                              month_symbol_button,
                                                                                              year_symbol_button,
                                                                                              decade_symbol_button,
                                                                                              century_symbol_button)

    return time_conversion_destination_inline_keyboard


def numeral_conversion_numbers_inline_keyboard():
    padding = 19

    numeral_converter__0_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "0".center(padding)),
                                                             callback_data="0_numeral_converter")
    numeral_converter__1_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "1".center(padding)),
                                                             callback_data="1_numeral_converter")
    numeral_converter__2_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "2".center(padding)),
                                                             callback_data="2_numeral_converter")
    numeral_converter__3_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "3".center(padding)),
                                                             callback_data="3_numeral_converter")
    numeral_converter__4_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "4".center(padding)),
                                                             callback_data="4_numeral_converter")
    numeral_converter__5_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "5".center(padding)),
                                                             callback_data="5_numeral_converter")
    numeral_converter__6_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "6".center(padding)),
                                                             callback_data="6_numeral_converter")
    numeral_converter__7_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "7".center(padding)),
                                                             callback_data="7_numeral_converter")
    numeral_converter__8_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "8".center(padding)),
                                                             callback_data="8_numeral_converter")
    numeral_converter__9_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "9".center(padding)),
                                                             callback_data="9_numeral_converter")

    numeral_converter__A_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "A".center(padding)),
                                                             callback_data="a_numeral_converter")
    numeral_converter__B_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "B".center(padding)),
                                                             callback_data="b_numeral_converter")
    numeral_converter__C_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "C".center(padding)),
                                                             callback_data="c_numeral_converter")
    numeral_converter__D_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "D".center(padding)),
                                                             callback_data="d_numeral_converter")
    numeral_converter__E_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "E".center(padding)),
                                                             callback_data="e_numeral_converter")
    numeral_converter__F_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "F".center(padding)),
                                                             callback_data="f_numeral_converter")
    numeral_converter__G_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "G".center(padding)),
                                                             callback_data="g_numeral_converter")
    numeral_converter__H_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "H".center(padding)),
                                                             callback_data="h_numeral_converter")
    numeral_converter__I_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "I".center(padding)),
                                                             callback_data="i_numeral_converter")
    numeral_converter__J_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "J".center(padding)),
                                                             callback_data="j_numeral_converter")
    numeral_converter__K_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "K".center(padding)),
                                                             callback_data="k_numeral_converter")
    numeral_converter__L_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "L".center(padding)),
                                                             callback_data="l_numeral_converter")
    numeral_converter__M_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "M".center(padding)),
                                                             callback_data="m_numeral_converter")
    numeral_converter__N_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "N".center(padding)),
                                                             callback_data="n_numeral_converter")
    numeral_converter__O_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "O".center(padding)),
                                                             callback_data="o_numeral_converter")
    numeral_converter__P_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "P".center(padding)),
                                                             callback_data="p_numeral_converter")
    numeral_converter__Q_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "Q".center(padding)),
                                                             callback_data="q_numeral_converter")
    numeral_converter__R_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "R".center(padding)),
                                                             callback_data="r_numeral_converter")
    numeral_converter__S_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "S".center(padding)),
                                                             callback_data="s_numeral_converter")
    numeral_converter__T_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "T".center(padding)),
                                                             callback_data="t_numeral_converter")
    numeral_converter__U_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "U".center(padding)),
                                                             callback_data="u_numeral_converter")
    numeral_converter__V_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "V".center(padding)),
                                                             callback_data="v_numeral_converter")
    numeral_converter__W_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "W".center(padding)),
                                                             callback_data="w_numeral_converter")
    numeral_converter__X_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "X".center(padding)),
                                                             callback_data="x_numeral_converter")
    numeral_converter__Y_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "Y".center(padding)),
                                                             callback_data="y_numeral_converter")
    numeral_converter__Z_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "Z".center(padding)),
                                                             callback_data="z_numeral_converter")

    numeral_converter__dot_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', ".".center(padding)),
                                                               callback_data="dot_numeral_converter")
    numeral_converter__clear_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "C".center(padding)),
        callback_data="clear_numeral_converter")

    numeral_converter__backward_button = types.InlineKeyboardButton(
        text=unicodedata.normalize('NFKC', "«".center(padding)),
        callback_data="backward_numeral_converter")

    numeral_converter__done_button = types.InlineKeyboardButton(text=unicodedata.normalize('NFKC', "✅".center(padding)),
                                                                callback_data="done_numeral_converter")

    numeral_conversion_numbers_inline_keyboard = types.InlineKeyboardMarkup(row_width=4).add(
        numeral_converter__1_button, numeral_converter__2_button, numeral_converter__3_button).add(
        numeral_converter__4_button, numeral_converter__5_button, numeral_converter__6_button).add(
        numeral_converter__7_button, numeral_converter__8_button, numeral_converter__9_button).add(
        numeral_converter__dot_button, numeral_converter__0_button).add(numeral_converter__A_button,
                                                                        numeral_converter__B_button,
                                                                        numeral_converter__C_button,
                                                                        numeral_converter__D_button,
                                                                        numeral_converter__E_button,
                                                                        numeral_converter__F_button,
                                                                        numeral_converter__G_button,
                                                                        numeral_converter__H_button,
                                                                        numeral_converter__I_button,
                                                                        numeral_converter__J_button,
                                                                        numeral_converter__K_button,
                                                                        numeral_converter__L_button,
                                                                        numeral_converter__M_button,
                                                                        numeral_converter__N_button,
                                                                        numeral_converter__O_button,
                                                                        numeral_converter__P_button,
                                                                        numeral_converter__Q_button,
                                                                        numeral_converter__R_button,
                                                                        numeral_converter__S_button,
                                                                        numeral_converter__T_button,
                                                                        numeral_converter__U_button,
                                                                        numeral_converter__V_button,
                                                                        numeral_converter__W_button,
                                                                        numeral_converter__X_button,
                                                                        numeral_converter__Y_button,
                                                                        numeral_converter__Z_button).add(
        numeral_converter__backward_button, numeral_converter__clear_button, numeral_converter__done_button)

    return numeral_conversion_numbers_inline_keyboard


def numeral_conversion_from_base_inline_keyboard():
    from_base_2 = types.InlineKeyboardButton(text="2", callback_data="2_from_base")
    from_base_3 = types.InlineKeyboardButton(text="3", callback_data="3_from_base")
    from_base_4 = types.InlineKeyboardButton(text="4", callback_data="4_from_base")
    from_base_5 = types.InlineKeyboardButton(text="5", callback_data="5_from_base")
    from_base_6 = types.InlineKeyboardButton(text="6", callback_data="6_from_base")
    from_base_7 = types.InlineKeyboardButton(text="7", callback_data="7_from_base")
    from_base_8 = types.InlineKeyboardButton(text="8", callback_data="8_from_base")
    from_base_9 = types.InlineKeyboardButton(text="9", callback_data="9_from_base")
    from_base_10 = types.InlineKeyboardButton(text="10", callback_data="10_from_base")
    from_base_11 = types.InlineKeyboardButton(text="11", callback_data="11_from_base")
    from_base_12 = types.InlineKeyboardButton(text="12", callback_data="12_from_base")
    from_base_13 = types.InlineKeyboardButton(text="13", callback_data="13_from_base")
    from_base_14 = types.InlineKeyboardButton(text="14", callback_data="14_from_base")
    from_base_15 = types.InlineKeyboardButton(text="15", callback_data="15_from_base")
    from_base_16 = types.InlineKeyboardButton(text="16", callback_data="16_from_base")
    from_base_17 = types.InlineKeyboardButton(text="17", callback_data="17_from_base")
    from_base_18 = types.InlineKeyboardButton(text="18", callback_data="18_from_base")
    from_base_19 = types.InlineKeyboardButton(text="19", callback_data="19_from_base")
    from_base_20 = types.InlineKeyboardButton(text="20", callback_data="20_from_base")
    from_base_21 = types.InlineKeyboardButton(text="21", callback_data="21_from_base")
    from_base_22 = types.InlineKeyboardButton(text="22", callback_data="22_from_base")
    from_base_23 = types.InlineKeyboardButton(text="23", callback_data="23_from_base")
    from_base_24 = types.InlineKeyboardButton(text="24", callback_data="24_from_base")
    from_base_25 = types.InlineKeyboardButton(text="25", callback_data="25_from_base")
    from_base_26 = types.InlineKeyboardButton(text="26", callback_data="26_from_base")
    from_base_27 = types.InlineKeyboardButton(text="27", callback_data="27_from_base")
    from_base_28 = types.InlineKeyboardButton(text="28", callback_data="28_from_base")
    from_base_29 = types.InlineKeyboardButton(text="29", callback_data="29_from_base")
    from_base_30 = types.InlineKeyboardButton(text="30", callback_data="30_from_base")
    from_base_31 = types.InlineKeyboardButton(text="31", callback_data="31_from_base")
    from_base_32 = types.InlineKeyboardButton(text="32", callback_data="32_from_base")
    from_base_33 = types.InlineKeyboardButton(text="33", callback_data="33_from_base")
    from_base_34 = types.InlineKeyboardButton(text="34", callback_data="34_from_base")
    from_base_35 = types.InlineKeyboardButton(text="35", callback_data="35_from_base")
    from_base_36 = types.InlineKeyboardButton(text="36", callback_data="36_from_base")
    from_base_inline_keyboard = types.InlineKeyboardMarkup(row_width=5).add(from_base_2, from_base_3, from_base_4,
                                                                            from_base_5, from_base_6, from_base_7,
                                                                            from_base_8,
                                                                            from_base_9, from_base_10, from_base_11,
                                                                            from_base_12, from_base_13, from_base_14,
                                                                            from_base_15,
                                                                            from_base_16, from_base_17, from_base_18,
                                                                            from_base_19, from_base_20, from_base_21,
                                                                            from_base_22,
                                                                            from_base_23, from_base_24, from_base_25,
                                                                            from_base_26, from_base_27, from_base_28,
                                                                            from_base_29,
                                                                            from_base_30, from_base_31, from_base_32,
                                                                            from_base_33, from_base_34, from_base_35,
                                                                            from_base_36)

    return from_base_inline_keyboard


def numeral_conversion_to_base_inline_keyboard():
    to_base_2 = types.InlineKeyboardButton(text="2", callback_data="2_to_base")
    to_base_3 = types.InlineKeyboardButton(text="3", callback_data="3_to_base")
    to_base_4 = types.InlineKeyboardButton(text="4", callback_data="4_to_base")
    to_base_5 = types.InlineKeyboardButton(text="5", callback_data="5_to_base")
    to_base_6 = types.InlineKeyboardButton(text="6", callback_data="6_to_base")
    to_base_7 = types.InlineKeyboardButton(text="7", callback_data="7_to_base")
    to_base_8 = types.InlineKeyboardButton(text="8", callback_data="8_to_base")
    to_base_9 = types.InlineKeyboardButton(text="9", callback_data="9_to_base")
    to_base_10 = types.InlineKeyboardButton(text="10", callback_data="10_to_base")
    to_base_11 = types.InlineKeyboardButton(text="11", callback_data="11_to_base")
    to_base_12 = types.InlineKeyboardButton(text="12", callback_data="12_to_base")
    to_base_13 = types.InlineKeyboardButton(text="13", callback_data="13_to_base")
    to_base_14 = types.InlineKeyboardButton(text="14", callback_data="14_to_base")
    to_base_15 = types.InlineKeyboardButton(text="15", callback_data="15_to_base")
    to_base_16 = types.InlineKeyboardButton(text="16", callback_data="16_to_base")
    to_base_17 = types.InlineKeyboardButton(text="17", callback_data="17_to_base")
    to_base_18 = types.InlineKeyboardButton(text="18", callback_data="18_to_base")
    to_base_19 = types.InlineKeyboardButton(text="19", callback_data="19_to_base")
    to_base_20 = types.InlineKeyboardButton(text="20", callback_data="20_to_base")
    to_base_21 = types.InlineKeyboardButton(text="21", callback_data="21_to_base")
    to_base_22 = types.InlineKeyboardButton(text="22", callback_data="22_to_base")
    to_base_23 = types.InlineKeyboardButton(text="23", callback_data="23_to_base")
    to_base_24 = types.InlineKeyboardButton(text="24", callback_data="24_to_base")
    to_base_25 = types.InlineKeyboardButton(text="25", callback_data="25_to_base")
    to_base_26 = types.InlineKeyboardButton(text="26", callback_data="26_to_base")
    to_base_27 = types.InlineKeyboardButton(text="27", callback_data="27_to_base")
    to_base_28 = types.InlineKeyboardButton(text="28", callback_data="28_to_base")
    to_base_29 = types.InlineKeyboardButton(text="29", callback_data="29_to_base")
    to_base_30 = types.InlineKeyboardButton(text="30", callback_data="30_to_base")
    to_base_31 = types.InlineKeyboardButton(text="31", callback_data="31_to_base")
    to_base_32 = types.InlineKeyboardButton(text="32", callback_data="32_to_base")
    to_base_33 = types.InlineKeyboardButton(text="33", callback_data="33_to_base")
    to_base_34 = types.InlineKeyboardButton(text="34", callback_data="34_to_base")
    to_base_35 = types.InlineKeyboardButton(text="35", callback_data="35_to_base")
    to_base_36 = types.InlineKeyboardButton(text="36", callback_data="36_to_base")
    to_base_inline_keyboard = types.InlineKeyboardMarkup(row_width=5).add(to_base_2, to_base_3, to_base_4, to_base_5,
                                                                          to_base_6, to_base_7, to_base_8,
                                                                          to_base_9, to_base_10, to_base_11, to_base_12,
                                                                          to_base_13, to_base_14,
                                                                          to_base_15,
                                                                          to_base_16, to_base_17, to_base_18,
                                                                          to_base_19, to_base_20, to_base_21,
                                                                          to_base_22,
                                                                          to_base_23, to_base_24, to_base_25,
                                                                          to_base_26, to_base_27, to_base_28,
                                                                          to_base_29,
                                                                          to_base_30, to_base_31, to_base_32,
                                                                          to_base_33, to_base_34, to_base_35,
                                                                          to_base_36)

    return to_base_inline_keyboard


def settings__options_keyboard(user_language):
    settings__language_option_button = languages[user_language]['language_option_selection']
    settings__back_option_button = languages[user_language]['back_option_selection']
    settings__options_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    settings__options_keyboard.add(settings__language_option_button).add(settings__back_option_button)

    return settings__options_keyboard


def languages_inline_keyboard():
    english_button = types.InlineKeyboardButton(text="English", callback_data="language_english")
    persian_button = types.InlineKeyboardButton(text="Persian", callback_data="language_persian")

    languages_inline_keyboard = types.InlineKeyboardMarkup(row_width=2).add(english_button, persian_button)

    return languages_inline_keyboard


all_keyboards_list = ["Calculation", "BMI", "Settings", "⬅️ Back ⬅️", "Calculator", "Unit Conversion", "Data",
                      "currency", "Length", "Mass", "Numeral", "Temperature", "Time"]

bmi_conversion_weight_callback_data_list = ["0_weight_bmi", "1_weight_bmi", "2_weight_bmi", "3_weight_bmi",
                                            "4_weight_bmi", "5_weight_bmi", "6_weight_bmi", "7_weight_bmi",
                                            "8_weight_bmi", "9_weight_bmi", "dot_weight_bmi", "backward_weight_bmi",
                                            "clear_weight_bmi", "kilogram_weight_bmi", "gram_weight_bmi",
                                            "done_weight_bmi"]

bmi_conversion_height_callback_data_list = ["0_height_bmi", "1_height_bmi", "2_height_bmi", "3_height_bmi",
                                            "4_height_bmi", "5_height_bmi", "6_height_bmi", "7_height_bmi",
                                            "8_height_bmi", "9_height_bmi", "dot_height_bmi", "backward_height_bmi",
                                            "clear_height_bmi", "meter_height_bmi", "centi_meter_height_bmi",
                                            "done_height_bmi"]

bmi__conversion_see_bmi_chart_callback_data_list = ["see_chart_bmi"]

date__calender_callback_data_list = ["gregorian_calender", "jalali_calender"]

date_conversion_callback_date_list = ["jalali_to_gregorian", "gregorian_to_jalali", "0_date_conversion_day",
                                      "1_date_conversion_day", "2_date_conversion_day",
                                      "3_date_conversion_day", "4_date_conversion_day", "5_date_conversion_day",
                                      "6_date_conversion_day", "7_date_conversion_day", "8_date_conversion_day",
                                      "9_date_conversion_day", "backward_date_conversion_day",
                                      "clear_date_conversion_day", "done_date_conversion_day",
                                      "0_date_conversion_month", "1_date_conversion_month", "2_date_conversion_month",
                                      "3_date_conversion_month", "4_date_conversion_month", "5_date_conversion_month",
                                      "6_date_conversion_month", "7_date_conversion_month", "8_date_conversion_month",
                                      "9_date_conversion_month", "backward_date_conversion_month",
                                      "clear_date_conversion_month", "done_date_conversion_month",
                                      "0_date_conversion_year", "1_date_conversion_year", "2_date_conversion_year",
                                      "3_date_conversion_year", "4_date_conversion_year", "5_date_conversion_year",
                                      "6_date_conversion_year", "7_date_conversion_year", "8_date_conversion_year",
                                      "9_date_conversion_year", "backward_date_conversion_year",
                                      "clear_date_conversion_year", "done_date_conversion_year"]

currency_callback_date_list = ["0_currency_converter", "1_currency_converter", "2_currency_converter",
                               "3_currency_converter", "4_currency_converter", "5_currency_converter",
                               "6_currency_converter", "7_currency_converter", "8_currency_converter",
                               "9_currency_converter", "dot_currency_converter", "clear_currency_converter",
                               "backward_currency_converter", "done_currency_converter",
                               "dollar_currency_conversion_starter", "tooman_currency_conversion_starter",
                               "euro_currency_conversion_starter", "pound_currency_conversion_starter",
                               "swiss_franc_currency_conversion_starter", "lir_currency_conversion_starter",
                               "dirham_currency_conversion_starter", "dollar_currency_conversion_destination",
                               "tooman_currency_conversion_destination", "euro_currency_conversion_destination",
                               "pound_currency_conversion_destination", "swiss_franc_currency_conversion_destination",
                               "lir_currency_conversion_destination", "dirham_currency_conversion_destination"]

calculator_callback_data_list = ["0_calculator", "1_calculator", "2_calculator", "3_calculator", "4_calculator",
                                 "5_calculator", "6_calculator", "7_calculator", "8_calculator", "9_calculator",
                                 "dot_calculator", "plus_calculator", "mines_calculator", "times_calculator",
                                 "fraction_calculator", "sin_calculator", "cos_calculator", "tan_calculator",
                                 "cot_calculator", "pi_calculator", "opening_parentheses_calculator",
                                 "closing_parentheses_calculator", "factorial_calculator", "power_calculator",
                                 "sqrt_calculator", "log_calculator", "backward_calculator", "clear_calculator",
                                 "neg_or_pos_maker_calculator", "done_calculator"]

languages_callback_data_list = ["language_english", "language_persian"]

data_conversion_callback_data_list = ["0_data_converter", "1_data_converter", "2_data_converter", "3_data_converter",
                                      "4_data_converter", "5_data_converter", "6_data_converter", "7_data_converter",
                                      "8_data_converter", "9_data_converter", "dot_data_converter",
                                      "clear_data_converter", "backward_data_converter", "done_data_converter",
                                      "bit_data_conversion_starter", "byte_data_conversion_starter",
                                      "kilo_byte_data_conversion_starter", "mega_byte_data_conversion_starter",
                                      "giga_byte_data_conversion_starter", "tera_byte_data_conversion_starter",
                                      "peta_byte_data_conversion_starter", "exa_byte_data_conversion_starter",
                                      "bit_data_conversion_destination", "byte_data_conversion_destination",
                                      "kilo_byte_data_conversion_destination", "mega_byte_data_conversion_destination",
                                      "giga_byte_data_conversion_destination", "tera_byte_data_conversion_destination",
                                      "peta_byte_data_conversion_destination", "exa_byte_data_conversion_destination"]

length_conversion_callback_data_list = ["0_length_converter", "1_length_converter", "2_length_converter",
                                        "3_length_converter", "4_length_converter", "5_length_converter",
                                        "6_length_converter", "7_length_converter", "8_length_converter",
                                        "9_length_converter", "0_length_converter", "dot_length_converter",
                                        "backward_length_converter", "clear_length_converter", "done_length_converter",
                                        "pico_meter_length_conversion_starter", "nano_meter_length_conversion_starter",
                                        "micro_meter_length_conversion_starter",
                                        "milli_meter_length_conversion_starter",
                                        "centi_meter_length_conversion_starter", "desi_meter_length_conversion_starter",
                                        "meter_length_conversion_starter", "kilo_meter_length_conversion_starter",
                                        "mile_length_conversion_starter", "nautical_mile_length_conversion_starter",
                                        "foot_length_conversion_starter", "inch_length_conversion_starter",
                                        "yard_length_conversion_starter", "fathom_length_conversion_starter",
                                        "light_year_length_conversion_starter",
                                        "pico_meter_length_conversion_destination",
                                        "nano_meter_length_conversion_destination",
                                        "micro_meter_length_conversion_destination",
                                        "milli_meter_length_conversion_destination",
                                        "centi_meter_length_conversion_destination",
                                        "desi_meter_length_conversion_destination",
                                        "meter_length_conversion_destination",
                                        "kilo_meter_length_conversion_destination",
                                        "mile_length_conversion_destination",
                                        "nautical_mile_length_conversion_destination",
                                        "foot_length_conversion_destination", "inch_length_conversion_destination",
                                        "yard_length_conversion_destination", "fathom_length_conversion_destination",
                                        "light_year_length_conversion_destination"]

mass_conversion_callback_data_list = ["0_mass_converter", "1_mass_converter", "2_mass_converter", "3_mass_converter",
                                      "4_mass_converter", "5_mass_converter", "6_mass_converter", "7_mass_converter",
                                      "8_mass_converter", "9_mass_converter", "dot_mass_converter",
                                      "clear_mass_converter", "backward_mass_converter", "done_mass_converter",
                                      "nano_gram_mass_conversion_starter", "micro_gram_mass_conversion_starter",
                                      "quintal_mass_conversion_starter", "milli_gram_mass_conversion_starter",
                                      "centi_gram_mass_conversion_starter", "desi_gram_mass_conversion_starter",
                                      "gram_mass_conversion_starter", "kilo_gram_mass_conversion_starter",
                                      "tone_mass_conversion_starter", "pound_mass_conversion_starter",
                                      "ounce_mass_conversion_starter", "carat_mass_conversion_starter",
                                      "grain_mass_conversion_starter", "long_ton_mass_conversion_starter",
                                      "short_ton_mass_conversion_starter", "stone_mass_conversion_starter",
                                      "dram_mass_conversion_starter", "sir_mass_conversion_starter",
                                      "nano_gram_mass_conversion_destination", "micro_gram_mass_conversion_destination",
                                      "quintal_mass_conversion_destination", "milli_gram_mass_conversion_destination",
                                      "centi_gram_mass_conversion_destination", "desi_gram_mass_conversion_destination",
                                      "gram_mass_conversion_destination", "kilo_gram_mass_conversion_destination",
                                      "tone_mass_conversion_destination", "pound_mass_conversion_destination",
                                      "ounce_mass_conversion_destination", "carat_mass_conversion_destination",
                                      "grain_mass_conversion_destination", "long_ton_mass_conversion_destination",
                                      "short_ton_mass_conversion_destination", "stone_mass_conversion_destination",
                                      "dram_mass_conversion_destination", "sir_mass_conversion_destination"]

numeral_conversion_callback_data_list = ["0_numeral_converter", "1_numeral_converter", "2_numeral_converter",
                                         "3_numeral_converter", "4_numeral_converter", "5_numeral_converter",
                                         "6_numeral_converter", "7_numeral_converter", "8_numeral_converter",
                                         "9_numeral_converter", "a_numeral_converter", "b_numeral_converter",
                                         "c_numeral_converter", "d_numeral_converter", "e_numeral_converter",
                                         "f_numeral_converter", "g_numeral_converter", "h_numeral_converter",
                                         "i_numeral_converter", "j_numeral_converter", "k_numeral_converter",
                                         "l_numeral_converter", "m_numeral_converter", "n_numeral_converter",
                                         "o_numeral_converter", "p_numeral_converter", "q_numeral_converter",
                                         "r_numeral_converter", "s_numeral_converter", "t_numeral_converter",
                                         "u_numeral_converter", "v_numeral_converter", "w_numeral_converter",
                                         "x_numeral_converter", "y_numeral_converter", "z_numeral_converter",
                                         "dot_numeral_converter", "clear_numeral_converter",
                                         "backward_numeral_converter", "done_numeral_converter", "2_from_base",
                                         "3_from_base", "4_from_base", "5_from_base", "6_from_base", "7_from_base",
                                         "8_from_base", "9_from_base", "10_from_base", "11_from_base", "12_from_base",
                                         "13_from_base", "14_from_base", "15_from_base", "16_from_base", "17_from_base",
                                         "18_from_base", "19_from_base", "20_from_base", "21_from_base", "22_from_base",
                                         "23_from_base", "24_from_base", "25_from_base", "26_from_base", "27_from_base",
                                         "28_from_base", "29_from_base", "30_from_base", "31_from_base", "32_from_base",
                                         "33_from_base", "34_from_base", "35_from_base", "36_from_base", "2_to_base",
                                         "3_to_base", "4_to_base", "5_to_base", "6_to_base", "7_to_base", "8_to_base",
                                         "9_to_base", "10_to_base", "11_to_base", "12_to_base", "13_to_base",
                                         "14_to_base", "15_to_base", "16_to_base", "17_to_base", "18_to_base",
                                         "19_to_base", "20_to_base", "21_to_base", "22_to_base", "23_to_base",
                                         "24_to_base", "25_to_base", "26_to_base", "27_to_base", "28_to_base",
                                         "29_to_base", "30_to_base", "31_to_base", "32_to_base", "33_to_base",
                                         "34_to_base", "35_to_base", "36_to_base"]

temperature_conversion_callback_data_list = ["0_temperature_converter", "1_temperature_converter",
                                             "2_temperature_converter", "3_temperature_converter",
                                             "4_temperature_converter", "5_temperature_converter",
                                             "6_temperature_converter", "7_temperature_converter",
                                             "8_temperature_converter", "9_temperature_converter",
                                             "dot_temperature_converter", "clear_temperature_converter",
                                             "backward_temperature_converter", "done_temperature_converter",
                                             "neg_or_pos_maker_temperature_converter",
                                             "celsius_temperature_conversion_starter",
                                             "fahrenheit_temperature_conversion_starter",
                                             "kelvin_temperature_conversion_starter",
                                             "celsius_temperature_conversion_destination",
                                             "fahrenheit_temperature_conversion_destination",
                                             "kelvin_temperature_conversion_destination"]

time_conversion_callback_data_list = ["0_time_converter", "1_time_converter", "2_time_converter", "3_time_converter",
                                      "4_time_converter", "5_time_converter", "6_time_converter", "7_time_converter",
                                      "8_time_converter", "9_time_converter", "dot_time_converter",
                                      "clear_time_converter", "backward_time_converter", "done_time_converter",
                                      "pico_second_time_conversion_starter", "nano_second_time_conversion_starter",
                                      "micro_second_time_conversion_starter", "milli_second_time_conversion_starter",
                                      "second_time_conversion_starter", "min_time_conversion_starter",
                                      "hour_time_conversion_starter", "day_time_conversion_starter",
                                      "month_time_conversion_starter", "year_time_conversion_starter",
                                      "decade_time_conversion_starter", "century_time_conversion_starter",
                                      "pico_second_time_conversion_destination",
                                      "nano_second_time_conversion_destination",
                                      "micro_second_time_conversion_destination",
                                      "milli_second_time_conversion_destination", "second_time_conversion_destination",
                                      "min_time_conversion_destination", "hour_time_conversion_destination",
                                      "day_time_conversion_destination", "month_time_conversion_destination",
                                      "year_time_conversion_destination", "decade_time_conversion_destination",
                                      "century_time_conversion_destination"]
