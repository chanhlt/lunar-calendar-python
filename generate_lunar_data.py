# pylint: disable=missing-module-docstring
import datetime
import json
from lunardate import LunarDate

data = {}

for year in range(1900, 2101):
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                g_date = datetime.date(year, month, day)
                lunar = LunarDate.fromSolarDate(year, month, day)
                data[str(g_date)] = {
                    "lunar_year": lunar.year,
                    "lunar_month": lunar.month,
                    "lunar_day": lunar.day,
                    "is_leap_month": lunar.isLeapMonth
                }
            except ValueError:
                continue  # skip invalid dates

with open("lunar_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
