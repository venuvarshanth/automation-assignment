import sys
import os
import time
from selenium import webdriver

# Add root folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage

def test_main_flow():
    print("Starting OrangeHRM test...")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    dashboard.go_to_pim()

    pim = PIMPage(driver)
    pim.add_employee("venu", "varshanth", "kolamudi")
    pim.verify_employee_list("venu")

    dashboard.logout()
    time.sleep(2)

    driver.quit()
    print("Test Completed")

if __name__ == "__main__":
    test_main_flow()
