from src.externals.stripe.application.services.dto.session import StatusSession
from src.externals.stripe.config import stripe


class GetCheckoutSession:
    def __init__(self, session_id):
        self.session_id = session_id

    def execute(self)-> StatusSession:
        try:
            stripe.checkout.Session.retrieve(self.session_id)
            status = stripe.checkout.Session.retrieve(self.session_id).payment_status
        except Exception as error:
            raise error

        return  StatusSession(payment_status=status)