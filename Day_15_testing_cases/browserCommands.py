import time

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# The differences between close and quit
# 1)
# The close command will close the browser but the browsers specific process will keep on running behind the scenes
# When you use the quit command, then processes running in the background stop

# 2)
# Close command will close one browser at the time, but quit command closes everything. If 100 browsers are open
# then sll 100 of them will close



wait = WebDriverWait(driver, 20)  # Increased timeout
# username_field = driver.find_element(By.NAME,"username") # WOULD NOT WORK

# This statement will result in another browser window/tab open
link = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")))

link.click()

# This line only closes the previous browser window/tab not all of them
# driver.close()

# This line closes  all the current browser windows/tabs
time.sleep(5) # Wait for 5 seconds
driver.quit()
# input("What is the current element??")