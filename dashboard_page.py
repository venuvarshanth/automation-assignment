from selenium.webdriver.common.by import By
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.logout_menu = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def go_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element(*self.logout_menu).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_button).click()
