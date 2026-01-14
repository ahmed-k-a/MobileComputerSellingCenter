from entity.user import User

class AuthenticationController:
    def __init__(self):
        # Hardcoded user for simplicity
        self.user = User("admin", "1234")

    def validate_login(self, username, password):
        return self.user.verify_credentials(username, password)
