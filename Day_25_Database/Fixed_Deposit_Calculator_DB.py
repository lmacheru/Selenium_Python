import time
import mysql.connector
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)  # Browser launcher
wait = WebDriverWait(driver, 10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="%LDMonyaku5995$", database="myDB")
    select_query = "select * from deposit"

    # create cursor, and through this cursor, an SQL statement will get executed
    cursors = connection.cursor()

    # Execute query through cursor
    # This statement will return the data for us, so we have to store the data in a variable
    cursors.execute(select_query)

    for row in cursors:
        principle = row[0]
        interest_rate = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expected_maturity = row[5]
        # This
        print(row)  # (1, 'Dennis', 'Mamyala', Decimal('150.50'), datetime.date(2024, 12, 26))
        print(row[0], row[1], row[2])  # 1 Dennis

        # Passing data to the application
        # if row > 6:
        #     break

        driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(principle)
        driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(interest_rate)
        driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(period1)
        period_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='tenurePeriod']"))
        period_dropdown.select_by_visible_text(period2)

        frequency_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
        frequency_dropdown.select_by_visible_text(frequency)

        if row[0] == 20000:
            driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

        time.sleep(5)

        # calculate_btn.click()
        act_maturity = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text

        if float(expected_maturity) == float(act_maturity):
            print("test passed")


        else:
            print("test failed")

        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
    connection.close()
except:
    print("Connection unsuccessful...")

driver.close()

