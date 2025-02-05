import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


####  Find_element() ---> Returns single web element

# The scenarios for find_element()

# (1) Locator matching with single web element
# (2) Locator matching with multiple web elements --> Only the first element get returned
# (3) Locator not matching any web element on the page --> Returns no such element exception. Unable to locate the element


##  Find_elements() ---> Returns multiple web elements

# The scenarios for find_elements()

# (1) Locator matching with single web element --> like "id" as it can only be used once

# We know that if the locator is matching multiple elements it will return multiple elements
# If the locator is matching with single element, then even that element will be returned but not as a web element
# but a list item, because find method always returns a list/array collection
elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
elements[0].send_keys("Dennis")

time.sleep(10)


# (2) Locator matching with multiple web elements --> All the elements get captured
# To access the specific element, use the index number like we do in javascript

# (3) Locator not matching any web element on the page --> Returns nothing, not even an exception error unlike find_element
