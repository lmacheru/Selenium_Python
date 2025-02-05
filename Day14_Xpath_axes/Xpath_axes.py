# Xpath axes key words:
# self
# parent
# child
# ancestor
# descendant
# following
# following-sibling
# preceding
# preceding-sibling

# Self is a "node" itself
# Parent is a node that is at the top of another node
# Child is node that is at the bottom of self
# So 1,2,3 can be considered ancestor,parent and child nodes respectively
# If we start from a child: 3,2,1 ---> 3 is the descendant of 1 but the child of 2 and 3 can be called self

# Following
# Nodes that are categorised "following-sibling" are siblings of self that come after self
# Nodes that are categorised "preceding-sibling" are siblings of self that come before self

# Why do we need this??
# Suppose we want to identify an element that does not have attributes, we can identify near by element, write an Xpath
# to that element, and then from there we can navigate to the actual element.
# So that means we can start from any node, and then we can navigate to any other node in the same DOM structure

from selenium import webdriver

# Selenium is a package and inside this package there is webdriver module, and inside this module there is chrome etc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:\Automation_Testing_Drivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service) #Browser launcher

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# The text property will capture the value (textContent) of this element

# Self
# This self keyword points at the same element
# text_msg = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[12]/td[1]/a/self::a").text
# print(text_msg) #Castrol India

# Parent
# Here we are trying to locate the parent and its text. So if the parent does not have the text the
# then the value of its child element gets used or printed out as it was saved in text_msg
#---------------------------------------------------------------self node---------------------------parent node
# text_msg = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[12]/td[1]/a/parent::td").text
# print(text_msg) #Castrol India

# Child Element ---> Ancestor
# Here we jump from the grand child to ancestor node, and then from this ancestor node, we go to the child nodes
# of the ancestor and get their texts
# text_msg = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[12]/td[1]/a/ancestor::tr/child::td")
# print(len(text_msg)) #Castrol India
#
# for i in text_msg:
#     print(i.text)

# Ancestor
# Getting a text of an ancestor node
# So tr does not have a a text, this results in its children texts being printed out instead
# text_msg = driver.find_element(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[12]/td[1]/a/ancestor::tr").text
# print(text_msg) #Castrol India A 207.50 219.50 + 5.78 Buy  |  Sell


# Descendant node
# Getting a text of descendant using the grand,grand parent
# We firstly go to the ancestor because the self does not have descendants, then from there we go to descendants
# If you do not know what are the descendants of the ancestor, use the star *
# text_msg = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[12]/td[1]/a/ancestor::tr/descendant::*")
# print(len(text_msg)) #10

# # Following - everything that comes after the element, not just the siblings
# following_elements = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[259]/td[1]/a/ancestor::tr/following::*")
# print(len(following_elements)) #719

# Following-Sibling - on a parallel line

# For the element that does not have the following-sibling, we have to go to the ancestor first
# following_elements = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[259]/td[1]/a/ancestor::tr/following-sibling::*")
# print(len(following_elements)) #137 siblings


# Preceding - everything that comes before the element, not just the siblings
# following_elements = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[259]/td[1]/a/ancestor::tr/preceding::*")
# print(len(following_elements)) #3011 siblings

# Preceding-sibling - on a parallel line
following_elements = driver.find_elements(By.XPATH, "//*[@id='leftcontainer']/table/tbody/tr[259]/td[1]/a/ancestor::tr/preceding-sibling::tr")
print(len(following_elements)) #258 siblings



















