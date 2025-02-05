import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This is what we firstly have to do to handle these kinds of notification
# ChromeOptions class found in webdriver, which returns an object of options, is used to specify browser level settings. We can use it to disable popups
# This instance should then be passed inside the Chrome class an as argument
ops = webdriver.ChromeOptions()

# Settings
ops.add_argument("--disable-notifications")

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=ops) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.



driver.get("https://whatmylocation.com/")
driver.maximize_window()

# The notification popups are not popups like those that appear after a click of a button, nor those which appear the moment
# after the page has loaded in the browser with inputs elements in which a value can be typed by injecting it in the url
# This notification popups load immediately after the browser has loaded and cannot simply be removed with with the injection
# of an input into the URL


time.sleep(10)