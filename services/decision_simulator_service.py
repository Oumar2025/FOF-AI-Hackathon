from services.forecast_service import ForecastService
from services.gemma_service import GemmaService


class DecisionSimulatorService:

    @staticmethod
    def simulate_import(product, quantity):

        product_name = product[1]

        supplier = product[4]

        current_stock = product[6]

        cost_price = product[8]

        selling_price = product[9]

        expiry_date = product[11]

        forecast = ForecastService.get_next_month_prediction(
            product_name
        )

        if forecast is None:
            forecast = current_stock

        multiplier, event = ForecastService.seasonal_multiplier(
            product[2]
        )

        predicted_demand = round(
            forecast * multiplier
        )
        recommended_quantity = max(
            predicted_demand - current_stock,
            0
        )
        remaining_stock = current_stock + quantity - predicted_demand

        expected_revenue = predicted_demand * selling_price

        expected_profit = predicted_demand * (selling_price - cost_price)

        stock_after_import = current_stock + quantity

        overstock = max(remaining_stock, 0)

        prompt = f"""
You are FOF-AI, an Executive AI Supply Chain Consultant.

Simulate the following import decision.

Product:
{product_name}

Supplier:
{supplier}

Current Stock:
{current_stock}

Planned Import:
{quantity} cartons

AI Recommended Import Quantity:
{recommended_quantity} cartons

Predicted Demand:
{predicted_demand}

Stock After Import:
{stock_after_import}

Remaining Stock:
{remaining_stock}

Expected Revenue:
${expected_revenue:.2f}

Expected Profit:
${expected_profit:.2f}

Potential Overstock:
{overstock} cartons

Cost Price:
{cost_price}

Selling Price:
{selling_price}

Expiry Date:
{expiry_date}

Season:
{event if event else "Normal"}

Instructions:

Analyze this business decision using the inventory data and calculations provided.

Evaluate:

• Inventory impact

• Revenue impact

• Profit impact

• Overstock or shortage risk

• Whether the planned import quantity is appropriate

Compare the user's planned import with the AI recommended quantity.

Explain whether the user should:

- keep the same quantity,
- reduce it,
- or increase it.

Always explain the reason using the business data provided.

Return exactly this format.

## Decision Simulation

• Inventory Impact

• Profit Impact

• Expiry Risk

• Business Advice

## Final Decision

(Recommended / Not Recommended)

## Confidence

Give only one percentage.
"""

        return GemmaService.ask(prompt)