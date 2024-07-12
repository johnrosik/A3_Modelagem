
class Supplier:
    def __init__(self, id, name, phone, address, productType, cnpj):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.productType = productType
        self.cnpj = cnpj
        
    def __str__(self):
        return f'{self.id} - {self.name} - {self.phone} - {self.address} - {self.productType} - {self.cnpj}'
    