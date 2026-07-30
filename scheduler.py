from services.alert_service import AlertService

print("FOF-AI Scheduler Started...")

AlertService.process_alerts()

print("Alert check completed.")