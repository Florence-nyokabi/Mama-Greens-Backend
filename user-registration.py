class User:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")
    user = User(name, email, password, address)
    return user

def authenticate(users):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.password == password:
            print("Authentication successful!")
            return True
    print("Authentication failed!")
    return False