# We need to use wait commands because most of the time, the script execution is faster than your application response
# So such cases, the script does not wait for the targeted element to be present after the page has completely reloaded
# This then results in the script failing. time.sleep(time) can be used to wait but we cannot really rely on it

# TWO TYPES OF WAIT COMMANDS

# 1) Implicit wait

# Advantages
#       a) You need only one statement
#       b) If the element is available within the specified seconds, then the following lines of code get executed

# Disadvantages
#       a)If the element is not available within the specified time, the exception gets returned
#
# 2) Explicit wait
# Explicit wait works based on a condition


import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

# Always place this statement at the top like it is now, so that the wait is applied to all the statements that will need below
# You just need this statement and nothing else
driver.implicitly_wait(10) #Explicit wait.

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH, "//*[@id='APjFqb']")
searchbox.send_keys("Selenium")
searchbox.submit()

hyperlink = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3")
hyperlink.click()

time.sleep(15)

