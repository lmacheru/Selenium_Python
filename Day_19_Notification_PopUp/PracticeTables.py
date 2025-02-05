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

row_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[2]")
column_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/td[1]")


# for row in range(2, len(row_elements) + 1):
#     for column in range(1, len(column_elements)+ 1):
#         element = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td["+str(column)+"]").text
#         print(element)




# 4) Read data based on conditional (List books name whose author is Mukesh)
authors_column = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/td[2]")
books_column = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/td[1]")

for position in range(1, len(authors_column)+1):
    # authors_column = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/td[2]")

    if authors_column[position - 1].text == "Mukesh":
        book = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(position + 1) + "]/td[1]")


        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(position + 1)+"]/td[4]")
        print("Book Title", book.text)
        print("Book Price", price.text)


    else:
        continue









# for author in authors_column:
#     print(author.text)



time.sleep(5)