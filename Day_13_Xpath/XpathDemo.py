# CHECK LESSON : SESSION 3 FOR MORE INFORMATION
# USING XPATH TO SELECT ELEMENTS
from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://ommifood.netlify.app/")
driver.maximize_window()

# driver.find_element(By.XPATH, "/html/body/header/div/nav/li[4]/a").click()

# Absulute Xpath
# driver.find_element(By.XPATH, "/html/body/header/div/nav/li[5]/a").click()
# driver.find_element(By.XPATH, "/html/body/section[7]/div/div/div[1]/form/div[1]/input").send_keys("Dennis")
# driver.find_element(By.XPATH, "/html/body/section[7]/div/div/div[1]/form/div[2]/input").send_keys("ldmamyala@gamil.com")

# Relative Xpath

# In this cases, you may use "or", "and" if you want to select an element using more than one attribute
# e.g @id='full-name' and @name='full-name', if both are correct for the element in question, then the element
# would get selected, otherwise the selection would fail

# In the case where "or" operator is used, then at least one of them should be correct
driver.find_element(By.XPATH, "/html/body/header/div/nav/li[5]/a").click()
# driver.find_element(By.XPATH, "//*[@id='full-name']").send_keys("Dennis")
# driver.find_element(By.XPATH, "//*[@id='email']").send_keys("ldmamyala@gamil.com")

# Using or/and operators

# or
driver.find_element(By.XPATH, "//*[@id='full-name' or @name='full-name']").send_keys("Dennis")
driver.find_element(By.XPATH, "//*[@id='email' or @name='email']").send_keys("ldmamyala@gamil.com")

# and
# driver.find_element(By.XPATH, "//*[@id='full-name'] and @name='full-name'").send_keys("Dennis")
# driver.find_element(By.XPATH, "//*[@id='email' and @name='email']").send_keys("ldmamyala@gamil.com")

# FUNCTIONS USED FOR DYNAMIC ELEMENTS
# Dynamic elements are the elements with classes/attributes that are constantly upon interacting with them
# For example, a text content may change from "Start" to "Stop" when clicked and id/class may as well change
# If the Xpath for "start" gets used while the id/class is "stop" then hai, it's chai, the element would not be found

#  So in these cases use contains() or startwith() functions to locate/select the element
# For example you can use the xpath in this way  //*[contains(@id,"st")]  ---> For contains() function
#                                                //*[starts-with(@id,"st")]  ---> For starts-with() function
#                                                //*[@id="start" or @id="stop"] using "or" operator


# There is also text function for text content of an element
# This is how it is used: //a[text()="women"]
# Another example: //*[text()="Sign up now"]






































