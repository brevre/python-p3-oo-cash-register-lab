class CashRegister:
    def __init__(self, discount=0):  
        self.discount = discount  
        self.total = 0  
        self.items = []  
        self.last_transaction = 0  

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item_name] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount

            # Force output format to match expected test case
            formatted_total = f"{int(self.total)}" if self.total.is_integer() else f"{self.total:.2f}"
            print(f"After the discount, the total comes to ${formatted_total}.")

        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items
