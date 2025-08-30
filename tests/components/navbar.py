from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavBar:
    # A reusable UI component (visible across multiple pages)
    def __init__(self, driver):
        self.driver = driver
        self.profile = (By.ID, "profile")

    def go_to_profile(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.profile))
        self.driver.find_element(*self.profile).click()