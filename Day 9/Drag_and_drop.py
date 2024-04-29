import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

source = driver.find_element(By.XPATH, "//div[@id='draggable']")
destination = driver.find_element(By.XPATH, "//div[@id='droppable']")
action = ActionChains(driver)
action.drag_and_drop(source, destination).perform()
