from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self,browser):
        self.browser = browser

    def wait_for_page_load(self):
        wait = WebDriverWait(self.browser,30)
        wait.until(expected_conditions.title_contains('Castlight - Sign In'))

    def get_register_button(self):
        try:
            return self.browser.find_element_by_xpath("(//a[contains(text(),'Register')])[1]")
        except:
            return None



