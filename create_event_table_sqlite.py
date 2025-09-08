# pylint: disable=missing-module-docstring,line-too-long
import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("lunar_data.db")
cur = conn.cursor()

# Create the table if it doesn’t exist
cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    solar_day INTEGER,
    solar_month INTEGER,
    lunar_month INTEGER,
    lunar_day INTEGER,
    is_all_day INTEGER NOT NULL
)
""")

conn.commit()
conn.close()
