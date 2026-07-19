from services.business_intelligence_service import BusinessIntelligenceService

summary = BusinessIntelligenceService.get_inventory_summary()

print(summary)