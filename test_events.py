from services.seasonal_event_service import SeasonalEventService

SeasonalEventService.seed_default_events()

events = SeasonalEventService.get_events()

for event in events:
    print(event)