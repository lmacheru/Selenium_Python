from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #maximize the browser window

driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# SELECTION OF LINK ELEMENTS
# Links are always selected using the link text, as in textContent in javascript
# By.LINK_TEXT is used when the whole link text is used as a selector
# By.PARTIAL_LINK_TEXT is for when the small portion of the link text is used for selection

# Linktext and Partial linktext
# driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


# We most of the time use "id" for selection because id are unique
# But if we want to locate more than one element, we use class or tag because a class/tag can be used more than once
# as opposed to "id". So basically, there are certain elements which have the same class names or tags

# FINDING MORE THAN ONE ELEMENT USING CLASS NAME AND TAG NAME
# So we use find_elements not find_element, then list will be returned containing all the selected elements


