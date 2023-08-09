from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def digitar(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed()

    def verificar_mensagem_de_sucesso(self, locator):
        return self.encontrar_elemento(locator).text

    def preencher_nome_robo_shadow(self, text):
        shadow_root = self.driver.find_element(By.CSS_SELECTOR, "sb-input-text[data-testid='robot-name']").shadow_root
        shadow_root.find_element(By.CSS_SELECTOR, "input[id='Tm9tZSBkbyBSb2L0']").send_keys(text)

    def clicar_modal_confirmacao(self):
        modal_confirmacao = self.driver.switch_to.active_element
        modal_confirmacao.send_keys(Keys.RETURN)

    def realizar_hover(self, locator):
        element_to_hover = self.encontrar_elemento(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover).perform()
