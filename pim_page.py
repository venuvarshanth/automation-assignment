from selenium.webdriver.common.by import By
import time

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.XPATH, "//button[text()=' Add ']")
        self.first_name_input = (By.NAME, "firstName")
        self.middle_name_input = (By.NAME, "middleName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_button = (By.LINK_TEXT, "Employee List")

    def add_employee(self, first_name, middle_name, last_name):
        self.driver.find_element(*self.add_button).click()
        time.sleep(1)
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.middle_name_input).send_keys(middle_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()
        time.sleep(2)

    def verify_employee_list(self, first_name):
        self.driver.find_element(*self.employee_list_button).click()
        time.sleep(2)
        page_source = self.driver.page_source
        if first_name in page_source:
            print("✅ Name Verified")
        else:
            print("❌ Name Not Found")
