from Sale import Sale


class SaleController:
    def __init__(self):
        self.sales = []
            
    def add(self, id, customer, product, quantity, date):
        self.sales.append(Sale(id, customer, product, quantity, date))
            
    def list(self):
        return self.sales
        
    def search(self, id):
        return next((sale for sale in self.sales if sale.id == id), None)
        
    def delete(self, id):
        sale = self.search(id)
        if sale:
            self.sales.remove(sale)
            return True
        return False
        
    def update(self, id, customer, product, quantity, date):
        sale = self.search(id)
        if sale:
            sale.customer = customer
            sale.product = product
            sale.quantity = quantity
            sale.date = date
            return True
        return False
    