import filehandling
import product

class inventory:
    def __init__(self):
        self.products = []

        # Load products from JSON only once when inventory is created
        file_handling = filehandling.filehandling()
        file_handling.load_inventory()

        for product_data in file_handling.productdetail["products"]:
            product_obj = product.product(
                id=product_data["ID"],
                name=product_data["name"],
                price=product_data["price"],
                stock=product_data["stock"]
            )
            self.products.append(product_obj)

    def storesproduct(self):
        # Save the current product objects to JSON
        file_handling = filehandling.filehandling()
        file_handling.save_inventory(self.products)

    def addproduct(self):
        # Validate product ID
        try:
            add_id = int(input("Enter the product ID: "))

            for item in self.products:
                if item.id == add_id:
                    print("Product ID already exists. Please enter a unique product ID.")
                    return

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            return

        # Validate product name
        add_product = input("Enter the product name: ").strip()

        if not add_product:
            print("Invalid input. Product name cannot be empty.")
            return

        # Validate price
        try:
            add_price = float(input("Enter the product price: "))

            if add_price <= 0:
                print("Invalid input. Please enter a positive number for price.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid product price.")
            return

        # Validate stock
        try:
            add_stock = int(input("Enter the product stock: "))

            if add_stock <= 0:
                print("Invalid input. Please enter a positive number for stock.")
                return

            if add_stock > 500:
                print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid product stock.")
            return

        # Create a product object and add it to the existing list
        new_product = product.product(add_id, add_product, add_price, add_stock)
        self.products.append(new_product)

        print("Product added successfully!")

    def updateproduct(self):

        try:
            update_id = int(input("Enter the product ID to update: "))
            for item in self.products:
                if item.id == update_id:
                    item.updatestock()
                    pass
                    
            print("Product ID not found.")

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
        pass

    def searchproduct(self):

        try:
            search_id = int(input("Enter the product ID to search: "))
            for item in self.products:
                if item.id == search_id:
                    print("===========================================================================")
                    print(f"Product found: ID: {item.id} | Name: {item.name} | Price: {item.price} | Stock: {item.stock}")
                    print("===========================================================================")
                    return
            print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
        pass

