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
        # Criar uma nova janela para coletar dados do produto
        self.product_window = tk.Toplevel(self.root)
        self.product_window.title("Adicionar Produto")

        # Labels e Entradas para os dados do produto
        tk.Label(self.product_window, text="ID do Produto:").grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(self.product_window)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Nome do Produto:").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.product_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Preço do Produto:").grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.product_window)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Número da Peça:").grid(row=3, column=0, padx=10, pady=5)
        self.part_number_entry = tk.Entry(self.product_window)
        self.part_number_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Estoque do Produto:").grid(row=4, column=0, padx=10, pady=5)
        self.stock_entry = tk.Entry(self.product_window)
        self.stock_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Categoria do Produto:").grid(row=5, column=0, padx=10, pady=5)
        self.category_entry = tk.Entry(self.product_window)
        self.category_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Preço de Fábrica:").grid(row=6, column=0, padx=10, pady=5)
        self.factory_price_entry = tk.Entry(self.product_window)
        self.factory_price_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Fabricante:").grid(row=8, column=0, padx=10, pady=5)
        self.manufacturer_entry = tk.Entry(self.product_window)
        self.manufacturer_entry.grid(row=8, column=1, padx=10, pady=5)

        tk.Label(self.product_window, text="Descrição:").grid(row=9, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(self.product_window)
        self.description_entry.grid(row=9, column=1, padx=10, pady=5)

        # Botão para salvar os dados do produto
        btn_save = tk.Button(self.product_window, text="Salvar", command=self.save_product)
        btn_save.grid(row=10, column=0, columnspan=2, pady=10)
        
    def save_product(self):
        # Coletar dados dos campos de entrada
        id = self.id_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        part_number = self.part_number_entry.get()
        stock = self.stock_entry.get()
        category = self.category_entry.get()
        factory_price = self.factory_price_entry.get()
        manufacturer = self.manufacturer_entry.get()
        description = self.description_entry.get()

        # Verificar se todos os campos foram preenchidos
        if id and name and price and part_number and stock and category and factory_price and manufacturer and description:
            # Chamar o método add do ProductController com os dados coletados
            self.productController.add_product(id, name, price, part_number, stock, category, factory_price, manufacturer, description)
            messagebox.showinfo("Produto Adicionado", f"Produto '{name}' cadastrado com sucesso")
            self.product_window.destroy()  # Fechar a janela após salvar
            self.productMenu()  # Atualizar o menu de produtos
        else:
            messagebox.showwarning("Dados Incompletos", "Todos os campos são obrigatórios!")
            
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
        # Criar uma nova janela para coletar dados do cliente
        self.customer_window = tk.Toplevel(self.root)
        self.customer_window.title("Adicionar Cliente")

        # Labels e Entradas para os dados do cliente
        tk.Label(self.customer_window, text="ID do Cliente:").grid(row=0, column=0, padx=10, pady=5)
        self.id_entry = tk.Entry(self.customer_window)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.customer_window, text="Nome do Cliente:").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.customer_window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.customer_window, text="Telefone do Cliente:").grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.customer_window)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.customer_window, text="Email do Cliente:").grid(row=3, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.customer_window)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.customer_window, text="CPF do Cliente:").grid(row=4, column=0, padx=10, pady=5)
        self.cpf_entry = tk.Entry(self.customer_window)
        self.cpf_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botão para salvar os dados do cliente
        btn_save = tk.Button(self.customer_window, text="Salvar", command=self.save_customer)
        btn_save.grid(row=5, column=0, columnspan=2, pady=10)

    def save_customer(self):
        # Coletar dados dos campos de entrada
        id = self.id_entry.get()
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        cpf = self.cpf_entry.get()

        # Verificar se todos os campos foram preenchidos
        if id and name and phone and email and cpf:
            # Chamar o método add_customer do CustomerController com os dados coletados
            self.customerController.add_customer(id, name, phone, email, cpf)
            messagebox.showinfo("Cliente Adicionado", f"Cliente '{name}' cadastrado com sucesso")
            self.customer_window.destroy()  # Fechar a janela após salvar
            self.customerMenu()  # Atualizar o menu de clientes
        else:
            messagebox.showwarning("Dados Incompletos", "Todos os campos são obrigatórios!")

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
