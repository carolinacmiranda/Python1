import pytest

from pythonProject.pages.home_page import HomePage
from pythonProject.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT01:
    def test_ct01_login_valido(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("automated01", "Testing202")
        home_page.verificar_login_com_sucesso()
