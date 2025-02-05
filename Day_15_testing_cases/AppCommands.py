from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# 1) APPLICATION COMMANDS
# ----------------------------------

# Getting the title of the page
print(driver.title) #OrangeHRM

# Capturing the URL of the application
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

# Getting the source of the page, so basically the code written by the server
# We use this verify if something is present on the page source or not
print(driver.page_source)

# 2) CONDITIONAL COMMANDS
# -----------------------------------

# is_displayed --> to check if the element is available or present on the web page or not

# is_enabled --> This is to check if the element can be interacted with. For example, a disabled button can't be clicked

# is_selected --> Check if the element is selected or not. If checked, true gets returned and false if the element id not selected
