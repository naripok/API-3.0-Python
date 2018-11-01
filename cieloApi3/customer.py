
class Customer(object):

    def __init__(self, name, email=None, birth_date=None, identity=None, identity_type=None, address=None, delivery_address=None):

        self.name = name
        self.email = email
        self.birth_date = birth_date
        self.identity = identity
        self.identity_type = identity_type
        self.address = address
        self.delivery_address = delivery_address
