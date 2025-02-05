import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This command will get us current working directory
location = os.getcwd()





# Setting up chrome browser
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"

    # Settings ---> This settings will be applicable to the browser at the run time
    # For PDF files, if the file gets downloaded on click, use this line
    # preferences = {"download.default_directory":location}
    #This line is for the PDF files that are not downloaded from the get go on click, but get opened instead
    # So the file will get downloaded, not opened
    preferences = {"download.default_directory":location, "plugins.always_open_pdf_externally":True}

    # Calling chromeOptions class available in the webdriver
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=ops)  # Browser launcher
    return driver


# Setting up Edge browser
def edge_setup():
    from selenium.webdriver.edge.service import Service
    driver_path = "C:\Automation_Testing_Drivers\edgedriver_win64\msedgedriver.exe"

    # Settings ---> This settings will be applicable to the browser at the run time
    # preferences = {"download.default_directory":location}
    # Check the explanation for this line in chrome preference settings above
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}

    # Calling edgeOptions class available in the webdriver
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=ops)  # Browser launcher
    return driver


# Setting up Firefox browser
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    driver_path = "C:\Automation_Testing_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe"
    service = Service(driver_path)

    # Settings ---> This settings will be applicable to the browser at the run time
    # These settings are for a popup that appears when a file is downloaded in using firefox.
    # But this seems to have only happened in the previous versions of firefox(I do not get the popups for the current version)
    ops = webdriver.FirefoxOptions()

    #                                                                                    specify the file type
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "myfile.pdf")
    # This will result in the popup not apperaring
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    # This is the next preference which is focust on the location in which the downloaded file can be saved
    # As a second argument, we can either pass 0, 1 or 2. When you pass 0, the file will be downloaded on the desktop
    # When you pass 1, the file will be downloaded and be saved in the default location (downloads folder)
    # But if you pass 2, the file will be downloaded and saved in the desired location that should clearly specified
    ops.set_preference("browser.download.folderList", 2)
    # Specified location
    ops.set_preference("Browser.download.dir", location)

    # For when the PDF file gets opened instead of getting downloaded
    # But I did not need this line, because the file was downloaded, not opened
    # ops.set_preference("pdfjs.disable", True) # For pdf

    # Use this link to find the file types
    # https://www.sitepoint.com/mime-types-complete-list/

    driver = webdriver.Firefox(service=service, options=ops)  # Browser launcher
    return driver



# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

wait=WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException, ElementNotSelectableException]) #Explicit wait.

driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()

# By default, the downloaded files are saved win the downloads folder
# But we can temporarily change the default location
download4 = driver.find_element(By.XPATH, "//*[@id='content']/div/a[66]")
download4.click()


time.sleep(5)