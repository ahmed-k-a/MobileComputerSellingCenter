from ui.login_ui import LoginUI
from ui.product_ui import ProductUI
from controller.authentication_controller import AuthenticationController
from controller.product_controller import ProductController

# Initialize components
login_ui = LoginUI()
auth_controller = AuthenticationController()
product_ui = ProductUI()
product_controller = ProductController()

# LOGIN USE CASE
username, password = login_ui.get_credentials()

if auth_controller.validate_login(username, password):
    login_ui.show_success()

    # MANAGE PRODUCTS USE CASE
    name, price, quantity = product_ui.get_product_details()
    product_controller.add_product(name, price, quantity)

    products = product_controller.get_products()
    product_ui.display_products(products)
else:
    login_ui.show_error()
