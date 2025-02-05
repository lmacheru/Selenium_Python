import time

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://www.snadeal.com") # First browser window
driver.get("https://www.amazon.com")  # Second browser window
driver.maximize_window()

# Moving back to snadeal page
driver.back()

# Moving forward, back to the amazon page
driver.forward()

# Refreshing the page
driver.refresh()




# time.sleep(15)
input("Test?")