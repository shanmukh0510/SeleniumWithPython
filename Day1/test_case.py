#
# Selenium WebDriver
# What is WebDriver?
# -> WebDriver is One of the component in selenium.
# -> WebDriver is module
# firefox browser -> Firefox()
# Chrome Browser ---> Chrome ()
# Edge---> Edge()
# ---|

# -> WebDriver is an API (Application Programming Interface)
# Architecture of WebDriver
# Selenium3
# Selenium Language bindings--JSON Wire protocol---> Browser drivers---w3c--> Browsers Selenium4
# Selenium Language bindings--w3c---> Browser drivers---w3c--> Browsers


# Setup & configure WebDriver in Pycharm
# Pre-requisites:
# Python Pychamp
# 1) Download browser specific drivers using below links....
# Chrome: https://chromedriver.chromium.org/downloads
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Firefox:
# https://github.com/mozilla/geckodriver/releases
# Once you downloaded, extract .zip files then you will se .exe files (they are drivers)
# 2) setup selenium webdriver
# Approach#1:
# pip install selenium==4.0.0.b4
# pip install selenium
# Approach#2:
# or through Pycharm project settings...


# Test Case
# 1) Open Web Browser (Chrome/firefox/IE).
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3) Provide Email
# (admin@yourstore.com).
# 4) Provide password (admin).
# 5) Click on Login.
# 6) Capture title of the dashboard page. (Actual title)
# 7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected) 8) close browser

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.find_element(By.ID, "email").send_keys("shanmukharao9010@gmail.com")
driver.find_element(By.ID, "password").send_keys("8985912662")
driver.find_element(By.ID, "submit").click()
time.sleep(5)
driver.find_element(By.ID, "logout").click()
act_title = driver.title
exp_title = "Contact List App"
if act_title == exp_title:
    print("test passed")

else:
    print("test failed")



