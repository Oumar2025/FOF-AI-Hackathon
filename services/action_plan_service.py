from services.ai_service import AIService
from services.decision_simulator_service import DecisionSimulatorService
from services.forecast_service import ForecastService
from services.gemma_service import GemmaService


class ActionPlanService:

    @staticmethod
    def generate_action_plan(product):

        analysis = AIService.analyze_product(product)

        recommendation = AIService.import_advisor(product)

        simulation = DecisionSimulatorService.simulate_import(
            product,
            recommendation["recommended_quantity"]
        )

        forecast = ForecastService.get_next_month_prediction(
            product[1]
        )

        if forecast is None:
            forecast = product[6]

        prompt = f"""
You are FOF-AI, the Executive AI Advisor of ETS FOFANA CONFISERIE.

Create a Weekly Business Action Plan.

Business Data

Product: {product[1]}
Category: {product[2]}
Supplier: {product[4]}
Current Stock: {product[6]}
Profit Margin: {analysis['margin']}%
Days Until Expiry: {analysis['days_left']}
Forecast Demand: {forecast}

Current Recommendation:
{analysis['recommendation']}

Import Recommendation:
{recommendation}

Decision Simulation:
{simulation}

Instructions

Think like the CEO of a food importing company.

Prioritize reducing expired products.

Prioritize increasing profit.

Prioritize preventing stock shortages.

Use only the business data provided.

Do not invent numbers.

If no action is required for a section, clearly say so.

Return ONLY the following format.

# Weekly Business Action Plan

🔴 Priority 1
(Action)

Why:
...

Expected Benefit:
...

🟡 Priority 2
(Action)

Why:
...

Expected Benefit:
...

🟢 Priority 3
(Action)

Why:
...

Expected Benefit:
...

# Executive Summary

Write a short summary for the company owner.

# Confidence

One percentage only.
"""

        return GemmaService.ask(prompt)