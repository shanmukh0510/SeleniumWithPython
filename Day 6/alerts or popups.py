# alerts / popups
#alert window is not a web element
# myalert = driver.switch_to.alert  # first create alert variable

# myalert.text
# myalert.accept()
# myalert.dismiss()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
driver.find_element(By.XPATH, "").click()
time.sleep()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("")
alertwindow.accept()                 #clicks ok
#alertwindow.dismiss()               #clicks cancel

#Authantication popup

# syntax :  http://username:password@test.com
#           http://username:password@demo.seleniumeasy.com/
