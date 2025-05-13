import pandas as pd

# Initial product list
products = [
    {"Product ID": 101, "Product Name": "Hydrating Moisturizer", "Category": "Skincare", "Stock": 15, "Selling Price": 50, "Cost Price": 25},
    {"Product ID": 102, "Product Name": "Glow Oil", "Category": "Skincare", "Stock": 10, "Selling Price": 70, "Cost Price": 35},
    {"Product ID": 103, "Product Name": "Beard Oil", "Category": "Haircare", "Stock": 10, "Selling Price": 40, "Cost Price": 20},
    {"Product ID": 104, "Product Name": "Hair Cream", "Category": "Haircare", "Stock": 12, "Selling Price": 35, "Cost Price": 18}
]

# Create the DataFrame
df = pd.DataFrame(products)


def add_new_product():
    try:
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        stock = int(input("Enter Stock Quantity: "))
        selling_price = float(input("Enter Selling Price: "))
        cost_price = float(input("Enter Cost Price: "))

        new_entry = {
            "Product ID": product_id,
            "Product Name": name,
            "Category": category,
            "Stock": stock,
            "Selling Price": selling_price,
            "Cost Price": cost_price
        }

        global df
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        print("✅ Product added successfully!\n")
    except Exception as e:
        print(f"❌ Error: {e}")

def record_sale():
    try:
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter quantity sold: "))
        product = df[df["Product ID"] == product_id]

        if not product.empty and product.iloc[0]["Stock"] >= quantity:
            df.loc[df["Product ID"] == product_id, "Stock"] -= quantity
            profit = (product["Selling Price"].values[0] - product["Cost Price"].values[0]) * quantity
            print(f"✅ Sale recorded! Profit made: ${profit:.2f}")
        else:
            print("❌ Not enough stock or invalid Product ID.")
    except Exception as e:
        print(f"❌ Error: {e}")


def search_filter():
    print("\nSearch by:\n1. Product Name\n2. Category")
    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        name = input("Enter part of product name: ").lower()
        results = df[df["Product Name"].str.lower().str.contains(name)]
    elif choice == "2":
        category = input("Enter category: ").lower()
        results = df[df["Category"].str.lower() == category]
    else:
        print("❌ Invalid option.")
        return

    print("\nSearch Results:")
    print(results if not results.empty else "No matching products found.")

def check_low_stock():
    low_stock_df = df[df["Stock"] <= 5]
    if low_stock_df.empty:
        print("✅ All stocks are above the threshold.")
    else:
        print("\n⚠️ Low Stock Products:")
        print(low_stock_df[["Product Name", "Stock"]])


sales_log = []


def record_sale_with_log():
    try:
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter quantity sold: "))
        product = df[df["Product ID"] == product_id]

        if not product.empty and product.iloc[0]["Stock"] >= quantity:
            df.loc[df["Product ID"] == product_id, "Stock"] -= quantity
            profit = (product["Selling Price"].values[0] - product["Cost Price"].values[0]) * quantity
            sales_log.append({"Product ID": product_id, "Quantity": quantity})
            print(f"✅ Sale recorded! Profit made: ${profit:.2f}")
        else:
            print("❌ Not enough stock or invalid Product ID.")
    except Exception as e:
        print(f"❌ Error: {e}")


def view_sales_trend():
    if not sales_log:
        print("No sales yet.")
        return

    sales_df = pd.DataFrame(sales_log)
    trend = sales_df.groupby("Product ID")["Quantity"].sum().reset_index()
    trend = pd.merge(trend, df[["Product ID", "Product Name"]], on="Product ID", how="left")
    print("\n📊 Sales Trend:")
    print(trend.sort_values(by="Quantity", ascending=False))


def menu():
    while True:
        print("\n🛠 Inventory Management System")
        print("1. Add New Product")
        print("2. Record a Sale")
        print("3. Record Sale with Log (for trend)")
        print("4. Search/Filter Products")
        print("5. Check Low Stock")
        print("6. View Sales Trend")
        print("7. Show All Products")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            add_new_product()
        elif choice == "2":
            record_sale()
        elif choice == "3":
            record_sale_with_log()
        elif choice == "4":
            search_filter()
        elif choice == "5":
            check_low_stock()
        elif choice == "6":
            view_sales_trend()
        elif choice == "7":
            print(df)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("❌ Invalid option. Please try again.")

# Uncomment below to run the menu
# menu()
