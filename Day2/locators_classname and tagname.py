from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/services.htm")
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(5)
sliders = driver.find_elements(By.CLASS_NAME, "input")
print(len(sliders))
time.sleep(5)

links = driver.find_elements(By.TAG_NAME, "li")
print(len(links))
