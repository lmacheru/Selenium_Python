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


# Popup selection
alert_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='alertBtn']")))
alert_btn.click()

# Switching to the popup window
switch = driver.switch_to.alert
switch.accept()


# Input selection

intro_input = driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']")
intro_input.send_keys("selenium")

# Click search button
search_btn = driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input")
search_btn.click()

# Multiple elements selection
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    if link.get_attribute("target") == "_blank":
        link.click()


browser_IDs = driver.window_handles
for window in browser_IDs:
    driver.switch_to.window(window)
    print(driver.title)



time.sleep(7)
driver.quit()

