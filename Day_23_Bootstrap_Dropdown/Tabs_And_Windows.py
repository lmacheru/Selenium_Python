import time
import os
from msilib import Control

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

register = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a")

# This does not open the link on the next tab, but on the same tab
# register.click()

# Keys.RETURN is the same as ENTER
# This will open the register link in another tab
# registration_link = Keys.CONTROL+Keys.RETURN
# register.send_keys(registration_link)

# ##### New Tab --> Selenium 4 : Opens a new tab and switches to new tab  #######
# So with this, as soon as another tab is opened, the focus will then be on it
driver.get("https://www.opencart.com/")

# This new_window method will open another tab, amd inside that tab window this new application below will be opened
# This opens a new tab
driver.switch_to.new_window('tab')
# This opens a new window
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")


time.sleep(5)
