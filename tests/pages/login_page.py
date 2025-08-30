from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "/home.html"  # Page Object maps a page's URL

    def __init__(self, driver, base_url="http://localhost:8000"):
        self.driver = driver
        self.base_url = base_url
        # Standard POM: keep locators centralized in the page class
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "loginBtn")
        self.error = (By.ID, "error")

    def load(self):
        # Navigation lives inside the page object
        self.driver.get(self.base_url + self.URL)

    def login(self, username, password, timeout=8):
        # Explicit wait ensures stability vs. brittle sleeps
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.username))
        self.driver.find_element(*self.username).clear()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).clear()
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def get_error_text(self, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.error))
            return self.driver.find_element(*self.error).text
        except:
            return ""