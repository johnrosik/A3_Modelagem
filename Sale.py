class Sale:
    def __init__(self, id, customer, product, quantity, date):
        self.id = id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.date = date
            
    def __str__(self):
        return f'{self.id} - {self.customer} - {self.product} - {self.quantity} - {self.date}'
    