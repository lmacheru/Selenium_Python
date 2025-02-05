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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()


# Alert window is not a web element, meaning that we cannot locate the elements that are in browser popup
# Opening the alert window
# btn3 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
# btn3.click()

btn1 = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
btn1.click()


# Since we cannot use select the alert window elements to perform actions on them, we use the following to
# switch to the alert window.
# The  alert window can be saved in a variable as an object
alertWindow = driver.switch_to.alert

# Capturing the text that is present inside the alert window
print(alertWindow.text)

# Passing a value into the alert window input box
# alertWindow.send_keys("welcome")

# Closing the alert window using the closing button
# alertWindow.accept()

# Closing the alert window using cancel button
alertWindow.accept()

time.sleep(5)





