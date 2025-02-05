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

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switching to the frame
frame = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
driver.switch_to.frame(frame)

# Since we have only one frame, we can also use: driver.switch_to.frame(0), using 0 instead of an element
# Input date
date_input = driver.find_element(By.XPATH, "//*[@id='datepicker']")
# date_input.send_keys("05/30/2022")
date_input.click()





# My solution
# while True:
#
#     month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
#     year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
#     go_back_btn = driver.find_element(By.CLASS_NAME, "ui-datepicker-prev")
#     go_forward_btn = driver.find_element(By.CLASS_NAME, "ui-datepicker-next")
#     date = driver.find_elements(By.CLASS_NAME, "ui-state-default")

    # month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    #
    # if month.text == "December" and year.text == "2026":
    #     for day in date:
    #         if day.text == "21":
    #             day.click()
    #     break
    #
    # else:
    #     go_forward_btn.click()
        # go_back_btn.click()


        # if int(year.text) > 2022:
        #     go_back_btn.click()
        # if int(year.text) < 2022:
        #     go_forward_btn.click()




# INSTRUCTOR'S SOLUTION

mon = "December"
yr = "2026"
date = "21"

while True:

    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year")
    go_back_btn = driver.find_element(By.CLASS_NAME, "ui-datepicker-prev")
    go_forward_btn = driver.find_element(By.CLASS_NAME, "ui-datepicker-next")

    # month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month")

    if month.text == mon and year.text == yr:
        break

    else:
        go_forward_btn.click()
        # go_back_btn.click()


dates = driver.find_elements(By.CLASS_NAME, "ui-state-default")

# He separated the dates from the month and year code, as opposed to what I did above, but both code work perfectly fine
for day in dates:
    if day.text == date:
        day.click()
        break