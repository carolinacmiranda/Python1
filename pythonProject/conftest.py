import pytest

from selenium import webdriver

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://app.smarttbot.com")

    # run test
    driver.implicitly_wait(10)
    yield
    driver.implicitly_wait(10)

    # teardown
    driver.quit()
