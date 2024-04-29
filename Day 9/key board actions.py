 # Key Board actions

 # CONTROL + A
 # CONTROL + C
 # TAB
 # CONTROL + V

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://text-compare-online.com/")
textbox_1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
textbox_2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
textbox_1.send_keys("good morning")
action = ActionChains(driver)
# CONTROL + A
action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(5)
# CONTROL + C
action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# press TAB
action.send_keys(Keys.TAB)
time.sleep(5)
# CONTROL + V
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)
driver.find_element(By.XPATH, "//b[normalize-space()='Compare Text']").click()
driver.close()

