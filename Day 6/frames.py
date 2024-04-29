# frame/iframe

# switch_to_frame     #selenium 3

# selenium 4
# switch_to.frame(name of the frame)
# switch_to.frame(Id of the frame)
# switch_to.frame(webelement)
# switch_to.frame(0)  #index

# switch_to.default_content()

# recognize frames in html with tag name

 #frame
 #iframe
 #form

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
driver.switch_to.frame("")
driver.find_element(By.XPATH, "").click()
driver.switch_to.default_content()              #go back to main page
driver.switch_to.frame("")
driver.find_element(By.XPATH, "").click()
driver.switch_to.default_content()              #go back to main page
driver.switch_to.frame("")
driver.find_element(By.XPATH, "").click()


#  inner frame