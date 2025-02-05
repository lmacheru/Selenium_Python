import time
import os

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture a screenshot whenever test-case fail on a particular page
# Inside the save_screenshot method, we pass the path for the location in which the screenshot is going to be saved
# driver.save_screenshot(os.getcwd()+"\homepage.png") # 1)

# This performs the same thing as the line above
# driver.get_screenshot_as_file(os.getcwd()+"\homepage.png") # 2)

# These are rarely used
# driver.get_screenshot_as_png() # 3)
# driver.get_screenshot_as_base64() # 4)



time.sleep(5)