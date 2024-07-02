from Product import Product


class ProductController:
    def __init__(self):
        self.products = []
            
    def add(self, id, name, price):
        product = {'id': id, 'name': name, 'price': price}
        self.products.append(Product(id, name, price))
            
    def list(self):
        return self.products
        
    def search(self, id):
        return next((product for product in self.products if product.id == id), None)
        
    def delete(self, id):
        product = self.search(id)
        if product:
            self.products.remove(product)
            return True
        return False
        
    def update(self, id, name, price):
        product = self.search(id)
        if product:
            product.name = name
            product.price = price
            return True
        return False