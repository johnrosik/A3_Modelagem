from Sale import Sale
import json


class SaleController:
    def __init__(self):
        self.sales = []
        
    def load_sales(self):
        try:
            with open('vendas.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
    def save_sales(self):
        with open('vendas.json', 'w') as file:
            json.dump(self.sales, file, indent=4)
            
    def add_sale(self, id, customer_id, product_id, quantity, total, discount, date):
        sale = {
            'id': id,
            'customer_id': customer_id,
            'product_id': product_id,
            'quantity': quantity,
            'total': total,
            'discount': discount,
            'date': date
        }
        self.sales.append(sale)
        self.save_sales()
        
    def list_sales(self):
        return self.sales
    
    def search_sales_by(self, id=None, customer_id=None, product_id=None, date=None):
        return [sale for sale in self.sales if
                        (id is None or sale['id'] == id) and
                        (customer_id is None or sale['customer_id'] == customer_id) and
                        (product_id is None or sale['product_id'] == product_id) and
                        (date is None or sale['date'] == date)]
        
    def delete_sales_by(self, id):
        if sale := self.search_sales_by(id=id):
            self.sales.remove(sale[0])
            self.save_sales()
            return True
        return False
    
    def update_sale(self, id, customer_id=None, product_id=None, quantity=None, total=None, discount=None, date=None):
        sale = self.search_sales_by(id=id)
        if sale := sale[0]:
            if customer_id:
                sale['customer_id'] = customer_id
            if product_id:
                sale['product_id'] = product_id
            if quantity:
                sale['quantity'] = quantity
            if total:
                sale['total'] = total
            if discount:
                sale['discount'] = discount
            if date:
                sale['date'] = date
            self.save_sales()
            return True
        return False
        