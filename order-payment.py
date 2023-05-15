class Customer:
    def __init__(self, name, phone_number, mpesa_balance):
        self.name = name
        self.phone_number = phone_number
        self.mpesa_balance = mpesa_balance

    def display_balance(self):
        print("Your current mobile money balance is:", self.mpesa_balance)

    def make_payment(self, amount):
        if amount > self.mpesa_balance:
            print("Insufficient funds.")
        else:
            self.mpesa_balance -= amount
            print("Payment successful. Your new balance is:", self.mpesa_balance)