from datetime import datetime
from services.forecast_service import ForecastService
from services.product_service import ProductService
from services.product_service import ProductService
from services.gemma_service import GemmaService




class AIService:

    @staticmethod
    def analyze_product(product):

        quantity = product[6]

        cost = product[8]

        selling = product[9]

        expiry = product[11]

        # --------------------------
        # Stock Analysis
        # --------------------------

        if quantity < 100:
            stock_status = "🔴 Low Stock"

        elif quantity < 300:
            stock_status = "🟡 Medium Stock"

        else:
            stock_status = "🟢 Healthy Stock"

        # --------------------------
        # Profit Margin
        # --------------------------

        if cost > 0:

            margin = ((selling - cost) / cost) * 100

        else:

            margin = 0

        # --------------------------
        # Expiry Analysis
        # --------------------------

        expiry_date = datetime.strptime(
            expiry,
            "%Y-%m-%d"
        )

        today = datetime.today()

        days_left = (
            expiry_date - today
        ).days

        if days_left <= 30:

            expiry_status = "🔴 Critical"

        elif days_left <= 90:

            expiry_status = "🟡 Warning"

        else:

            expiry_status = "🟢 Safe"

        # --------------------------
        # Recommendation
        # --------------------------

        if quantity < 100:

            recommendation = (
                "Import additional stock soon."
            )

        elif days_left <= 30:

            recommendation = (
                "Launch a promotion before expiry."
            )

        else:

            recommendation = (
                "Inventory is healthy."
            )

        return {

            "stock": stock_status,

            "expiry": expiry_status,

            "margin": round(margin, 2),

            "days_left": days_left,

            "recommendation": recommendation

        }
    
    @staticmethod
    def promotion_advisor(product):

        quantity = product[6]

        expiry_days = AIService.analyze_product(product)["days_left"]

        if expiry_days <= 15:

            return {
                "discount": "25%",
                "priority": "🔴 High",
                "action": "Launch an urgent promotion immediately."
            }

        elif expiry_days <= 30:

            return {
                "discount": "15%",
                "priority": "🟠 Medium",
                "action": "Start a promotional campaign."
            }

        elif quantity > 1000:

            return {
                "discount": "10%",
                "priority": "🟡 Normal",
                "action": "Bundle this product with other products."
            }

        else:

            return {
                "discount": "0%",
                "priority": "🟢 None",
                "action": "No promotion needed."
            }


    @staticmethod
    def import_advisor(product):

        product_name = product[1]
        supplier = product[4]

        current_stock = product[6]

        predicted_demand = ForecastService.get_next_month_prediction(
            product_name
        )

        if predicted_demand is None:

            predicted_demand = current_stock

        multiplier, event = ForecastService.seasonal_multiplier(
            product[2]
        )

        predicted_demand = round(
            predicted_demand * multiplier
        )

        if predicted_demand is None:

            return {
                "supplier": supplier,
                "predicted_demand": 0,
                "recommended_quantity": 0,
                "priority": "Unknown",
                "timing": "No prediction available"
            }

        quantity_to_import = max(
            predicted_demand - current_stock,
            0
        )

        if quantity_to_import > 500:

            priority = "🔴 High"

        elif quantity_to_import > 200:

            priority = "🟠 Medium"

        else:

            priority = "🟢 Low"

        return {

            "supplier": supplier,

            "predicted_demand": predicted_demand,

            "recommended_quantity": quantity_to_import,

            "priority": priority,

            "timing": "Next Import Cycle",
            "event": event

        }
    
    @staticmethod
    def company_advisor(products):

        report = {
            "critical": [],
            "warnings": [],
            "recommendations": [],
            "health": "Excellent"
        }

        low_stock = 0
        expiry = 0

        for product in products:

            analysis = AIService.analyze_product(product)

            if analysis["days_left"] <= 30:
                expiry += 1
                report["critical"].append(
                    f"{product[1]} expires in {analysis['days_left']} days."
                )

            if product[6] < 100:
                low_stock += 1
                report["warnings"].append(
                    f"Import more {product[1]} from {product[4]}."
                )

            if product[6] > 1000:
                report["recommendations"].append(
                    f"Slow imports of {product[1]}."
                )

        if expiry > 3 or low_stock > 5:
            report["health"] = "Needs Attention"

        elif expiry > 0 or low_stock > 0:
            report["health"] = "Good"

        return report
    
    @staticmethod
    def business_chat(question):

        products = ProductService.get_all_products()

        inventory = ""

        for p in products:

            forecast = ForecastService.get_next_month_prediction(
                p[1]
            )

            if forecast is None:
                forecast = p[6]

            multiplier, event = ForecastService.seasonal_multiplier(
                p[2]
            )

            predicted = round(
                forecast * multiplier
            )

            recommended_import = max(
                predicted - p[6],
                0
            )

            inventory += f"""
    Product: {p[1]}
    Category: {p[2]}
    Brand: {p[3]}
    Supplier: {p[4]}
    Destination: {p[5]}

    Current Stock: {p[6]}

    Predicted Demand: {predicted}

    Recommended Import: {recommended_import}

    Season: {event if event else "Normal"}

    Cost Price: {p[8]}

    Selling Price: {p[9]}

    Expiry Date: {p[11]}

    Warehouse: {p[12]}

    Status: {p[13]}

    """

        prompt = f"""
        You are FOF-AI, an AI Business Intelligence Assistant developed for
        ETS FOFANA CONFISERIE.

        Company Profile:
        - Imports food products from Turkey, Morocco, Tunisia and Brazil.
        - Exports products to Mali, Burkina Faso, Côte d'Ivoire and Angola.
        - Products include Biscuits, Chocolate, Candy and Dates.

        Your responsibilities:

        1. Analyze inventory.

        2. Analyze future demand.

        3. Analyze seasonal demand.

        4. Recommend imports.

        5. Recommend promotions.

        6. Reduce expiry losses.

        7. Improve company profitability.

        8. Suggest inventory optimization.

        9. Answer like a professional Supply Chain and Business Consultant.
        Rules:

        - Answer only from the inventory provided.
        - Never invent products.
        - If information is missing, clearly state that.
        - Give practical business advice whenever possible.
        - Keep answers concise and professional.

        Inventory:

        {inventory}

        User Question:

        {question}

        Business Answer:
        """

        return GeminiService.ask(prompt)
    
    @staticmethod
    def generate_executive_report():

        products = ProductService.get_all_products()

        total_products = len(products)

        low_stock = len(
            [p for p in products if p[6] < 100]
        )

        expiring = len(
            ProductService.get_expiring_products()
        )

        report = f"""
    # 📊 Executive Business Report

    ## Inventory Summary

    • Total Products: {total_products}

    • Low Stock Products: {low_stock}

    • Products Near Expiry: {expiring}

    ---

    ## AI Business Insights

    • Inventory is being monitored successfully.

    • Demand forecasting is active.

    • Seasonal intelligence is enabled.

    • AI Import Planner is operational.

    ---

    ## Recommendations

    - Increase stock for high-demand products.

    - Monitor expiry dates weekly.

    - Prepare imports before seasonal demand increases.

    - Continue using demand forecasting before placing supplier orders.

    ---

    Generated by **FOF-AI Business Intelligence System**
    """

        return report

    @staticmethod
    def explain_recommendation(product):

        analysis = AIService.analyze_product(product)

        prompt = f"""
    You are FOF-AI, an Executive AI Business Consultant for ETS FOFANA CONFISERIE.

    Your task is to explain WHY the recommendation was made.

    Product Information

    Product Name: {product[1]}
    Category: {product[2]}
    Supplier Country: {product[4]}
    Current Stock: {product[6]} {product[7]}
    Profit Margin: {analysis['margin']}%
    Days Until Expiry: {analysis['days_left']}
    Recommendation: {analysis['recommendation']}

    Rules:

    - Think like an experienced Supply Chain Manager.
    - Explain the business reasons behind the recommendation.
    - Never invent information.
    - Keep the explanation short and practical.
    - Use exactly this format.

    ### Why?

    • Reason 1

    • Reason 2

    • Reason 3

    ### Business Impact

    One short sentence explaining how this recommendation helps the company.

    ### Confidence

    Give only one percentage from 0–100%.
    """

        return GemmaService.ask(prompt)

    @staticmethod
    def check_and_send_alerts():

            from services.notification_service import NotificationService

            products = ProductService.get_all_products()

            for product in products:

                analysis = AIService.analyze_product(product)

                if analysis["days_left"] <= 30:

                    subject = f"⚠️ FOF-AI Alert: {product[1]} Near Expiry"

                    message = f"""
    Product: {product[1]}

    Current Stock: {product[6]} {product[7]}

    Expiry Date: {product[11]}

    Days Remaining: {analysis['days_left']}

    AI Recommendation:

    {analysis['recommendation']}

    

    Generated automatically by FOF-AI.
    """

                    NotificationService.send_email(
                        subject,
                        message
                    )