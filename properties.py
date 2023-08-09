
class Customer:
    loyalty_level = {'silver', 'gold', 'platinum'}

    def __init__(self ,loyalty):
        self.loyalty = loyalty

    @property
    def loyalty(self):
        return self._loyalty

    @loyalty.setter
    def loyalty(self ,level):
        if level in Customer.loyalty_level:
            self._loyalty = level
        else:
            raise ValueError(f'{level} is not a valid loyalty level')


x = Customer('silver')
print(x.loyalty)
