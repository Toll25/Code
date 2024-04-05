import mariadb
import json
from bson import ObjectId

def convert_to_json(db_host, db_user, db_password, db_name):
    conn = mariadb.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cur = conn.cursor()

    # Save data from suppliers table
    cur.execute("SELECT * FROM suppliers")
    suppliers = []
    for row in cur.fetchall():
        supplier = {}
        supplier["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            supplier[cur.description[i][0]] = entry
        suppliers.append(supplier)

    # Save data from categories table
    cur.execute("SELECT * FROM categories")
    categories = []
    for row in cur.fetchall():
        category = {}
        category["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            category[cur.description[i][0]] = entry
        categories.append(category)

    # Save data from customers table
    cur.execute("SELECT * FROM customers")
    customers = []
    for row in cur.fetchall():
        customer = {}
        customer["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            if cur.description[i][0] == "BirthDate":
                entry = entry.strftime('%Y-%m-%dT%H:%M:%S')

            customer[cur.description[i][0]] = entry
        customers.append(customer)

    # Save data from employees table
    cur.execute("SELECT * FROM employees")
    employees = []
    for row in cur.fetchall():
        employee = {}
        employee["_id"] = str(ObjectId())
        for i, entry in enumerate(row):

            if cur.description[i][0] == "BirthDate":
                entry = entry.strftime('%Y-%m-%dT%H:%M:%S')
            employee[cur.description[i][0]] = entry
        employees.append(employee)

    # Save data from shippers table
    cur.execute("SELECT * FROM shippers")
    shippers = []
    for row in cur.fetchall():
        shipper = {}
        shipper["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            shipper[cur.description[i][0]] = entry
        shippers.append(shipper)

    # Save data from orders table
    cur.execute("SELECT * FROM orders")
    orders = []
    for row in cur.fetchall():
        order = {}
        order["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            column_name = cur.description[i][0]
            if column_name == "OrderDate":
                order[column_name] = entry.strftime('%Y-%m-%dT%H:%M:%S')
            elif column_name == "CustomerID":
                order["Customer"] = str(
                    [customer["_id"] for customer in customers if customer["CustomerID"] == entry][0])
            elif column_name == "EmployeeID":
                order["Employee"] = str(
                    [employee["_id"] for employee in employees if employee["EmployeeID"] == entry][0])
            elif column_name == "ShipperID":
                order["Shipper"] = str(
                    [shipper["_id"] for shipper in shippers if shipper["ShipperID"] == entry][0])
            else:
                order[column_name] = entry
        orders.append(order)

    # Save data from products table
    cur.execute("SELECT * FROM products")
    products = []
    for row in cur.fetchall():
        product = {}
        product["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            column_name = cur.description[i][0]
            if column_name == "SupplierID":
                product["Supplier"] = str([supplier["_id"] for supplier in suppliers if supplier["SupplierID"] == entry][0])
            elif column_name == "CategoryID":
                product["Category"] = str(
                    [category["_id"] for category in categories if category["CategoryID"] == entry][0])
            else:
                product[column_name] = entry
        products.append(product)

    # Save data from order_details table with references
    cur.execute("SELECT * FROM order_details")
    order_details = []
    for row in cur.fetchall():
        order_detail = {}
        order_detail["_id"] = str(ObjectId())
        for i, entry in enumerate(row):
            column_name = cur.description[i][0]
            if column_name == "OrderID":
                order_detail["Order"] = str([order["_id"] for order in orders if order["OrderID"] == entry][0])
            elif column_name == "ProductID":
                order_detail["Product"] = str([product["_id"] for product in products if product["ProductID"] == entry][0])
            else:
                order_detail[column_name] = entry
        order_details.append(order_detail)

    # Combine all collections into a single dictionary
    data = {
        "suppliers": suppliers,
        "categories": categories,
        "customers": customers,
        "employees": employees,
        "shippers": shippers,
        "orders": orders,
        "products": products,
        "order_details": order_details
    }

    # Write documents to JSON file
    with open('data.json', 'w') as json_file:
        for collection_name, collection_data in data.items():
            for doc in collection_data:
                json.dump(doc, json_file)
                json_file.write('\n')

    conn.close()

convert_to_json('localhost', 'root', ':)', 'w3schools')
