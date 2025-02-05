import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
driver.maximize_window()


date_input = driver.find_element(By.XPATH, "//*[@id='datetimepicker1']")
date_input.click()


select_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/select")

options = Select(select_element)
options.select_by_visible_text("April") # This selects the desired month

# while True:
#     arrow_down = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/span[2]")
#     year = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/input")
#
#
#     if year.text == "1995":
#         break
#
#     else:
#         arrow_down.click()


date = driver.find_element(By.CLASS_NAME, "flatpickr-day")
date.click()
input_value = date_input.get_attribute("value")
print(input_value)

time.sleep(5)





