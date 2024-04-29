# Browser_Commands

# 1) close() - closes single browser window(where driver focused)
# 2) quit()  -close multipule browser windows(this will kill the process)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
driver.find_element(By.XPATH,"/html/body/footer/div/div[2]/ul/li[1]/a").click()
time.sleep(5)
driver.close()