# Suzuka.py

# Importing necessary libraries

# Product
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
            
    def __str__(self):
        return f'{self.id} - {self.name} - {self.price}'

class ProductController:
    def __init__(self):
        self.products = []
            
    def add(self, id, name, price):
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
    
    
# Customer
class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
            
    def __str__(self):
        return f'{self.id} - {self.name} - {self.email}'
    
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
    
    # Sale
class Sale:
    def __init__(self, id, customer, product, quantity, date):
        self.id = id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.date = date
            
    def __str__(self):
        return f'{self.id} - {self.customer} - {self.product} - {self.quantity} - {self.date}'
    
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
    
# Menu

class Menu:
    def __init__(self):
        self.productController = ProductController()
        self.customerController = CustomerController()
        self.saleController = SaleController()
        
    def menu(self):
        while True:
            print('1 - Product')
            print('2 - Customer')
            print('3 - Sale')
            print('4 - Exit')
            option = input('Choose an option: ')
            if option == '1':
                self.productMenu()
            elif option == '2':
                self.customerMenu()
            elif option == '3':
                self.saleMenu()
            elif option == '4':
                break
                
    def productMenu(self):
        while True:
            print('1 - Add')
            print('2 - List')
            print('3 - Search')
            print('4 - Delete')
            print('5 - Update')
            print('6 - Back')
            option = input('Choose an option: ')
            if option == '1':
                id = input('Enter the id: ')
                name = input('Enter the name: ')
                price = input('Enter the price: ')
                self.productController.add(id, name, price)
            elif option == '2':
                for product in self.productController.list():
                    print(product)
            elif option == '3':
                id = input('Enter the id: ')
                product = self.productController.search(id)
                if product:
                    print(product)
                else:
                    print('Product not found')
            elif option == '4':
                id = input('Enter the id: ')
                if self.productController.delete(id):
                    print('Product deleted successfully')
                else:
                    print('Product not found')
            elif option == '5':
                id = input('Enter the id: ')
                name = input('Enter the name: ')
                price = input('Enter the price: ')
                if self.productController.update(id, name, price):
                    print('Product updated successfully')
                else:
                    print('Product not found')
            elif option == '6':
                break
                
    def customerMenu(self):
        while True:
            print('1 - Add')
            print('2 - List')
            print('3 - Search')
            # Add more options here
            
