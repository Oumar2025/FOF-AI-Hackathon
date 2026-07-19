import sqlite3
import pandas as pd

from config.settings import DATABASE_NAME


def import_seasonal_events():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    df = pd.read_csv("data/seasonal_events.csv")

    cursor.execute("DELETE FROM seasonal_events")

    for _, row in df.iterrows():

        cursor.execute("""
            INSERT INTO seasonal_events
            (
                category,
                event,
                start_date,
                end_date,
                demand_multiplier
            )
            VALUES (?, ?, ?, ?, ?)
        """, (

            row["Category"],
            row["Event"],
            row["StartDate"],
            row["EndDate"],
            row["DemandMultiplier"]

        ))

    conn.commit()
    conn.close()

    print("✅ Seasonal events imported.")


if __name__ == "__main__":

    import_seasonal_events()