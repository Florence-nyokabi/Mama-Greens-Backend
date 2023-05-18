<<<<<<< HEAD
class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    def register(self):
        new_user = User(self,name,password,email)
        return new_user
    def login(self, email, password):
        if self.email == email and self.password == password:
            print("Login successful!")
        else:
            print("Invalid login credentials")
=======
   import re

class SignUp:

    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_password(self):
        if len(self.password) < 8:
            print("Password must be at least 8 characters long.")
            return False

        if not re.search("[a-z]", self.password):
            print("Password must contain at least one lowercase letter.")
            return False

        if not re.search("[A-Z]", self.password):
            print("Password must contain at least one uppercase letter.")
            return False
        
        if not re.search("[0-9]", self.password):
            print("Password must contain at least one digit.")
            return False

        if not re.search("[@#$%^&+=]", self.password):
            print("Password must contain at least one special character among @#$%^&+=" )
            return False
        
        if self.password != self.confirm_password:
            print("Password and Confirm Password do not match.")
            return False

        return True

    def validate_email(self):
        pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, self.email):
            return True
        else:
            print("Invalid email address.")
            return False

    def register(self):
        if self.validate_email() and self.validate_password():
            print("User registered successfully!")
        else:
            print("Registration failed.")
>>>>>>> 0858b70a4c8dac5e4ab9e8f24aae337bab394fbd
