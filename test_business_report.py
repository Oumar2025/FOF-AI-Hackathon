from pprint import pprint

from services.business_intelligence_service import (
    BusinessIntelligenceService
)

report = BusinessIntelligenceService.generate_business_report()

pprint(report)