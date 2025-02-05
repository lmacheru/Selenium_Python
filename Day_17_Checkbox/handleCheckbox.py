import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

# 1) Select specific checkbox
# checkbox = driver.find_element(By.XPATH, "//*[@id='check1']")
# checkbox.click()

# 2) Multiple checkbox selection and 3)
checkboxes = driver.find_elements(By.NAME, "identity_type")

# for checkbox in checkboxes:
#     if checkbox.get_attribute("id") == "passport":
#         continue
#     else:
#         checkbox.click()

# 3) Selecting the last two checkboxes
# checkboxes[len(checkboxes) - 1].click()
# checkboxes[len(checkboxes)-2].click()
# checkboxes[-1].click()
# checkboxes[-2].click()

# Another way of selecting the last two boxes
# for i in range(len(checkboxes)-2, len(checkboxes)):
#     checkboxes[i].click()
#     print(i)

# 4) Selecting only the first 2 elements

for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

# 5) Unchecking the checkbox
for i in range(len(checkboxes)):
    # Checking if there is any box selected
    if checkboxes[i].is_selected():
        checkboxes[i].click()

time.sleep(10)
