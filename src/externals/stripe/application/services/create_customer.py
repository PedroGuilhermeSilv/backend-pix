from src.externals.stripe.application.services.dto.customer import Customer
from src.externals.stripe.config import stripe


class CreateCustomerStripe:
    def __init__(self, customer: Customer):
        self.customer = customer

    def create(self) -> Customer:
        stripe_customer = stripe.Customer.create(
            email=self.customer.email, name=self.customer.name
        )

        return Customer(name=stripe_customer.name, email=stripe_customer.email)
