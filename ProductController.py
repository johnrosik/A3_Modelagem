import json

class ProductController:
    def __init__(self, file_path='produtos.json'):
        self.file_path = file_path
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_products(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.products, file, indent=4)

    def add_product(self, id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description):
        product = {
            'id': id,
            'name': name,
            'price': price,
            'partNumber': partNumber,
            'stock': stock,
            'category': category,
            'factoryPrice': factoryPrice,
            'manufacturer': manufacturer,
            'description': description
        }
        self.products.append(product)
        self.save_products()

    def list_products(self):
        return self.products

    def search_products_by(self, id=None, partNumber=None, name=None, category=None, manufacturer=None, description=None):
        return [product for product in self.products if
                (id is None or product['id'] == id) and
                (partNumber is None or product['partNumber'] == partNumber) and
                (name is None or product['name'] == name) and
                (category is None or product['category'] == category) and
                (manufacturer is None or product['manufacturer'] == manufacturer) and
                (description is None or product['description'] == description)]

    def delete_products_by(self, id):
        product = self.search_products_by(id=id)
        if product:
            self.products.remove(product[0])
            self.save_products()
            return True
        return False

    def update_product(self, id, name=None, price=None, partNumber=None, stock=None, category=None, factoryPrice=None, manufacturer=None, description=None):
        product = self.search_products_by(id=id)
        if product:
            product = product[0]
            if name:
                product['name'] = name
            if price:
                product['price'] = price
            if partNumber:
                product['partNumber'] = partNumber
            if stock:
                product['stock'] = stock
            if category:
                product['category'] = category
            if factoryPrice:
                product['factoryPrice'] = factoryPrice
            if manufacturer:
                product['manufacturer'] = manufacturer
            if description:
                product['description'] = description
            self.save_products()
            return True
        return False
