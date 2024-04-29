import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

textbox = driver.find_element(By.XPATH, "//input[@id='field1']")
textbox.clear()
textbox.send_keys("welcome")
button = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
action = ActionChains(driver)
action.double_click(button).perform()
