from Customer import Customer
import json

class CustomerController:
    def __init__(self):
        self.customers = []
            
    def add_customer(self, id, name, phone, email, cpf):
        customer = {"id": id, "name": name, "phone": phone, "email": email, "cpf": cpf}
        self.customers.append(customer)

    def get_all_customers(self):
        try:
            with open(self.file_path, 'r') as file:
                customers = json.load(file)
                return customers
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def find_customer_by(self, name, id, cpf):
        # sourcery skip: merge-duplicate-blocks, remove-redundant-if, use-next
        for customer in self.customers:
            if customer["name"] == name:
                return customer
            elif customer["id"] == id:
                return customer
            elif customer["CPF"] == cpf:
                return customer
        return None

    def delete_customer_by(self, name, id, cpf):
        self.customers = [customer for customer in self.customers if customer["name"] != name and customer["id"] != id and customer["cpf"] != cpf]

    def update_customer(self, id, new_name, new_phone, new_email, new_cpf):
        for customer in self.customers:
            if customer["id"] == id:
                customer["name"] = new_name
                customer["phone"] = new_phone
                customer["email"] = new_email
                customer["cpf"] = new_cpf
                return True
        return False