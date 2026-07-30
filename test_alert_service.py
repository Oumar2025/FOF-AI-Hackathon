from services.alert_service import AlertService

print(AlertService.has_alert_been_sent(1, 30))

AlertService.save_alert(1, 30)

print(AlertService.has_alert_been_sent(1, 30))