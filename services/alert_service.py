import sqlite3
from datetime import datetime

from services.product_service import ProductService

from services.notification_service import NotificationService

from config.settings import DATABASE_NAME


class AlertService:

    @staticmethod
    def has_alert_been_sent(product_id, alert_level):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM alert_history
            WHERE product_id = ?
            AND alert_level = ?
        """, (product_id, alert_level))

        count = cursor.fetchone()[0]

        conn.close()

        return count > 0
    
    @staticmethod
    def save_alert(product_id, alert_level):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO alert_history
            (
                product_id,
                alert_level,
                sent_at
            )
            VALUES (?, ?, ?)
        """, (
            product_id,
            alert_level,
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def process_alerts():

        products = ProductService.get_all_products()

        today = datetime.now().date()

        for product in products:

            product_id = product[0]
            product_name = product[1]
            category = product[2]
            quantity = product[6]
            unit = product[7]
            expiry_date = product[11]

            expiry = datetime.strptime(
                expiry_date,
                "%Y-%m-%d"
            ).date()

            days_left = (expiry - today).days

            # Ignore expired products
            if days_left < 0:
                continue

            # Determine alert level
            alert_level = None

            if days_left <= 1:
                alert_level = 1
            elif days_left <= 3:
                alert_level = 3
            elif days_left <= 7:
                alert_level = 7
            elif days_left <= 15:
                alert_level = 15
            elif days_left <= 30:
                alert_level = 30

            if alert_level is None:
                continue

            # Skip duplicate alerts
            if AlertService.has_alert_been_sent(product_id, alert_level):
                continue

            subject = f"⚠️ FOF-AI Alert: {product_name}"

            message = f"""
    Product: {product_name}

    Category: {category}

    Current Stock: {quantity} {unit}

    Expiry Date: {expiry_date}

    Days Remaining: {days_left}

    Alert Level: {alert_level}-Day Alert

    Generated automatically by FOF-AI.
    """

            NotificationService.send_email(
                subject,
                message
            )

            AlertService.save_alert(
                product_id,
                alert_level
            )

    @staticmethod
    def get_active_alerts():

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                ah.alert_id,
                p.product_id,
                p.product_name,
                p.category,
                p.quantity,
                p.unit,
                p.expiry_date,
                ah.alert_level,
                ah.sent_at,
                ah.acknowledged,
                ah.muted,
                ah.resolved

            FROM alert_history ah

            JOIN products p
                ON ah.product_id = p.product_id

            WHERE ah.resolved = 0

            ORDER BY p.expiry_date ASC
        """)

        alerts = cursor.fetchall()

        conn.close()

        return alerts              
    
    @staticmethod
    def acknowledge_alert(alert_id):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE alert_history
            SET acknowledged = 1
            WHERE alert_id = ?
        """, (alert_id,))

        conn.commit()
        conn.close()

    @staticmethod
    def mute_alert(alert_id):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE alert_history
            SET muted = 1
            WHERE alert_id = ?
        """, (alert_id,))

        conn.commit()
        conn.close()    

    @staticmethod
    def resolve_alert(alert_id):

        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE alert_history
            SET resolved = 1
            WHERE alert_id = ?
        """, (alert_id,))

        conn.commit()
        conn.close()    