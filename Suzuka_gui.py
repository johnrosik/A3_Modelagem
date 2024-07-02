import tkinter as tk
from tkinter import messagebox, simpledialog

from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController
from Menu import Menu

class ERPSuzuka:
    def __init__(self, root):
        self.root = root
        self.root.title('Suzuka Auto Peças')
        
        self.productController = ProductController()
        self.customerController = CustomerController()
        self.saleController = SaleController()
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        self.create_main_menu()
    
    def create_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
        # Definir os textos e comandos para os botões
        buttons = [
            ('Produto', self.productMenu),
            ('Cliente', self.customerMenu),
            ('Venda', self.saleMenu),
            ('Estoque', self.stockMenu),
            ('Sair', self.root.quit)
        ]
    
        # Criar e posicionar os botões usando um loop
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=5)
    
        # Botão de sair ocupando todas as colunas disponíveis
        btn_exit = tk.Button(self.main_frame, text='Sair', command=self.root.quit)
        btn_exit.grid(row=1, column=0, columnspan=len(buttons), pady=10)

    def productMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.main_frame, text="ID do Produto:").grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.main_frame, text="Nome do Produto:").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self.main_frame, text="Preço do Produto:").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.main_frame)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)
        
        btn_save = tk.Button(self.main_frame, text="Salvar", command=self.save_product)
        btn_save.grid(row=3, column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.grid(row=4, column=0, columnspan=2, pady=10)
        
    def stockMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        products = self.productController.get_all_products()
        
        if not products:
            tk.Label(self.main_frame, text="Nenhum produto cadastrado.").pack(pady=20)
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
            return
        
        tk.Label(self.main_frame, text="Selecione o Produto para Atualizar o Estoque").pack(pady=10)
        
        self.selected_product = tk.StringVar(self.main_frame)
        self.selected_product.set(products[0]['name'])  # Valor padrão
        
        product_options = [product['name'] for product in products]
        option_menu = tk.OptionMenu(self.main_frame, self.selected_product, *product_options)
        option_menu.pack(pady=10)
        
        tk.Label(self.main_frame, text="Quantidade a Adicionar/Remover:").pack(pady=5)
        self.quantity_entry = tk.Entry(self.main_frame)
        self.quantity_entry.pack(pady=5)
        
        btn_update = tk.Button(self.main_frame, text="Atualizar Estoque", command=self.performStockUpdate)
        btn_update.pack(pady=10)
        
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
            
    def performStockUpdate(self):
        selected_product_name = self.selected_product.get()
        quantity_str = self.quantity_entry.get()
    
        try:
            quantity = int(quantity_str)
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "A quantidade deve ser um número inteiro!")
            return
    
        # Encontrar o produto selecionado pelo nome
        selected_product = None
        for product in self.productController.get_all_products():
            if product.name == selected_product_name:
                selected_product = product
                break
    
        if not selected_product:
            messagebox.showerror("Produto Não Encontrado", "O produto selecionado não foi encontrado!")
            return
    
        # Atualizar o estoque do produto
        new_stock = selected_product.stock + quantity
        selected_product.stock = new_stock
    
        # Exibir mensagem de sucesso
        messagebox.showinfo("Estoque Atualizado", f"Estoque de '{selected_product_name}' atualizado para {new_stock}")
    
        # Voltar ao menu principal
        self.create_main_menu()

        
        
        
    def save_product(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        price_str = self.price_entry.get()
    
        try:
            # Convertendo a string de preço para float, trocando vírgula por ponto
            price = float(price_str.replace(',', '.'))
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "Preço deve ser um número válido!")
            return
    
        if id and name and price:
            # Debug: Imprimir dados antes de salvar
            print(f"ID: {id}, Nome: {name}, Preço: {price}")
    
            self.productController.add(id, name, price)
            messagebox.showinfo("Produto Adicionado", f"Produto '{name}' cadastrado com sucesso")
            self.create_main_menu()  # Volta ao menu principal após salvar
    
            # Debug: Verificar se o produto foi adicionado corretamente
            products = self.productController.get_all_products()
            print("Produtos cadastrados:")
            for product in products:
                print(product)
        else:
            messagebox.showwarning("Entrada Inválida", "Todos os campos são obrigatórios!")

    def customerMenu(self):
        id = "001"
        name = "Customer 1"
        phone = "123456789"
        self.customerController.add(id, name, phone)
        
        messagebox.showinfo("Cliente Adicionado", f"Cliente '{name}' cadastrado com sucesso")
        
    def saleMenu(self):
        id = "001"
        customer
        product
        quantity = 1
        date = "01/01/2021"
        self.saleController.add(id, customer, product, quantity, date)
        
        messagebox.showinfo("Venda Adicionada", f"Venda '{id}' cadastrada com sucesso")
    

def main():
    root = tk.Tk()
    app = ERPSuzuka(root)
    root.mainloop()

if __name__ == "__main__":
    main()
