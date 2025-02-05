from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


# 2) CONDITIONAL COMMANDS
# -----------------------------------

# is_displayed --> to check if the element is available or present on the web page or not
searchbox = driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("Is displayed :", searchbox.is_displayed())

# is_enabled --> This is to check if the element can be interacted with. For example, a disabled button can't be clicked
print("Is enabled :", searchbox.is_enabled())

# is_selected --> Check if the element is selected or not. If checked, true gets returned and false if the element id not selected

# For male
maleBtn = driver.find_element(By.XPATH, "//*[@id='gender-male']")
maleBtn.click()
print("Is selected", maleBtn.is_selected())

# For female
femaleBtn = driver.find_element(By.XPATH, "//*[@id='gender-female']")
femaleBtn.click()
print("Is selected", femaleBtn.is_selected())


driver.quit()