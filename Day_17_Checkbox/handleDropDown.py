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

driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

# WORKING WITH DROPDOWNS
country_ele = driver.find_element(By.ID, "country")

# Inside selenium driver, there is a pre-defined "Select' and inside this select class, we pass the "select" element
# The instance of this Select class is an object that contains the options for the "select" element
dropdown_country = Select(country_ele)

# Select option from the dropdown

# 1)
# dropdown_country.select_by_visible_text("India")

# 2)
# This is another method of selecting an option
# value is actually the attribute of the option in the select element
# dropdown_country.select_by_value("Brazil")

# 3)
# Option selection using an index number
# dropdown_country.select_by_index(13)


# Capturing all the options available

# options = driver.find_elements(By.TAG_NAME, "option")
# print(len(options))
# for option in options:
#     print(option.text)

#  Capturing options for a specific "select" element
# This options property returns all the options
alloptions  = dropdown_country.options
# print("Tota; number of options for this select element is: ", len(alloptions))
#
# for option in alloptions:
#     print(option.text)

# Selecting an option without using build in methods
# for option in alloptions:
#     if option.text == "South Africa":
#         option.click()
#         break #We break because we need not to check other elements



# If you do want to use Select class we've above then you may select the multiple option elements as we did with other element
# Then click a specific option using for loop as we did above

options = driver.find_elements(By.TAG_NAME, "option")
print(len(options))
for option in options:
    if option.text == "South Africa":
        option.click()
        break

time.sleep(5)





