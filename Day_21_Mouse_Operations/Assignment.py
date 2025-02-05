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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_down = driver.find_element(By.XPATH, "//*[@id='HTML3']/div[1]/div/button")
mobiles_btn = driver.find_element(By.XPATH, "//*[@id='HTML3']/div[1]/div/div/a[1]")
labtops_btn = driver.find_element(By.XPATH, "//*[@id='HTML3']/div[1]/div/div/a[2]")



act = ActionChains(driver)

# Mouse hover
act.move_to_element(drop_down).move_to_element(mobiles_btn).move_to_element(labtops_btn).click().perform()

# Double click
input1 = driver.find_element(By.XPATH, "//*[@id='field1']")
input1.clear()
input1.send_keys("You are wellcome")

copy_btn = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")

act.double_click(copy_btn).perform()

# Drag and drop
source_box = driver.find_element(By.ID, "draggable")
target_box = driver.find_element(By.ID, "droppable")

act.drag_and_drop(source_box, target_box)

# Drag and Drop
min_btn = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_btn = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

act.drag_and_drop_by_offset(min_btn, -40, 0).perform()
act.drag_and_drop_by_offset(max_btn, 140, 0).perform()

time.sleep(5)