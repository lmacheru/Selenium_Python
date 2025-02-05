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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

# Determination of the location of the button elements located on both ends of the slider

min_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of sliders before moving........")
# These are default locations
print("Min slider", min_slider.location) # {'x': 59, 'y': 289}
print("Max slider", max_slider.location) # {'x': 638, 'y': 289}


# Here we are changing the axis

act = ActionChains(driver)

# Here we pass three arguments: target element, x-axis, y-axis
# The passing in of 100 will be added to 59 which will then results in the element moving 100 units to the right
# We do not know y-axis, hence we pass in 0 as a third argument
act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -39, 0).perform()



print("Location of sliders after moving........")
# These are locations of the sliders after moving
print("Min slider", min_slider.location) # {'x': 59, 'y': 289}
print("Max slider", max_slider.location) # {'x': 638, 'y': 289}
time.sleep(5)


# If teh slider is in a vertical direction, we focus on y-axis

