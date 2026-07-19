from pprint import pprint

from services.business_intelligence_service import (
    BusinessIntelligenceService
)

pprint(
    BusinessIntelligenceService.get_forecast_summary()
)