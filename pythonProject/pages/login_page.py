import conftest

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "login-username")
        self.password_field = (By.ID, "login-password")
        self.login_button = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        self.digitar(self.username_field, usuario)
        self.digitar(self.password_field, senha)
        self.clicar(self.login_button)
