

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
            print("Registration failed.")
    
    #To confirm the user name and the password are correct 
    # and so facilitate a first timer Log-Ins and future logins
    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False
    
    def confirm_password(self, password):
        if password == self.password:
            return "Password confirmed."
        else:
            return "Passwords do not match."
        

        #firstUser = User("Merlin", "password14")

        # print(first_user.confirm_password("password14")) # "Password confirmed."
        # print(first_user.confirm_password("34ftg")) # "Passwords do not match."


            print("Invalid login credentials")
