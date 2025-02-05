import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains

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

# user_management_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")))

# users_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li")))

pmi_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")))

Leave_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a")))



# Mouse Hover
# We firstly have to create an object of the class "ActionChains" to perform mouse hover operations
# We use mouse hover actions whenever clicks are not allowed in some of the elements in the page
act = ActionChains(driver)

act.move_to_element(admin_btn).move_to_element(pmi_btn).move_to_element(Leave_btn).click().perform()


time.sleep(5)

