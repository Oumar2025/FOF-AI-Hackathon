import schedule
import threading
import time

from services.alert_service import AlertService


class SchedulerService:

    @staticmethod
    def start():

        # Run every day at 08:00
        schedule.every(30).seconds.do(
            AlertService.process_alerts
        )

        def run_scheduler():

            while True:
                schedule.run_pending()
                time.sleep(30)

        thread = threading.Thread(
            target=run_scheduler,
            daemon=True
        )

        thread.start()

        print("✅ Alert Scheduler Started")