from Report import Report
from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController
from datetime import datetime

class ReportController:
    def __init__(self, product_controller: ProductController, customer_controller: CustomerController, sale_controller: SaleController):
        self.report = Report(product_controller, customer_controller, sale_controller)

    def list_products(self):
        products = self.report.get_products()
        for product in products:
            print(product)

    def list_customers(self):
        customers = self.report.get_customers()
        for customer in customers:
            print(customer)

    def list_sales(self):
        sales = self.report.get_sales()
        for sale in sales:
            print(sale)

    def list_sales_by_customer(self, customer_id):
        sales = self.report.get_sales_by_customer(customer_id)
        for sale in sales:
            print(sale)

    def list_sales_by_product(self, product_id):
        sales = self.report.get_sales_by_product(product_id)
        for sale in sales:
            print(sale)

    def list_sales_by_date(self, date):
        sales = self.report.get_sales_by_date(date)
        for sale in sales:
            print(sale)

    def list_sales_by_date_range(self, start_date, end_date):
        sales = self.report.get_sales_by_date_range(start_date, end_date)
        for sale in sales:
            print(sale)

    def get_sales_total(self):
        sales = self.report.get_sales()
        total = 0
        for sale in sales:
            total += sale.total
        return total

    def get_sales_total_by_customer(self, customer_id):
        sales = self.report.get_sales_by_customer(customer_id)
        total = 0
        for sale in sales:
            total += sale.total
        return total

    def get_sales_total_by_product(self, product_id):
        sales = self.report.get_sales_by_product(product_id)
        total = 0
        for sale in sales:
            total += sale.total
        return total

    def get_sales_total_by_date(self, date):
        sales = self.report.get_sales_by_date(date)
        total = 0
        for sale in sales:
            total += sale.total
        return total

    def get_sales_total_by_date_range(self, start_date, end_date):
        sales = self.report.get_sales_by_date_range(start_date, end_date)
        total = 0
        for sale in sales:
            total += sale.total
        return total

    def get_sales_total_by_product_category(self, category):
        pass
        
    def save_report(self):
        with open('report.txt', 'w') as file:
            file.write(f'Total de vendas: R${self.get_sales_total()}\n')
            file.write(f'Total de vendas por cliente: R${self.get_sales_total_by_customer(1)}\n')
            file.write(f'Total de vendas por produto: R${self.get_sales_total_by_product(1)}\n')
            file.write(f'Total de vendas por data: R${self.get_sales_total_by_date(datetime.now().strftime("%Y-%m-%d"))}\n')
            file.write(f'Total de vendas por intervalo de datas: R${self.get_sales_total_by_date_range(datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%Y-%m-%d"))}\n')
            
            file.write('Vendas por cliente:\n')
            sales = self.report.get_sales()
            for sale in sales:
                file.write(f'{sale}\n')
            
            file.write('Vendas por produto:\n')
            sales = self.report.get_sales()
            for sale in sales:
                file.write(f'{sale}\n')
                
            file.write('Vendas por data:\n')
            sales = self.report.get_sales()
            for sale in sales:
                file.write(f'{sale}\n')
                
            file.write('Vendas por intervalo de datas:\n')
            sales = self.report.get_sales()
            for sale in sales:
                file.write(f'{sale}\n')
