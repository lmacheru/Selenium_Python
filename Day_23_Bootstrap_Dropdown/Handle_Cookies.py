import time
import os
from msilib import Control

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# By default, there are cookies created by the application. So we want to know how many cookies are created
# This line captures cookies from the browser
# Cookie is not a web element and every cookie have name and values attribute and expiry date
# And this cookie data is stored in the dictionary object
# cookies = driver.get_cookies()
# print(len(cookies))

# Printing the information about all the cookies
# for cookie in cookies:
#     # print(cookie)
#     # To print a specific value, this line of code would work perfectly fine
#     # print(cookie["httpOnly"])
#     # Instructor's property value print technique
#     print(cookie.get("name"), ":", cookie.get("value"))

# ADDITION OF OUR OWN COOKIE TO THE BROWSER
# If after adding a cookie, the length of the cookies does not change, then that means the application does not  allow you to add cookies


# The cookies should be specified in a dictionary format
driver.add_cookie({"name":"MyCookie", "value":"123456"})

cookies = driver.get_cookies()
print(len(cookies))

# for cookie in cookies:
#     print(cookie)

# DELETING A COOKIE FROM THE BROWSER

# If after deleting the cookies, the number of the cookies remains the same, then in that case the browser does not allow you to delete cookies
# How to delete a specific cookie from the browser
# Inside the delete_cookie method, we pass the name of the cookie
driver.delete_cookie("MyCookie")

cookies = driver.get_cookies()
print(len(cookies))

# DELETING ALL THE COOKIES

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))


# COOKIES TESTS ARE NOT ALWAYS REQUIRED
time.sleep(5)















# Here we check if the web application is creating cookies or not, and what type of cookies it is creating
# And we can also extract the values of the cookies