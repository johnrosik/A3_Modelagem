from Product import Product
from ProductController import ProductController

class StockController:
    def __init__(self):
        self.productController = ProductController()
    
    def add(self, id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description):
        product = Product(id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description)
        self.productController.add(product)
    
    def list(self):
        return self.productController.list()
    
    def search(self, id):
        return self.productController.search(id)
    
    def delete(self, id):
        return self.productController.delete(id)
    
    def update(self, id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description):
        product = Product(id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description)
        self.productController.update(product)
    
    def sell(self, id, quantity):
        product = self.productController.search(id)
        if product:
            if product.stock >= quantity:
                product.stock -= quantity
                self.productController.update(product)
                return True
        return False