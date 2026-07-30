from services.alert_service import AlertService

alerts = AlertService.get_active_alerts()

print("Active Alerts")

for alert in alerts:
    print(alert)