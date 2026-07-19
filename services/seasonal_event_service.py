import sqlite3
from config.settings import DATABASE_NAME


class SeasonalEventService:

    @staticmethod
    def add_event(category, event, start_date, end_date, multiplier):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO seasonal_events
            (category, event, start_date, end_date, demand_multiplier)
            VALUES (?, ?, ?, ?, ?)
        """, (
            category,
            event,
            start_date,
            end_date,
            multiplier
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_events():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM seasonal_events
            ORDER BY start_date
        """)

        events = cursor.fetchall()

        conn.close()

        return events

    @staticmethod
    def delete_all_events():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM seasonal_events")

        conn.commit()
        conn.close()

    @staticmethod
    def seed_default_events():

        SeasonalEventService.delete_all_events()

        events = [

            ("Dates", "Ramadan", "2026-02-17", "2026-03-19", 2.50),

            ("Chocolate", "Christmas", "2026-12-01", "2026-12-25", 1.80),

            ("Candy", "Eid al-Fitr", "2026-03-20", "2026-03-25", 1.60),

            ("Biscuit", "Back to School", "2026-08-15", "2026-09-10", 1.40)

        ]

        for event in events:
            SeasonalEventService.add_event(*event)