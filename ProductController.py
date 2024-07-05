from Product import Product
import json

class ProductController:
    def __init__(self):
        self.products = []
            
    def add_product(self, id, name, price, partNumber, stock, category, factoryPrice,  manufacturer, description):
        product = {'id': id, 'name': name, 'price': price , 'partNumber': partNumber, 'stock': stock, 'category': category, 'factoryPrice': factoryPrice, 'manufacturer': manufacturer, 'description': description}
        self.products.append(Product(id, name, price , partNumber, stock, category, factoryPrice,  manufacturer, description))
            
    def list_products(self):
        try:
            with open(self.file_path, 'r') as file:
                product = json.load(file)
                return self.products
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
    def search_products_by(self, id, partNumber, name, category, manufacturer, description,):
        return next((product for product in self.products if product['id'] == id and product['partNumber'] == partNumber and product['name'] == name and product['category'] == category and product['manufacturer'] == manufacturer and product['description'] == description), None)
        
    def delete_products_by(self, id, partNumber, name, category, manufacturer, description):
        product = self.search(id)
        if product:
            self.products.remove(product)
            return True
        return False
        
    def update_product(self, id, name, price, partNumber, stock, category, factoryPrice, salePrice, manufacturer, description):
        product = self.search(id)
        if product:
            product.name = name
            product.price = price
            product.partNumber = partNumber
            product.stock = stock
            product.category = category
            product.factoryPrice = factoryPrice
            product.manufacturer = manufacturer
            product.description = description
            return True
        return False