import pytest
from selenium import webdriver
from library.config import Config





@pytest.fixture(params=["Chrome"])#,"firefox"])#, "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH)

    elif browser.lower() == "firefox":

        driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH)

    else:
        driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.close()

