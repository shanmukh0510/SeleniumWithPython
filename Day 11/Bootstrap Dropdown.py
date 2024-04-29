
# Bootstrap Dropdown

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/jquery-dropdown-search-demo.html")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").click()
time.sleep(5)