from flask import Flask, render_template, request, redirect
from ProductController import ProductController
from CustomerController import CustomerController
from SaleController import SaleController
from ReportController import ReportController
from Supplier import SupplierController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    product_controller = ProductController()
    products = product_controller.list()
    return render_template('products.html', products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        price = request.form['price']
        product_controller = ProductController()
        product_controller.add(id, name, price)
        return redirect('/products')
    return render_template('add_product.html')

@app.route('/products/delete/<id>')
def delete_product(id):
    product_controller = ProductController()
    product_controller.delete(id)
    return redirect('/products')

@app.route('/products/update/<id>', methods=['GET', 'POST'])
def update_product(id):
    product_controller = ProductController()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        product_controller.update(id, name, price)
        return redirect('/products')
    product = product_controller.search(id)
    return render_template('update_product.html', product=product)

@app.route('/customers')
def customers():
    customer_controller = CustomerController()
    customers = customer_controller.list()
    return render_template('customers.html', customers=customers)

@app.route('/customers/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        customer_controller = CustomerController()
        customer_controller.add(id, name)
        return redirect('/customers')
    return render_template('add_customer.html')

@app.route('/customers/delete/<id>')
def delete_customer(id):
    customer_controller = CustomerController()
    customer_controller.delete(id)
    return redirect('/customers')

@app.route('/customers/update/<id>', methods=['GET', 'POST'])
def update_customer(id):
    customer_controller = CustomerController()
    if request.method == 'POST':
        name = request.form['name']
        customer_controller.update(id, name)
        return redirect('/customers')
    customer = customer_controller.search(id)
    return render_template('update_customer.html', customer=customer)

@app.route('/sales')
def sales():
    sale_controller = SaleController()
    sales = sale_controller.list()
    return render_template('sales.html', sales=sales)

@app.route('/sales/add', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        id = request.form['id']
        product_id = request.form['product_id']
        customer_id = request.form['customer_id']
        quantity = request.form['quantity']
        sale_controller = SaleController()
        sale_controller.add(id, product_id, customer_id, quantity)
        return redirect('/sales')
    return render_template('add_sale.html')

@app.route('/sales/delete/<id>')
def delete_sale(id):
    sale_controller = SaleController()
    sale_controller.delete(id)
    return redirect('/sales')

@app.route('/sales/update/<id>', methods=['GET', 'POST'])
def update_sale(id):
    sale_controller = SaleController()
    if request.method == 'POST':
        product_id = request.form['product_id']
        customer_id = request.form['customer_id']
        quantity = request.form['quantity']
        sale_controller.update(id, product_id, customer_id, quantity)
        return redirect('/sales')
    sale = sale_controller.search(id)
    return render_template('update_sale.html', sale=sale)

@app.route('/suppliers')
def suppliers():
    supplier_controller = SupplierController()
    suppliers = supplier_controller.list()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/suppliers/add', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        productType = request.form['productType']
        cnpj = request.form['cnpj']
        supplier_controller = SupplierController()
        supplier_controller.add(id, name, phone, address, productType, cnpj)
        return redirect('/suppliers')
    return render_template('add_supplier.html')

@app.route('/suppliers/delete/<id>')
def delete_supplier(id):
    supplier_controller = SupplierController()
    supplier_controller.delete(id)
    return redirect('/suppliers')

@app.route('/suppliers/update/<id>', methods=['GET', 'POST'])
def update_supplier(id):
    supplier_controller = SupplierController()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        productType = request.form['productType']
        cnpj = request.form['cnpj']
        supplier_controller.update(id, name, phone, address, productType, cnpj)
        return redirect('/suppliers')
    supplier = supplier_controller.search(id)
    return render_template('update_supplier.html', supplier=supplier)

@app.route('/reports')
def reports():
    report_controller = ReportController()
    return render_template('reports.html')

@app.route('/reports/products')
def report_products():
    report_controller = ReportController()
    products = report_controller.list_products()
    return render_template('report_products.html', products=products)

@app.route('/reports/customers')
def report_customers():
    report_controller = ReportController()
    customers = report_controller.list_customers()
    return render_template('report_customers.html', customers=customers)

@app.route('/reports/sales')
def report_sales():
    report_controller = ReportController()
    sales = report_controller.list_sales()
    return render_template('report_sales.html', sales=sales)

@app.route('/reports/sales/<customer_id>')
def report_sales_by_customer(customer_id):
    report_controller = ReportController()
    sales = report_controller.list_sales_by_customer(customer_id)
    return render_template('report_sales.html', sales=sales)

@app.route('/reports/sales/<product_id>')
def report_sales_by_product(product_id):
    report_controller = ReportController()
    sales = report_controller.list_sales_by_product(product_id)
    return render_template('report_sales.html', sales=sales)

@app.route('/reports/sales/date/<date>')
def report_sales_by_date(date):
    report_controller = ReportController()
    sales = report_controller.list_sales_by_date(date)
    return render_template('report_sales.html', sales=sales)

@app.route('/reports/sales/date/<start_date>/<end_date>')
def report_sales_by_date_range(start_date, end_date):
    report_controller = ReportController()
    sales = report_controller.list_sales_by_date_range(start_date, end_date)
    return render_template('report_sales.html', sales=sales)

@app.route('/reports/sales/total')
def report_sales_total():
    report_controller = ReportController()
    total = report_controller.get_sales_total()
    return render_template('report_sales_total.html', total=total)

@app.route('/reports/sales/total/<customer_id>')
def report_sales_total_by_customer(customer_id):
    report_controller = ReportController()
    total = report_controller.get_sales_total_by_customer(customer_id)
    return render_template('report_sales_total.html', total=total)

@app.route('/reports/sales/total/<product_id>')
def report_sales_total_by_product(product_id):
    report_controller = ReportController()
    total = report_controller.get_sales_total_by_product(product_id)
    return render_template('report_sales_total.html', total=total)

@app.route('/reports/sales/total/date/<date>')
def report_sales_total_by_date(date):
    report_controller = ReportController()
    total = report_controller.get_sales_total_by_date(date)
    return render_template('report_sales_total.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
    