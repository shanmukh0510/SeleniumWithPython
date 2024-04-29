import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
#locator matching with single web element
driver.find_element(By.XPATH,"//*[@id='navbar-brand-centered']/ul[1]/li[1]/a").click()
driver.find_element(By.LINK_TEXT,"Simple Form Demo").click()
driver.find_element(By.XPATH,"//input[@id='user-message']").send_keys("good morning")
driver.find_element(By.XPATH,"//button[normalize-space()='Show Message']").click()
driver.close()

#locator matching with multiple web elements
