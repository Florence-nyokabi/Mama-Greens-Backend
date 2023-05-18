class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def register(self):
        new_user = User(self,name,password,email)
        return new_user
    def login(self, email, password):
        # method to authenticate user's login credentials
        if self.email == email and self.password == password:
            print("Login successful!")
        else:
            print("Invalid login credentials")