import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("")

button = driver.find_element(By.XPATH, "")

action = ActionChains(driver)

action.context_click(button).perform()


