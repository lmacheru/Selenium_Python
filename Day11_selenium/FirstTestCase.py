# Before get started. we need to import webDriver module which is available in selenium package
# In the webDriver module we have all the classes and the methods we need to perform the tests

from selenium import webdriver

# In the webDriver module there is a chrome class within which there is a constructor available which takes
# browser driver as a parameter.
# driver is the object of the chrome class

# driver = webdriver.Chrome(executable_path="C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe") #WRONG

# The url taken by get method id the url of the tested site
# driver.get("https://opensource-demo.orangehrmlive.com/") # WRONG


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# # Specify the path to your ChromeDriver
# driver_path = "chromedriver.exe"
# service_obj = Service(driver_path)
#
# # Initialize the WebDriver
# driver = webdriver.Chrome(service=service_obj)
#
# # Example usage
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#
# # FINDING AN ELEMENT ON A PAGE
# # driver.find_element_by_name("txtUsername") #WRONG
#
# # Locate the username field using the By class
# driver.find_element(By.NAME,"username").send_keys("Admin")
#
# # Enter text into the username field
# # username_field.send_keys("Admin")
#
# # Locate the password field using the By class
# password_field = driver.find_element(By.NAME,"password")
#
# # Enter text into the password field
# password_field.send_keys("admin123")
#
# # select the button element
# login_btn = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
#
# # # click the button
# login_btn.click()
# #
# # # This will get the actual title of the page
# act_title = driver.title
# expected_title = "OrangeHRM"
#
#
# # # Wait for user input to close the browser
#
#
# #
# # input("Press Enter to close the browser...")
# if act_title == expected_title:
#     print("Login Test Passed")
#
# else:
#     print("Login Test Failed")
#
#
# # Close the driver
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to your ChromeDriver
# If you want to avoid having to having to copy and paste the file path as shown in the following line of code
# copy or move all the browser drivers to the script folder which is found in the python folder in C drive
# driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
# service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Firefox()

# try:
    # Open the login page
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait for the username field to be visible
wait = WebDriverWait(driver, 20)  # Increased timeout
# username_field = driver.find_element(By.NAME,"username") # WOULD NOT WORK
username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# Enter text into the username field
username_field.send_keys("Admin")

# Locate the password field and enter the password
password_field = driver.find_element(By.NAME, "password")  # Adjust locator if necessary
password_field.send_keys("admin123")

# Locate and click the login button
login_btn = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
login_btn.click()

# Verify the login was successful
# wait.until(EC.title_contains("OrangeHRM"))
act_title = driver.title
expected_title = "OrangeHRM"

if act_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
# except Exception as e:
#     print("An error occurred:", str(e))
# finally:
    # Close the browser
driver.quit()