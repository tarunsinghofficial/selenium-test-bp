from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    URL = "/dashboard.html"

    def __init__(self, driver, base_url="http://localhost:8000"):
        self.driver = driver
        self.base_url = base_url
        # Page-specific locators
        self.dashboard_header = (By.ID, "dashboard")
        self.action_btn = (By.ID, "actionBtn")

    def is_loaded(self, timeout=6):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self.dashboard_header))
        return self.driver.find_element(*self.dashboard_header).is_displayed()

    def click_action(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.action_btn))
        self.driver.find_element(*self.action_btn).click()