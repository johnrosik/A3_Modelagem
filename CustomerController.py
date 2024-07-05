import json
from Customer import Customer

class CustomerController:
    def __init__(self, file_path='clientes.json'):
        self.file_path = file_path
        self.customers = self.load_customers()

    def load_customers(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_customers(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.customers, file, indent=4)

    def add_customer(self, id, name, phone, email, cpf):
        customer = {"id": id, "name": name, "phone": phone, "email": email, "cpf": cpf}
        self.customers.append(customer)
        self.save_customers()

    def get_all_customers(self):
        return self.customers

    def find_customer_by(self, name=None, id=None, cpf=None):
        return [customer for customer in self.customers if
                (name is None or customer["name"] == name) and
                (id is None or customer["id"] == id) and
                (cpf is None or customer["cpf"] == cpf)]

    def delete_customer_by(self, id):
        customer = self.find_customer_by(id=id)
        if customer:
            self.customers.remove(customer[0])
            self.save_customers()
            return True
        return False

    def update_customer(self, id, new_name=None, new_phone=None, new_email=None, new_cpf=None):
        customer = self.find_customer_by(id=id)
        if customer:
            customer = customer[0]
            if new_name:
                customer["name"] = new_name
            if new_phone:
                customer["phone"] = new_phone
            if new_email:
                customer["email"] = new_email
            if new_cpf:
                customer["cpf"] = new_cpf
            self.save_customers()
            return True
        return False
