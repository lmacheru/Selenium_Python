import time
from selenium.webdriver.support.select import Select



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Day_24_Excel import XLUtility
from Day_24_Excel.XLUtility import writeData

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher
wait=WebDriverWait(driver,10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()


file = "C:/Users/DENNIS/Desktop/Automation_Excel_Files/Book3.xlsx"

rows = XLUtility.getRowCount(file, "Sheet1")

for row in range(2, rows + 1):
    principle = XLUtility.readData(file, "Sheet1", row, 1)
    interest_rate = XLUtility.readData(file, "Sheet1", row, 2)
    period1 = XLUtility.readData(file, "Sheet1", row, 3)
    period2 = XLUtility.readData(file, "Sheet1", row, 4)
    frequency = XLUtility.readData(file, "Sheet1", row, 5)
    expected_maturity = XLUtility.readData(file, "Sheet1", row, 6)

    #Passing data to the application
    if row > 6:
        break

    driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(interest_rate)
    driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(period1)
    period_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='tenurePeriod']"))
    period_dropdown.select_by_visible_text(period2)

    frequency_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)

    if row == 2:
        driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    time.sleep(5)


    # calculate_btn.click()
    act_maturity = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text

    if float(expected_maturity) == float(act_maturity):
        print("test passed")
        XLUtility.writeData(file,"Sheet1", row, 8, "Passed")
        XLUtility.fillGreenColor(file,"Sheet1", row, 8)

    else:
        print("test failed")
        XLUtility.writeData(file,"Sheet1", row, 8, "Failed")
        XLUtility.fillRedColor(file,"Sheet1", row, 8)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()

driver.close()







