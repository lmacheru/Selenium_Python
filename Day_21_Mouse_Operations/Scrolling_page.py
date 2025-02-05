import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://flagpedia.net/index")
driver.maximize_window()

# time.sleep()

# 1) Scroll down page by pixel

# We are passing in javascript statements
# driver.execute_script("window.scrollBy(0, 3000)", "")
# value = driver.execute_script("return window.pageYOffset;")   # This will return the exact position of the scroll
#
# print("Number of pixes moved:", value)


# 2) Scroll down page till the element is visible/FOUND

# SA_flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/ul[2]/li[210]/a/img")
#
# # Here we will scroll the page, until the SA_flag element is found
# driver.execute_script("arguments[0].scrollIntoView();", SA_flag)
#
# # To find out by how pixels it has moved
# value = driver.execute_script("return window.pageYOffset;")   # This will return the exact position of the scroll
#
# print("Number of pixes moved:", value)



# Scroll down page till end
# execute_script is the  method that allows us to execute the javascript method
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

value = driver.execute_script("return window.pageYOffset;")   # This will return the exact position of the scroll

print("Number of pixes moved:", value)



# Moving back to the original position
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")



time.sleep(5)