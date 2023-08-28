import pytest
from selenium import webdriver

# Indicando a URL do serviço remoto do Selenium
# REMOTE_URL = "http://localhost:4444"
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
   # options = webdriver.ChromeOptions()

    driver = webdriver.Chrome()

    # Configurando o driver para usar o serviço remoto
   # driver = webdriver.Remote(command_executor=REMOTE_URL, options=options)

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://app.smarttbot.com")

    # run test
    yield

    # teardown
    driver.quit()
