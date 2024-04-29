# Navigational Comands
# 1) back()
# 2) forward()
# 3) refresh()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
print(driver.current_url)
driver.find_element(By.XPATH,"/html/body/footer/div/div[2]/ul/li[1]/a").click()
print(driver.current_url)
time.sleep(5)
driver.back()
driver.forward()
driver.refresh()
time.sleep(5)
driver.close()