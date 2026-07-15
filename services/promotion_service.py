from services.gemma_service import GemmaService


class PromotionService:

    @staticmethod
    def generate_promotion(product):

        prompt = f"""
You are a professional marketing expert working for
ETS FOFANA CONFISERIE.

Create a promotional campaign for this product.

Product Name:
{product[1]}

Category:
{product[2]}

Brand:
{product[3]}

Supplier Country:
{product[4]}

Current Stock:
{product[6]} {product[7]}

Expiry Date:
{product[11]}

Return your answer in the following format exactly.

FACEBOOK_POST:
(write only the Facebook advertisement)

WHATSAPP_POST:
(write only the WhatsApp advertisement)

SLOGAN:
(write only the slogan)

CALL_TO_ACTION:
(write only the call to action)

Do not add explanations.
Do not use Markdown.
"""

        return GemmaService.ask(prompt)