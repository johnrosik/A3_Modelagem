import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController

import sv_ttk
class SuzukaMain:
    
    
    def __init__(self, root):
        self.root = root
        self.root.title('Suzuka Auto Peças')
        self.productController = ProductController()
        self.customerController = CustomerController()
        self.saleController = SaleController()
        
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        self.create_main_menu()
    def create_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
        buttons = [
            ('Produto', self.productMenu),
            ('Cliente', self.customerMenu),
            ('Venda', self.saleMenu),
        ]
    
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(self.main_frame, text=text, command=command)
            btn.pack(pady=10)
    
        btn_exit = ttk.Button(self.main_frame, text='Sair', command=self.root.quit)
        btn_exit.grid(row=1, column=0, columnspan=len(buttons), pady=5)
        
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def productMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        buttons = [
            ('Adicionar Produto', self.collect_product_data),
            ('Listar Produtos', self.list_products),
            ('Buscar Produto', self.search_products),
            ('Deletar Produto', self.delete_product),
            ('Atualizar Produto', self.update_product),
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = ttk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=5)
            
        btn_back = ttk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
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
            ttk.Label(self.product_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(self.product_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)  # Define o atributo dinamicamente
    
        btn_save = ttk.Button(self.product_window, text="Salvar", command=self.save_product)
        btn_save.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
    def save_product(self):
        campos = [
            ("id_entry", "id"),
            ("name_entry", "name"),
            ("price_entry", "price"),
            ("part_number_entry", "partNumber"),
            ("stock_entry", "stock"),
            ("category_entry", "category"),
            ("factory_price_entry", "factoryPrice"),
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
    
        self.productController.add_product(**produto)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        self.product_window.destroy()
        
    def list_products(self):
        self.clear_main_frame()
        
        products = self.productController.list_products()
        
        if not products:
            ttk.Label(self.main_frame, text="Nenhum produto cadastrado.").pack(pady=20)
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
            return
        
        for product in products:
            product_info = f"ID: {product['id']}, Nome: {product['name']}, Preço: {product['price']}"
            ttk.Label(self.main_frame, text=product_info).pack(pady=5)
            
            btn_update_product = ttk.Button(self.main_frame, text="Atualizar Produto", command=self.update_product)
            btn_update_product.pack(pady=10)
            
            btn_delete_product = ttk.Button(self.main_frame, text="Deletar Produto", command=self.delete_product)
            btn_delete_product.pack(pady=10)
        
        btn_back = ttk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
        
    def search_products(self):
        self.clear_main_frame()
        self.product_window.title("Buscar Produto")
        
        campos = [
            ("ID do Produto:", "id_entry"),
            ("Nome do Produto:", "name_entry"),
            ("Número da Peça:", "part_number_entry"),
            ("Categoria do Produto:", "category_entry"),
            ("Fabricante:", "manufacturer_entry"),
            ("Descrição:", "description_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            ttk.Label(self.product_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(self.product_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_search = ttk.Button(self.product_window, text="Buscar", command=lambda: self.display_search_results())
        btn_search.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = ttk.Button(self.product_window, text="Voltar", command=self.create_main_menu)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
        
    def display_search_results(self, id, name, part_number, category, manufacturer, description):
        results = self.productController.search_products_by(id, name, part_number, category, manufacturer, description) 
        if not results:
            messagebox.showinfo("Nenhum Produto Encontrado", "Nenhum produto encontrado com os critérios fornecidos.")
        else:
            self.clear_main_frame()
            for product in results:
                product_info = f"ID: {product['id']}, Nome: {product['name']}, Preço: {product['price']}"
                ttk.Label(self.main_frame, text=product_info).pack(pady=5)
    
        btn_back = ttk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
            
    def delete_product(self):
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Deletar Produto")
        
        campos = [
            ("ID do Produto:", "id_entry"),
            ("Nome do Produto:", "name_entry"),
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.delete_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.delete_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_delete = tk.Button(self.delete_window, text="Deletar", command=self.delete_product)
        btn_delete.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.delete_window, text="Voltar", command=self.delete_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
        
    def delete_product_by_id(self, id, name):
        deleted = self.productController.delete_product_by(id, name)
        if deleted:
            messagebox.showinfo("Sucesso", "Produto deletado com sucesso.")
        else:
            messagebox.showinfo("Erro", "Não foi possível deletar o produto.")
    
    def update_product(self):
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Atualizar Produto")
        
        campos = [
            ("ID do Produto:", "id_entry"),
            ("Novo Nome do Produto:", "new_name_entry"),
            ("Novo Preço do Produto:", "new_price_entry"),
            ("Novo Número da Peça:", "new_part_number_entry"),
            ("Novo Estoque do Produto:", "new_stock_entry"),
            ("Nova Categoria do Produto:", "new_category_entry"),
            ("Novo Preço de Fábrica:", "new_factory_price_entry"),
            ("Novo Fabricante:", "new_manufacturer_entry"),
            ("Nova Descrição:", "new_description_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.update_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.update_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_update = tk.Button(self.update_window, text="Atualizar", command=self.update_product_by_id)
        btn_update.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.update_window, text="Voltar", command=self.update_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def update_product_by_id(self, id, new_name, new_price, new_part_number, new_stock, new_category,
                                                new_factory_price, new_manufacturer, new_description):
        updated = self.productController.update_product(id, new_name, new_price, new_part_number, new_stock,
                                                        new_category, new_factory_price, new_manufacturer,
                                                        new_description)
        if updated:
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso.")
        else:
            messagebox.showinfo("Erro", "Não foi possível atualizar o produto.")
            
    def customerMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        buttons = [
            ('Adicionar Cliente', self.collect_customer_data),
            ('Listar Clientes', self.list_customers),
            ('Buscar Cliente', self.search_customers),
            ('Deletar Cliente', self.delete_customer),
            ('Atualizar Cliente', self.update_customer),
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
            setattr(self, entry_attr, entry)  # Define o atributo dinamicamente
        
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
        
        cliente = {}
        for entry_attr, key in campos:
            value = getattr(self, entry_attr).get()
            if not value:
                # Handle empty value
                value = None
            cliente[key] = value
        
        self.customerController.add_customer(**cliente)
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        self.customers_window.destroy()
        
    def list_customers(self):
        self.clear_main_frame()
        
        customers = self.customerController.get_all_customers()
        
        if not customers:
            tk.Label(self.main_frame, text="Nenhum cliente cadastrado.").pack(pady=20)
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
            return
        
        for customer in customers:
            customer_info = f"ID: {customer['id']}, Nome: {customer['name']}, CPF: {customer['cpf']}"
            tk.Label(self.main_frame, text=customer_info).pack(pady=5)
        
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
        
    def search_customers(self):
        self.search_window = tk.Toplevel(self.root)
        self.search_window.title("Buscar Cliente")
        
        campos = [
            ("ID do Cliente:", "id_entry"),
            ("Nome do Cliente:", "name_entry"),
            ("CPF do Cliente:", "cpf_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.search_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.search_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_search = tk.Button(self.search_window, text="Buscar", command=lambda: self.display_search_results_customer(
            self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get()))
        btn_search.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.search_window, text="Voltar", command=self.search_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def display_search_results_customer(self, id, name, cpf):
        results = self.customerController.find_customer_by(name=name, id=id, cpf=cpf)
        
        if not results:
            messagebox.showinfo("Nenhum Cliente Encontrado", "Nenhum cliente encontrado com os critérios fornecidos.")
        else:
            self.clear_main_frame()
            for customer in results:
                customer_info = f"ID: {customer['id']}, Nome: {customer['name']}, CPF: {customer['cpf']}"
                tk.Label(self.main_frame, text=customer_info).pack(pady=5)
        
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
        
    def delete_customer(self):
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Deletar Cliente")
        
        campos = [
            ("ID do Cliente:", "id_entry"),
            ("Nome do Cliente:", "name_entry"),
            ("CPF do Cliente:", "cpf_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.delete_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.delete_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_delete = tk.Button(self.delete_window, text="Deletar", command=lambda: self.delete_customer_by_id(
            self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get()))
        btn_delete.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.delete_window, text="Voltar", command=self.delete_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def delete_customer_by_id(self, id, name, cpf):
        deleted = self.customerController.delete_customer_by(id, name, cpf)
        if deleted:
            messagebox.showinfo("Sucesso", "Cliente deletado com sucesso.")
        else:
            messagebox.showinfo("Erro", "Não foi possível deletar o cliente.")
    
        self.create_main_menu()
    
    def update_customer(self):
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Atualizar Cliente")
        
        campos = [
            ("ID do Cliente:", "id_entry"),
            ("Novo Nome do Cliente:", "new_name_entry"),
            ("Novo Telefone do Cliente:", "new_phone_entry"),
            ("Novo Email do Cliente:", "new_email_entry"),
            ("Novo CPF do Cliente:", "new_cpf_entry")
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.update_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.update_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_update = tk.Button(self.update_window, text="Atualizar", command=lambda: self.update_customer_by_id(
            self.id_entry.get(), self.new_name_entry.get(), self.new_phone_entry.get(), self.new_email_entry.get(),
            self.new_cpf_entry.get()))
        btn_update.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.update_window, text="Voltar", command=self.update_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def update_customer_by_id(self, id, new_name, new_phone, new_email, new_cpf):
        updated = self.customerController.update_customer(id, new_name, new_phone, new_email, new_cpf)
        if updated:
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso.")
        else:
            messagebox.showinfo("Erro", "Não foi possível atualizar o cliente.")
            
    def saleMenu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        buttons = [
            ('Adicionar Venda', self.collect_sale_data),
            ('Listar Vendas', self.list_sales),
            ('Buscar Venda', self.search_sales),
            ('Deletar Venda', self.delete_sale),
        ]

        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(self.main_frame, text=text, command=command)
            btn.grid(row=0, column=i, padx=10, pady=5)

        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.grid(row=1, column=0, columnspan=len(buttons), pady=10)
        
    def collect_sale_data(self):
        self.sales_window = tk.Toplevel(self.root)
        self.sales_window.title("Adicionar Venda")
        
        campos = [
            ("ID da Venda:", "id_entry"),
            ("ID do Cliente:", "customer_id_entry"),
            ("Data da Venda (DD/MM/AAAA):", "date_entry"),
            ("ID dos Produtos (separados por vírgula):", "products_entry"),
            ("Quantidades dos Produtos (separados por vírgula):", "quantities_entry"),
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.sales_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.sales_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)  # Define o atributo dinamicamente
        
        btn_save = tk.Button(self.sales_window, text="Salvar", command=self.save_sale)
        btn_save.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
    def save_sale(self):
        campos = [
            ("id_entry", "id"),
            ("customer_id_entry", "customerId"),
            ("date_entry", "date"),
            ("products_entry", "products"),
            ("quantities_entry", "quantities")
        ]
        
        venda = {}
        for entry_attr, key in campos:
            value = getattr(self, entry_attr).get()
            if not value:
                # Handle empty value
                value = None
            venda[key] = value
        
        self.saleController.add_sale(**venda)
        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        self.sales_window.destroy()
        
    def list_sales(self):
        self.clear_main_frame()
        
        sales = self.saleController.list_sales()
        
        if not sales:
            tk.Label(self.main_frame, text="Nenhuma venda cadastrada.").pack(pady=20)
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
            return
        
        for sale in sales:
            sale_info = f"ID: {sale['id']}, Cliente: {sale['customerId']}, Data: {sale['date']}"
            tk.Label(self.main_frame, text=sale_info).pack(pady=5)
        
        btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
        btn_back.pack(pady=10)
        
    def search_sales(self):
        self.search_window = tk.Toplevel(self.root)
        self.search_window.title("Buscar Venda")
        
        campos = [
            ("ID da Venda:", "id_entry"),
            ("ID do Cliente:", "customer_id_entry"),
            ("Data da Venda (DD/MM/AAAA):", "date_entry"),
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.search_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.search_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_search = tk.Button(self.search_window, text="Buscar", command=lambda: self.display_search_results_sale(
            self.id_entry.get(), self.customer_id_entry.get(), self.date_entry.get()))
        btn_search.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.search_window, text="Voltar", command=self.search_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def display_search_results_sale(self, id, customer_id, date):
        if not (results := self.saleController.search_sales_by(id, customer_id, date)):
            messagebox.showinfo("Nenhuma Venda Encontrada", "Nenhuma venda encontrada com os critérios fornecidos.")
        else:
            self.clear_main_frame()
            for sale in results:
                sale_info = f"ID: {sale['id']}, Cliente: {sale['customerId']}, Data: {sale['date']}"
                tk.Label(self.main_frame, text=sale_info).pack(pady=5)
    
            btn_back = tk.Button(self.main_frame, text="Voltar", command=self.create_main_menu)
            btn_back.pack(pady=10)
        
    def delete_sale(self):
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Deletar Venda")
        
        campos = [
            ("ID da Venda:", "id_entry"),
            ("ID do Cliente:", "customer_id_entry"),
            ("Data da Venda (DD/MM/AAAA):", "date_entry"),
        ]
        
        for i, (label_text, entry_attr) in enumerate(campos):
            tk.Label(self.delete_window, text=label_text).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.delete_window)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, entry_attr, entry)
            
        btn_delete = tk.Button(self.delete_window, text="Deletar", command=lambda: self.delete_sale_by_id(
            self.id_entry.get()))
        btn_delete.grid(row=len(campos), column=0, columnspan=2, pady=10)
        
        btn_back = tk.Button(self.delete_window, text="Voltar", command=self.delete_window.destroy)
        btn_back.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)
        
    def delete_sale_by_id(self, id):
        if (deleted := self.saleController.delete_sale_by_id(id)):
            messagebox.showinfo("Sucesso", "Venda deletada com sucesso.")
        else:
            messagebox.showinfo("Erro", "Não foi possível deletar a venda.")
            
        self.create_main_menu()
    
    
    
def main():
    root = tk.Tk()
    SuzukaMain(root)
    root.mainloop()

if __name__ == "__main__":
    sv_ttk.set_theme("dark")
    main()