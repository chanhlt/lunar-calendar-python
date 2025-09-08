# pylint: disable=missing-module-docstring,line-too-long
import datetime
import sqlite3
from lunardate import LunarDate

# Connect to (or create) the database
conn = sqlite3.connect("lunar_calendar.db")
cur = conn.cursor()

# Create the table if it doesn’t exist
cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    solar_day INTEGER,
    solar_month INTEGER,
    lunar_month INTEGER,
    lunar_day INTEGER,
    start_hour INTEGER,
    end_hour INTEGER,
    start_minute INTEGER,
    end_minute INTEGER,
    is_all_day INTEGER NOT NULL
)
""")

# Create the table if it doesn’t exist
cur.execute("""
CREATE TABLE IF NOT EXISTS lunar_dates (
    solar_date TEXT PRIMARY KEY,
    lunar_year INTEGER NOT NULL,
    lunar_month INTEGER NOT NULL,
    lunar_day INTEGER NOT NULL,
    is_leap_month INTEGER NOT NULL
)
""")

# Indexes for common reverse lookups
cur.execute("CREATE INDEX IF NOT EXISTS idx_lunar_year ON lunar_dates (lunar_year)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_lunar_year_month ON lunar_dates (lunar_year, lunar_month)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_is_leap_month ON lunar_dates (is_leap_month)")

# Prepare insert statement
INSERT_SQL = """
INSERT OR REPLACE INTO lunar_dates
(solar_date, lunar_year, lunar_month, lunar_day, is_leap_month)
VALUES (?, ?, ?, ?, ?)
"""

# Loop through Gregorian dates and compute lunar dates
for year in range(1900, 2101):
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                g_date = datetime.date(year, month, day)
                lunar = LunarDate.fromSolarDate(year, month, day)
                cur.execute(INSERT_SQL, (
                    str(g_date),
                    lunar.year,
                    lunar.month,
                    lunar.day,
                    int(lunar.isLeapMonth)  # store as 0/1
                ))
            except ValueError:
                continue  # skip invalid dates

# Commit and close
conn.commit()
conn.close()
