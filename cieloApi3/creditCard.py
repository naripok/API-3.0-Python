
from .objectJSON import ObjectJSON

class CreditCard(ObjectJSON):

    def __init__(self, customer_name, card_number, holder, expiration_date, security_code, brand, card_token=None, save_card=False):

        self.card_number = card_number
        self.holder = holder
        self.expiration_date = expiration_date
        self.security_code = security_code
        self.save_card = save_card
        self.brand = brand
        self.card_token = card_token
        self.customer_name = customer_name


    def update_return(self, response_return):

        self.card_token = response_return['CardToken']
