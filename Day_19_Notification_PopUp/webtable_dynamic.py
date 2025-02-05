import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# Enter text into the username field
username_field.send_keys("Admin")

# Locate the password field and enter the password
password_field = driver.find_element(By.NAME, "password")  # Adjust locator if necessary
password_field.send_keys("admin123")

# Locate and click the login button
login_btn = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
login_btn.click()

# Click admin button
admin_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))
admin_btn.click()


# Changing enabled to disabled
# state_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[2]")))
# state_button.click()
#
# change_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i")))
# change_btn.click()

# Find out how many users are disabled and how many are enabled

# table_rows = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='oxd-table-card']")))
# print(len(table_rows))

table_rows = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "oxd-table-row")))
print(len(table_rows))

disabled = 0
enabled = 0

for row_index in range(1, len(table_rows)):
    user_state = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div["+str(row_index)+"]/div/div[5]/div")))
    # print(user_state.text)

    if user_state.text == "Enabled":
        enabled = enabled + 1

    else:
        disabled = disabled + 1

print("Enabled: ", enabled)
print("Disabled: ", disabled)

time.sleep(10)