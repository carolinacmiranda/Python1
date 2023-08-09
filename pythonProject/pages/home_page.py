import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.pagina_logada = (By.XPATH, "//*[contains(text(), 'Análise geral')]")
        self.botao_criar_robo = (By.XPATH, "//*[contains(text(), 'Criar Robô')]")
        self.criacao_facil = (By.XPATH, "//*[contains(text(), 'Escolher Robô')]")
        self.robo_dourado = (By.XPATH, "(//*[contains(text(), 'Criar')])[2]")
        self.modo_simulado = (By.XPATH, "(//sb-button[@data-testid='button'][contains(.,'Configurar')])[1]")
        self.botao_play = (By.XPATH, "(//*[contains(text(), 'Play')])")
        self.botao_segundo_play = (By.XPATH, "//sb-button[contains(@data-testid,'play-button')]")
        self.criacao_completa = (By.XPATH, "//sb-button[@type='solid'][contains(.,'Configurar')]")
        self.robo_sardinha = (By.XPATH, "//div[@class='truncate'][contains(.,'SardinhaAutor: SmarttBot')]")
        self.botao_avancar = (By.XPATH, "//sb-button[@type='link'][contains(.,'Avançar')]")
        self.botao_salvar = (By.XPATH, "//button[contains(@aria-label,'Salvar')]")
        self.modal_salvar = (By.XPATH, "//button[@class='jss171 jss756 jss758 jss759 jss761 jss762'][contains(.,'Salvar')]")
        self.botao_iniciar = (By.XPATH, "//button[contains(@aria-label,'Iniciar')]")
        self.verificar_status = (By.XPATH, "(//*[contains(text(), 'Executando')])[2]")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.pagina_logada)

    def criar_robo_modo_facil(self, text):
        self.clicar(self.botao_criar_robo)
        self.clicar(self.criacao_facil)
        self.clicar(self.robo_dourado)
        self.clicar(self.modo_simulado)
        self.preencher_nome_robo_shadow(text)
        self.clicar(self.botao_play)
        self.clicar_modal_confirmacao()
        self.realizar_hover(self.botao_segundo_play)

    def criar_robo_modo_completo(self, text):
        self.clicar(self.botao_criar_robo)
        self.clicar(self.criacao_completa)
        self.clicar(self.robo_sardinha)
        self.clicar(self.modo_simulado)
        self.preencher_nome_robo_shadow(text)
        self.clicar(self.botao_avancar)
        self.clicar(self.botao_salvar)
        self.clicar_modal_confirmacao()

    def verificar_status_do_robo(self):
        self.verificar_se_elemento_existe(self.verificar_status)
