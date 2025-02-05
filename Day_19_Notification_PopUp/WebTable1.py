# WORKING WITH TABLES

# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on conditional (List books name whose author is Mukesh)


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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# WORKING WITH TABLES

# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on conditional (List books name whose author is Mukesh)

# 1) Count number of rows & columns
rows_number = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")  # rows
print(len(rows_number))
columns_number = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")  # columns
print(len(columns_number))

# 2) Read specific row & Column data
#                                                                                        rows   column
data_element = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[5]/td[1]")
print(data_element.text)

# 3) Read all the rows & Columns data

print("printing all the rows and columns data............................")


# for r in range(2, len(rows_number) + 1):
#     for c in range(1, len(columns_number) + 1):
#         data_element = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data_element)
#
#         # To make sure that the printed data is side by side
#         print(data_element, end='             ')

#
#
#     # To have a space in between the printed data
#     print()


# 4) Read data based on conditional (List books name whose author is Mukesh)


    # print()
time.sleep(5)















