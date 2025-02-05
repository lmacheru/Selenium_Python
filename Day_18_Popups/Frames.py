# When dealing with frames in web pages, the elements inside the frame can't be selected as we've been selecting them
# If you want to interact with an element that is inside a frame/iframe, you need to switch to the particular frame that contains the element


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

driver.get("https://selectorshub.com/iframe-scenario/")
driver.maximize_window()

# When dealing with frames in web pages, the elements inside the frame can't be selected as we've been selecting them
# If you want to interact with an element that is inside a frame/iframe, you need to switch to the particular frame that contains the element
# This are the options you have to switch from one frame to another:

# 1) switch_to.frame(name of the frame)
# 2) switch_to.frame(name of the frame)
# 3) switch_to.frame(webelement)
# 3) switch_to.frame(0) , id you have only one frame

# In this case, we have "pact1" as the parent of "pact2" and grandparent of "pact3"
# If this frames were siblings, meaning that they were not nested, then we would have to get out of each frame
# after any action has been perfomed on it. We get out by using:
# driver.switch_to.default_content()

# Frame 1
driver.switch_to.frame("pact1")

frame_input1 = driver.find_element(By.XPATH, "//*[@id='inp_val']")
frame_input1.send_keys("Dennis")

frame_btn1 = driver.find_element(By.XPATH, "//*[@id='lost']")
frame_btn1.click()


# Frame 2
driver.switch_to.frame("pact2")

frame_input2 = driver.find_element(By.ID, "jex")
frame_input2.send_keys("Homba")

frame_btn2 = driver.find_element(By.XPATH, "//*[@id='connect']")
frame_btn2.click()

# Frame 3

driver.switch_to.frame("pact3")

frame_input3 = driver.find_element(By.XPATH, "//*[@id='glaf']")
frame_input3.send_keys("Groove")

frame_btn3 = driver.find_element(By.XPATH, "//*[@id='close']")
frame_btn3.click()

# Switching to the parent frame
driver.switch_to.parent_frame()
frame_input2 = driver.find_element(By.ID, "jex")
frame_input2.clear()
frame_input2.send_keys("Mazaleni")

# Switching to the default page
driver.switch_to.default_content()
courses_btn = driver.find_element("//*[@id='menu-item-1075']/a")
courses_btn.click()


time.sleep(5)

