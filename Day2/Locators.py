# Identify
# element action

# <input id='sddsd' name='sadasd'> Name: </input>
# <a href="link"> register </a>
# register is a link text

# id
# name
# link text
# partial link text

# class name
# tag name


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.applitools.com/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("shanmukharao9010@gmail.com")  # ID
driver.find_element(By.ID, "password").send_keys("8985912662")  # ID
driver.find_element(By.LINK_TEXT, "Sign in").click()  # Link_TEXT
time.sleep(5)
