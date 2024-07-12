from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController

class Report:
    def __init__(self, product_controller: ProductController, customer_controller: CustomerController, sale_controller: SaleController):
        self.product_controller = product_controller
        self.customer_controller = customer_controller
        self.sale_controller = sale_controller

    def get_products(self):
        return self.product_controller.list_products()

    def get_customers(self):
        return self.customer_controller.get_all_customers()

    def get_sales(self):
        return self.sale_controller.get_sales()

    def get_sales_by_customer(self, customer_id):
        return self.sale_controller.get_sales_by_customer(customer_id)

    def get_sales_by_product(self, product_id):
        return self.sale_controller.get_sales_by_product(product_id)

    def get_sales_by_date(self, date):
        return self.sale_controller.get_sales_by_date(date)

    def get_sales_by_date_range(self, start_date, end_date):
        return self.sale_controller.get_sales_by_date_range(start_date, end_date)