import time
import os
from msilib import Control
from pickletools import read_uint1

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.common.by import By



def headless_chrome():
    from selenium.webdriver.chrome.service import Service

    driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
    service = Service(driver_path)

    # Headless mode line
    ops = webdriver.ChromeOptions()
    # ops.headless = True # This does not work for headless
    ops.add_argument("--headless") # But this works
    driver = webdriver.Chrome(service=service, options=ops)  # Browser launcher
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service

    driver_path =  "C:\Automation_Testing_Drivers\edgedriver_win64\msedgedriver.exe"
    service = Service(driver_path)

    # Headless mode line
    ops = webdriver.EdgeOptions()
    # ops.headless = True # This does not work for headless
    ops.add_argument("--headless") # But this works
    driver = webdriver.Edge(service=service, options=ops)  # Browser launcher
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service

    driver_path =  "C:\Automation_Testing_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe"
    service = Service(driver_path)

    # Headless mode line
    ops = webdriver.FirefoxOptions()
    # ops.headless = True # This does not work for headless
    ops.add_argument("--headless") # But this works
    driver = webdriver.Firefox(service=service, options=ops)  # Browser launcher
    return driver
# driver = headless_chrome()
# driver = headless_edge()
driver = headless_firefox()
driver.get("https://demo.nopcommerce.com/")




# Headless mode means that even without a UI, we can still execute our test case.
# That means you do not see the browser or the application during the execution of the script, but the execution will be successful
# Normally when we are executing a test case, we are able to see the browser and every action our automation script is doing

# -----Advantages of Headless mode-----
# 1) High performance
# 2) Multiple tasks can be performed

# -----Disadvantages-------
# 1) You would not know the functionality of the application. You would not know if it navigates to each and every page or not

print(driver.title)
print(driver.current_url)

time.sleep(3)
driver.close()
