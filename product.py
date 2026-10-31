

class product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def displayinfo(self):

        print(
                f"ID: {self.id} | "
                f"Product: {self.name} | "
                f"Price: {self.price:.2f} | "
                f"Stock: {self.stock}"
            )
        pass

    def updatestock(self):
        try:
            new_stock = int(input("Enter the new stock quantity: "))
            if new_stock < 0:
                print("Invalid input. Please enter a positive number for stock.")
                return
            
            elif new_stock > 500:
                print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                return
            
            self.stock = new_stock
            print("\nStock updated successfully.")
            print(f"Stock for product ID {self.id} updated to {new_stock}.\n")
            return
        
        except ValueError:
            print("Invalid input. Please enter a valid stock quantity.")
            return




        pass
