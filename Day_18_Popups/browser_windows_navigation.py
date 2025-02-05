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

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()





# Here we switch from one browser window to another and how exactly is that done ??
# We use: switch_to.window(WindowID)
# driver.current_window_handle  ---> return the window ID of a browser

# A new window is always created upon launch of the browser
# window_id = driver.current_window_handle
# print(window_id) #A5B129C8A5CBDE4546BC199E96A5886B

btn1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")))
btn1.click()

# Switching to another window
# This returns two ids as a list

# window_id = driver.current_window_handle # for when we expect only one window id (parent window)
# print(window_id)

# For multiple windows
window_id = driver.window_handles # for when we expect only two window ids (parent window and child window)
# parentWindowID = window_id[0]
# childWindowID = window_id[1]
#
# print(parentWindowID, childWindowID)
#
# # Switching to the child window
# driver.switch_to.window(childWindowID)
#
# print("PARENT WINDOW TITLE: ", driver.title)
#
# nav_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[2]/a")))
# nav_btn.click()
#
# # Switched back to the parent
# driver.switch_to.window(parentWindowID)
# print("CHILD WINDOW TITLE: ", driver.title)

# LOOPING THROUGH A LIST OF WINDOW IDs

# for window in window_id:
#     driver.switch_to.window(window)
#     print(driver.title)

# CLOSING THE BROWSER WINDOW
for window in window_id:
    driver.switch_to.window(window)
    print(driver.title)

    # if driver.title == "OrangeHRM":
    # you can also add more browser windows by using or/and in your if statement
    if driver.title == "Human Resources Management Software | OrangeHRM":
        driver.close()

time.sleep(5)