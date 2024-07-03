class Customer:
    def __init__(self, id, name, phone, email, cpf):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.cpf = cpf

    def __str__(self):
        return f'{self.id} - {self.name} - {self.email} - {self.phone} - {self.cpf}'