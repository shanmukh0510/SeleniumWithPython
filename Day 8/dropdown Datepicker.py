# drop down date picker
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/datepicker/#Simple%20Date%20Picker")
driver.find_element(By.XPATH, "//li[@id='DropDown DatePicker']")
driver.switch_to.frame(3)
time.sleep(5)
driver.find_element(By.ID, "datepicker")
time.sleep(5)
