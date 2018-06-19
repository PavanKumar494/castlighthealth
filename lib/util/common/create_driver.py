from selenium.webdriver import Chrome, Firefox, Ie
import pytest


def get_browser_instance():
    browser_type = pytest.config.option.browser
    env = pytest.config.option.env
    if env == "remote":
        if browser_type == "firefox":
            browser = Firefox(executable_path="E:\Pavan\geckodriver-v0.20.1-win64\geckodriver")
        elif browser_type == "chrome":
            browser = Chrome(executable_path="E:\Pavan\chromedriver_win32\chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get("https://us.castlighthealth.com")
    return browser
    # else:
