class LoginUI:
    def get_credentials(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username, password

    def show_success(self):
        print("Login successful!")

    def show_error(self):
        print("Invalid username or password.")
