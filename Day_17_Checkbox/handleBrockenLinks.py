
import time

import requests
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

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()


# WHAT IS A BROCKEN LINK??

# It is a link that does not point anywhere, meaning that it does not have a target
# We need to install requests package through File --Settings --> ProjectInterpreter --> search for "requests" package
# This helps us find the brocken links in the page

# links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Errorcode")
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

# Not really the right way
# brocken_links = []
# for link in links:
#     if link.text.startswith("Errorcode"):
#         brocken_links.append("link")
#
#
# print(len(brocken_links))



# The correct way
# whenever you are sending the request, there are network related exceptions that will be thrown
# So to avoid them, make sure that whenever you sent a request, put the statement (res = requests.head(url)) inside try/except block
count = 0
for link in links:

    # Now we sent the url to the server
    # We do that by using requests.head() which accept the url as an argument
    # Then the server will give you the response called "res"
    url = link.get_attribute("href")

    try:
        res = requests.head(url)

    except:
        None

    if res.status_code>=400:
        print(url, " is brocken link")
        count+=1

    else:
        print(url, " Is valid link")

print("Total number of the brocken links", count)

time.sleep(5)
