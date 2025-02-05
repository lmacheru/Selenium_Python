# 2) Explicit wait
# Explicit wait works based on a condition not on the time


import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

# Why do we need time if this statement or explicit wait depends on the conditon??
#
# wait=WebDriverWait(driver,10) #Explicit wait.

# As opposed to the statement above, this statement results in the exceptions being ignored which then
# make it possible for the following line of code to be executed even if the element is not found
# If you need not write all these exceptions, then just write "Exception" only in the square bracket and all the exceptions will still be ignored
# You may also include as an argument: poll_frequency = 2, this will result in an element being checked after every two munites if the element is available or not
wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://www.google.com/")
driver.maximize_window()

# If the element is not available on the page what will happen??
# The conditon will never be true, which means that the executiion will stop here
searchbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='APjFqb']")))
searchbox.send_keys("Selenium")
searchbox.submit()

hyperlink = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3")))
hyperlink.click()

time.sleep(15)