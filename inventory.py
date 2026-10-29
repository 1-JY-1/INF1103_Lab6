import filehandling

class product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock


class inventory:
    def __init__(self):
        self.products = []

        # Load products from JSON only once when inventory is created
        file_handling = filehandling.filehandling()
        file_handling.load_inventory()

        for product_data in file_handling.productdetail["products"]:
            product_obj = product(
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
        new_product = product(add_id, add_product, add_price, add_stock)
        self.products.append(new_product)

        print("Product added successfully!")

    def updateproduct(self):

        try:
            update_id = int(input("Enter the product ID to update: "))
            for item in self.products:
                if item.id == update_id:
                    try:
                        new_stock = int(input("Enter the new stock quantity: "))
                        if new_stock < 0:
                            print("Invalid input. Please enter a positive number for stock.")
                            return

                        elif new_stock > 500:
                            print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                            return

                        item.stock = new_stock
                        print("\nStock updated successfully.")
                        print(f"Stock for product ID {update_id} updated to {new_stock}.\n")
                        return

                    except ValueError:
                        print("Invalid input. Please enter a valid stock quantity.")
                        return
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


class mainprogram:
    def __init__(self):
        # Create one inventory object
        self.inventory = inventory()

    def getuserinput(self, user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            return
        
        if user_input == 1:
            print("\nCurrent Inventory")
            print("===========================================================================")
            if not self.inventory.products:
                print("No products found.")
            else:
                for product_obj in self.inventory.products:
                    print(
                        f"ID: {product_obj.id} | "
                        f"Product: {product_obj.name} | "
                        f"Price: {product_obj.price:.2f} | "
                        f"Stock: {product_obj.stock}"
                    )
            print("===========================================================================")

        elif user_input == 2:
            print("===========================================================================")
            print("Add a new product to the inventory")
            self.inventory.addproduct()
            print("===========================================================================")

        elif user_input == 3:
            print("===========================================================================")
            print("Update the stock of the product")
            self.inventory.updateproduct()
            print("===========================================================================")

        elif user_input == 4:
            print("===========================================================================")
            print("Search for the product")
            self.inventory.searchproduct()
            print("===========================================================================")

        elif user_input == 5:
            print("===========================================================================")
            print("Save Inventory")
            self.inventory.storesproduct()
            print("===========================================================================")

        elif user_input == 6:
            print("===========================================================================")
            print("Quit the app")

        else:
            print("Invalid input. Please enter a number between 1 and 6.")

























































# import filehandling

# class product:
#     def __init__(self, id, name, price, stock):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.stock = stock


# class inventory:
#     def __init__(self):
#         self.products = []


#     def storesproduct():
#         pass

#     def addproduct(self):
#         # Get and validate product ID
#         try:
#             add_id = int(input("Enter the product ID: "))

#             for item in self.products:
#                 if item.id == add_id:
#                     print("Product ID already exists. Please enter a unique product ID.")
#                     return

#         except ValueError:
#             print("Invalid input. Please enter a valid product ID.")
#             return

#         # Get product name
#         add_product = input("Enter the product name: ").strip()

#         if not add_product:
#             print("Invalid input. Product name cannot be empty.")
#             return

#         # Get and validate price
#         try:
#             add_price = float(input("Enter the product price: "))

#             if add_price <= 0:
#                 print("Invalid input. Please enter a positive number for price.")
#                 return

#         except ValueError:
#             print("Invalid input. Please enter a valid product price.")
#             return

#         # Get and validate stock
#         try:
#             add_stock = int(input("Enter the product stock: "))

#             if add_stock <= 0:
#                 print("Invalid input. Please enter a positive number for stock.")
#                 return

#             elif add_stock > 500:
#                 print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
#                 return

#         except ValueError:
#             print("Invalid input. Please enter a valid product stock.")
#             return

#         # Create a product object
#         new_product = product(add_id, add_product, add_price, add_stock)

#         # Add the product object to the list
#         self.products.append(new_product)

#         print("Product added successfully!")


#     def searchproduct():
#         pass

#     def displayproduct(self):
#         self.products.clear()
#         file_handling = filehandling.filehandling()
#         file_handling.load_inventory()
#         for product_data in file_handling.productdetail["products"]:
#             product_obj = product(
#                 id = product_data["ID"],
#                 name = product_data["name"],
#                 price = product_data["price"],
#                 stock = product_data["stock"]
#             )
#             self.products.append(product_obj)


# class mainprogram:

#     def __init__(self):
#         self.inventory = inventory()
#         self.inventory.displayproduct()


#     def getuserinput(self, user_input):
#         print(user_input)
#         try:
#             user_input = int(user_input)
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 6.")
#             # return False, inventory, rejectedEntries

#         if user_input == 1:

#             print("\nCurrent Inventory")
#             print("===========================================================================")
#             for product_obj in self.inventory.products:

#                 print(f"ID: {product_obj.id} | Product: {product_obj.name} | Price: {product_obj.price} | Stock: {product_obj.stock}")
#             print("===========================================================================")
#             # return False, inventory, rejectedEntries

#         elif user_input == 2:

#             print("Add a new product to the inventory")
#             self.inventory.addproduct()

#             # inventory, rejectedEntries = add_item_to_inventory(inventory, rejectedEntries)

#             # return False, inventory, rejectedEntries
    
#         elif user_input == 3:

#             print("Update the stock of the product")

#             # inventory, rejectedEntries = update_stock(inventory, rejectedEntries)

#             # return False, inventory, rejectedEntries

#         elif user_input == 4:

#             print("search for the product")

#             # search_product(inventory)

#             # return False, inventory, rejectedEntries

#         elif user_input == 5:

#             print("Save Inventory")

#             # inventory = save_inventory(inventory)

#             # return False, inventory, rejectedEntries

#         elif user_input == 6:

#             print("quit the app")
#             # return True, inventory, rejectedEntries

#         else:
#             print("Invalid input. Please enter a number between 1 and 6.")
#             # return False, inventory, rejectedEntries