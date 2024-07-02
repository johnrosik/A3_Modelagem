from CustomerController import CustomerController
from ProductController import ProductController
from SaleController import SaleController


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