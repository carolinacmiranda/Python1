import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.criar_robo_modo_facil
class TestCT02:
    def test_ct02_criar_robo_modo_facil(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("automated01", "Testing202")
        home_page.criar_robo_modo_facil("Dourado")
