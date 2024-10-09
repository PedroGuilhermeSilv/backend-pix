
from src.externals.stripe.application.services.dto.session import ListItems
from src.externals.stripe.config import stripe


class  CreateCheckout():
    def __init__(self, itens: ListItems):
        self.itens = itens

    def create(self)-> str:
        stripe_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=self.itens.model_dump().get("data"),
            mode='payment',
            success_url='http://localhost:3000/payment/sucess',
            customer_creation='always',
            cancel_url='http://localhost:3000/payment/cancel',
        )

        return stripe_session.id