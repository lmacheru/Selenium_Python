import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://textcompareonline.com/")
driver.maximize_window()

# Selection of the boxes within which the text is going to be compared
text_box1 = driver.find_element(By.XPATH, "//*[@id='originalText']")
text_box2 = driver.find_element(By.XPATH, "//*[@id='changedText']")

text_box1.send_keys("Welcome to selenium")

act = ActionChains(driver)

# 1)  Ctrl + A to Select the text

# # MULTIPLE STATEMENTS

# # This two lines of code will press Ctrl A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")

# # Releasing the keys after pressing them
# act.key_up(Keys.CONTROL)
# act.perform()


# SINGLE STATEMENT
# You can also write the above lines of code in this way:
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()


# 2) Ctrl + C to Copy the content
# # MULTIPLE STATEMENTS

# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()


# SINGLE STATEMENT
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# 3) Moving to the next box using TAB key
# MULTIPLE STATEMENTS
# act.key_down(Keys.TAB)
# act.key_up(Keys.TAB)
# act.perform()

# SINGLE STATEMENT
# act.key_down(Keys.TAB).key_up(Keys.TAB).perform() #key_up include but excluded in the code below
act.key_down(Keys.TAB).perform()

# 4) Pasting content in the text_box 2

# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


time.sleep(15)

































