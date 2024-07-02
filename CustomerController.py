from Customer import Customer


class CustomerController:
    def __init__(self):
        self.customers = []
            
    def add(self, id, name, email):
        self.customers.append(Customer(id, name, email))
            
    def list(self):
        return self.customers
        
    def search(self, id):
        return next((customer for customer in self.customers if customer.id == id), None)
        
    def delete(self, id):
        customer = self.search(id)
        if customer:
            self.customers.remove(customer)
            return True
        return False
        
    def update(self, id, name, email):
        customer = self.search(id)
        if customer:
            customer.name = name
            customer.email = email
            return True
        return False