import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

wait=WebDriverWait(driver,10)
emailbox=wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='Email']")))
emailbox.clear()
emailbox.send_keys("molaodi@gmail.com")

print("results of text:", emailbox.text) # Returns nothing
print("results of get attribute:", emailbox.get_attribute('value')) # Returns the value of the input (It is like textContent and value in javascript)
# print("results of get attribute:", emailbox.get_attribute('id')) # Returns the value of the id (It is like textContent and value in javascript)
# print("results of get attribute:", emailbox.get_attribute('name')) # Returns the value of the name (It is like textContent and value in javascript)

# print("results of text:", emailbox.text) #This does not work
time.sleep(10)
# input("test")