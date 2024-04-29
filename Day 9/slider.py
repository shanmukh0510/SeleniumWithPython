import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print(slider.location)            # {'x': 903, 'y': 1092}
action = ActionChains(driver)
action.drag_and_drop_by_offset(slider, 903, 1092).perform()
time.sleep(5)