from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://ommifood.netlify.app/")
driver.maximize_window() #maximize the browser window



sliders =  driver.find_elements(By.CLASS_NAME, "feature")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links)) #Total number of links