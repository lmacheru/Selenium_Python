import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

# # Performing right click action on a button
# frame = driver.find_element(By.XPATH, "//*[@id='iframeResult']")
# driver.switch_to.frame(frame)
#
# field_1 = driver.find_element(By.XPATH, "//*[@id='field1']")
# field_1.clear()
# field_1.send_keys("Welcome")
#
# # field_2 = driver.find_element(By.XPATH, "//*[@id='field2']")
#
# copy_btn = driver.find_element(By.XPATH, "/html/body/button")
#
# act = ActionChains(driver)
# act.double_click(copy_btn).perform()


# WORKED FINE

btn = driver.find_element(By.XPATH, "//*[@id='authentication']/button")

act = ActionChains(driver)
act.double_click(btn).perform()

alert = driver.switch_to.alert
alert.accept()
time.sleep(5)