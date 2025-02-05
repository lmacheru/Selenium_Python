import time

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# To pick the option in the bootstrap dropdown, we cannot use the "Select" class like we did for the normal dropdowns
select_input = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
select_input.click()

options = driver.find_elements(By.CLASS_NAME, "select2-results__option")

for option in options:
    if option.text == "South Africa":
        option.click()
        break



time.sleep(5)