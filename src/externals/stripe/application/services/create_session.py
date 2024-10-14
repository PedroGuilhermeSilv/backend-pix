from src.externals.stripe.application.services.dto.session import ListItems
from src.externals.stripe.config import stripe


class CreateCheckout:
    def __init__(self, itens: ListItems, user: str):
        self.itens = itens
        self.user = user

    def create(self) -> str:
        user = stripe.Customer.search(query=f"email:'{self.user}'")
        stripe_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=self.itens.model_dump().get("data"),
            mode="payment",
            success_url="http://localhost:3000/my-list",
            cancel_url="http://localhost:3000/my-list/cancel",
            customer=user.get("data")[0].get("id"),
        )

        return stripe_session.id
