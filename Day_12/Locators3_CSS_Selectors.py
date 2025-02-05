from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://web.facebook.com/")
driver.maximize_window()

# CSS Selectors (Here we basically use the combination like we usually when styling elements in css
# tag & id

# The "#" is for id selection
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")


# Tag and Class combination
# username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# wait = WebDriverWait(driver, 20)  # Increased timeout
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".inputtext"))).send_keys("abc")

# Tag and name attribute combination

driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_pass").send_keys("Dennis")


