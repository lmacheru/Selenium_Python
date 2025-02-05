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

driver.get("https://demo.nopcommerce.com/#")
driver.maximize_window()

# WORKING WITH LINKS

# selected_element1 = driver.find_element(By.LINK_TEXT, "Digital downloads")
# selected_element2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Digital")
# selected_element = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/ul[1]/li[4]/a")
# selected_element.click()


# Selection of multiple links
# links = driver.find_elements(By.XPATH, "//a")
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
for link in links:
    print(link.text)


time.sleep(5)


