import jdatetime
from datetime import datetime
import pytz


def current_time_getter(location='Asia/Tehran'):
    time_zone = pytz.timezone(location)
    current_time = datetime.now(time_zone).strftime("%H:%M:%S")

    return current_time


def jalali_getter():
    today = jdatetime.datetime.now()
    year, month, day = today.year, today.month, today.day

    return f"{year}/{month}/{day}"


def gregorian_getter():
    now = datetime.now()
    year, month, day = now.year, now.month, now.day

    return f"{year}/{month}/{day}"


def gregorian_to_jalali(gregorian_date):
    gregorian_date = datetime.strptime(gregorian_date, "%Y/%m/%d")
    year, month, day = gregorian_date.year, gregorian_date.month, gregorian_date.day
    jalali_date = jdatetime.datetime.fromgregorian(date=datetime(year, month, day))
    jalali_date = jalali_date.strftime("%Y/%m/%d")

    return jalali_date


def jalali_to_gregorian(jalali_date):
    jalali_date = jdatetime.date(*map(int, jalali_date.split('/')))
    gregorian_date = jalali_date.togregorian()

    return gregorian_date.strftime("%Y/%m/%d")
