import json
import tkinter as tk
from tkinter import messagebox

from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController

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
        ]
    
        # Criar e posicionar os botões usando um loop
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=10)
    
        # Botão de sair ocupando todas as colunas disponíveis
        btn_exit = tk.Button(self.main_frame, text='Sair', command=self.root.quit)
        btn_exit.grid(row=1, column=0, columnspan=len(buttons), pady=5)
    def productMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        buttons = [
            ('Adicionar Produto', self.collect_product_data),
            ('Listar Produtos', self.productController.list_products),
            ('Buscar Produto', self.productController.search_products_by),
            ('Deletar Produto', self.productController.delete_products_by),
            ('Atualizar Produto', self.productController.update_product),
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=5)
            
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.grid(row=1, column=0, columnspan=len(buttons), pady=10)
        
    def collect_product_data(self):
        self.product_window = tk.Toplevel(self.root)
        self.product_window.title("Adicionar Produto")
    
        campos = [
            ("ID do Produto:", "id_entry"),
            ("Nome do Produto:", "name_entry"),
            ("Preço do Produto:", "price_entry"),
            ("Número da Peça:", "part_number_entry"),
            ("Estoque do Produto:", "stock_entry"),
            ("Categoria do Produto:", "category_entry"),
            ("Preço de Fábrica:", "factory_price_entry"),
            ("Fabricante:", "manufacturer_entry"),
            ("Descrição:", "description_entry")
        ]
    
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.product_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.product_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)  # Define o atributo dinamicamente
    
        btn_save = tk.Button(self.product_window, text="Salvar", command=self.save_product)
        btn_save.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
    def save_product(self):
        campos = [
            ("id_entry", "id"),
            ("name_entry", "name"),
            ("price_entry", "price"),
            ("part_number_entry", "part_number"),
            ("stock_entry", "stock"),
            ("category_entry", "category"),
            ("factory_price_entry", "factory_price"),
            ("manufacturer_entry", "manufacturer"),
            ("description_entry", "description")
        ]
    
    
        produto = {}
        for entry_attr, key in campos:
            value = getattr(self, entry_attr).get()
            if not value:
                # Handle empty value
                value = None
            produto[key] = value
    
    
        with open('produto.json', 'w') as json_file:
            json.dump(produto, json_file, indent=4)
    
        print("Objeto salvo com sucesso em produto.json")

            
    def list_products(self):
        products = self.productController.list_products()
        
        if not products:
            tk.Label(self.main_frame, text="Nenhum produto cadastrado.").pack(pady=20)
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
            return
        
        for product in products:
            tk.Label(self.main_frame, text=product).pack(pady=5)
        
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
        
    def customerMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        buttons = [
            ('Adicionar Cliente', self.collect_customer_data),
            ('Listar Clientes', self.customerController.get_all_customers),
            ('Buscar Cliente', self.customerController.find_customer_by),
            ('Deletar Cliente', self.customerController.delete_customer_by),
            ('Atualizar Cliente', self.customerController.update_customer),
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=5)

        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.grid(row=1, column=0, columnspan=len(buttons), pady=10)
        
    def collect_customer_data(self):
        self.customers_window = tk.Toplevel(self.root)
        self.customers_window.title("Adicionar Cliente")
        
        campos = [
            ("ID do Cliente:", "id_entry"),
            ("Nome do Cliente:", "name_entry"),
            ("Telefone do Cliente:", "phone_entry"),
            ("Email do Cliente:", "email_entry"),
            ("CPF do Cliente:", "cpf_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.customers_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.customers_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_save = tk.Button(self.customers_window, text="Salvar", command=self.save_customer)
        btn_save.grid(row=len(campos), column=0, columnspan=2, pady=10)

    def save_customer(self):
        campos = [
            ("id_entry", "id"),
            ("name_entry", "name"),
            ("phone_entry", "phone"),
            ("email_entry", "email"),
            ("cpf_entry", "cpf")
        ]
        
        customer = {}
        for entry_attr, key in campos:
            value = getattr(self, entry_attr).get()
            if not value:
                # Handle empty value
                value = None
            customer[key] = value
            
        with open('customer.json', 'w') as json_file:
            json.dump(customer, json_file, indent=4)
            
        print("Objeto salvo com sucesso em customer.json")

    #def saleMenu(self):
        
    
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
    def stockMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        products = self.productController.list()
        
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
    
            # Encontrar o produto selecionado pelo nome
            selected_product = None
            for product in self.productController.get_all_products():
                if product['name'] == selected_product_name:
                    selected_product = product
                    break
    
            if not selected_product:
                messagebox.showerror("Produto não encontrado", f"Produto '{selected_product_name}' não encontrado.")
                return
    
            # Atualizar o estoque do produto
            new_stock = selected_product['stock'] + quantity
            selected_product['stock'] = new_stock
    
            # Exibir mensagem de sucesso
            messagebox.showinfo("Estoque Atualizado", f"Estoque de '{selected_product_name}' atualizado para {new_stock}")
    
            # Voltar ao menu principal
            self.create_main_menu()
    
        except ValueError:
            messagebox.showerror("Erro de entrada", "A quantidade deve ser um número inteiro.")
        new_stock = selected_product.stock + quantity
        selected_product.stock = new_stock
    
        # Exibir mensagem de sucesso
        messagebox.showinfo("Estoque Atualizado", f"Estoque de '{selected_product_name}' atualizado para {new_stock}")
    
        # Voltar ao menu principal
        self.create_main_menu()

    def saleMenu(self):
        id = "001"
        customer = "John Doe"  # Replace "John Doe" with the actual customer name
        product = "Product Name"  # Replace "Product Name" with the actual product name
        quantity = 1
        date = "01/01/2021"
        self.saleController.add(id, customer, product, quantity, date)
        
        messagebox.showinfo("Venda Adicionada", f"Venda '{id}' cadastrada com sucesso")
    

def main():
    root = tk.Tk()
    ERPSuzuka(root)
    root.mainloop()

if __name__ == "__main__":
    main()
