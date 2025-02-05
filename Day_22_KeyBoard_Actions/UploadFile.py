import time

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://practice.expandtesting.com/upload")
driver.maximize_window()

upload_input = driver.find_element(By.XPATH, "//*[@id='fileInput']")

# In the send_key method, we specify the location of the file we want to upload
upload_input.send_keys("C:/Users/DENNIS/Downloads/myfile.pdf")

time.sleep(5)
