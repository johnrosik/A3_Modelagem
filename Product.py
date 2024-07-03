class Product:
    def __init__(self, id, name, price, partNumber, stock, category, factoryPrice, manufacturer, description):
        self.id = id
        self.name = name
        self.price = price
        self.partNumber = partNumber
        self.stock = stock
        self.category = category
        self.factoryPrice = factoryPrice
        self.manufacturer = manufacturer
        self.description = description        
    def __str__(self):
        return f'{self.id} - {self.name} - {self.price} ' \
            f'{self.partNumber} - {self.stock} - {self.category} ' \
            f'{self.factoryPrice} - {self.manufacturer} ' \
            f'{self.description}'
