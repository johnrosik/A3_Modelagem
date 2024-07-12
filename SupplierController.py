import json
class SupplierController:
    def __init__(self, file_path='suppliers.json'):
        self.file_path = file_path
        self.suppliers = self.load_suppliers()
        
    def load_suppliers(self):
        try:
            with open('suppliers.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        
    def save_suppliers(self):
        with open('suppliers.json', 'w') as file:
            json.dump(self.suppliers, file, indent=4)

    def add_supplier(self, id, name, phone, address, productType, cnpj):
        Supplier = {
            'id': id,
            'name': name,
            'phone': phone,
            'address': address,
            'productType': productType,
            'cnpj': cnpj
        }
        self.suppliers.append(Supplier)
        self.save_suppliers()
        
    def list_suppliers(self):
        return self.suppliers
    
    def search_suppliers_by(self, id=None, name=None, phone=None, address=None, productType=None, cnpj=None):
        return [Supplier for Supplier in self.suppliers if
                (id is None or Supplier['id'] == id) and
                (name is None or Supplier['name'] == name) and
                (phone is None or Supplier['phone'] == phone) and
                (address is None or Supplier['address'] == address) and
                (productType is None or Supplier['productType'] == productType) and
                (cnpj is None or Supplier['cnpj'] == cnpj)]
        
    def delete_supplier_by(self, id):
        Supplier = self.search_suppliers_by(id=id)
        if Supplier:
            self.suppliers.remove(Supplier[0])
            self.save_suppliers()
            return True
        return False
    
    def update_supplier(self, id, name=None, phone=None, address=None, productType=None, cnpj=None):
        Supplier = self.search_suppliers_by(id=id)
        if Supplier:
            Supplier = Supplier[0]
            if name:
                Supplier['name'] = name
            if phone:
                Supplier['phone'] = phone
            if address:
                Supplier['address'] = address
            if productType:
                Supplier['productType'] = productType
            if cnpj:
                Supplier['cnpj'] = cnpj
            self.save_suppliers()
            return True
        return False