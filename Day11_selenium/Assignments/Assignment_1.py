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
driver = webdriver.Chrome()

# try:
    # Open the login page
driver.get("https://admin-demo.nopcommerce.com/login")

# Wait for the username field to be visible
wait = WebDriverWait(driver, 20)  # Increased timeout
# username_field = driver.find_element(By.NAME,"username") # WOULD NOT WORK
username_field = wait.until(EC.visibility_of_element_located((By.NAME, "Email")))
# username_field.clear()
# Enter text into the username field
username_field.send_keys("admin@yourstore.com")

# Locate the password field and enter the password
password_field = driver.find_element(By.NAME, "Password")  # Adjust locator if necessary
# password_field.clear()
password_field.send_keys("admin")

# Locate and click the login button
login_btn = driver.find_element(By.CLASS_NAME, "login-button")
login_btn.click()

# Verify the login was successful
wait.until(EC.title_contains("Your store. Login"))
act_title = driver.title
expected_title = "Your store. Login"

if act_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
# except Exception as e:
#     print("An error occurred:", str(e))
# finally:
    # Close the browser
driver.quit()