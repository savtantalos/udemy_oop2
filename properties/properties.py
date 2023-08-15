class Customer:
    loyalty_level = {'silver', 'gold', 'platinum'}
    membership_level = {'min': 0, 'max': 100}

    def __init__(self ,loyalty, membership):
        self.loyalty = loyalty
        self.membership = membership

    @property
    def loyalty(self):
        return self._loyalty

    @loyalty.setter
    def loyalty(self ,level):
        if level in Customer.loyalty_level:
            self._loyalty = level
        else:
            raise ValueError(f'{level} is not a valid loyalty level')

    @property
    def membership(self):
        return self._membership

    @membership.setter
    def membership(self, level):
        if level>=Customer.membership_level['max'] or level<=Customer.membership_level['min']:
            raise ValueError(f'{level} is not a valid membership level')
        else:
            self._membership = level

x = Customer('silver',100)
print(x.loyalty, x.membership)
