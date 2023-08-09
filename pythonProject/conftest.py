import pytest

from selenium import webdriver

# Indicando a URL do serviço remoto do Selenium
REMOTE_URL = "http://localhost:4444/wd/hub"


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    options = webdriver.ChromeOptions()

    # Configurando o driver para usar o serviço remoto
    driver = webdriver.Remote(command_executor=REMOTE_URL, desired_capabilities=options.to_capabilities())

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://app.smarttbot.com")

    # run test
    driver.implicitly_wait(10)
    yield
    driver.implicitly_wait(10)

    # teardown
    driver.quit()
