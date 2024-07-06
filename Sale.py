class Sale:
    def __init__(self, id, customer_id, product_id, quantity, total, discount, date):
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.discount = discount
        self.date = date
        
    def __str__(self):
        return f'{self.id} - {self.customer_id} - {self.product_id} - {self.quantity} - {self.total} - {self.discount} - {self.date}'