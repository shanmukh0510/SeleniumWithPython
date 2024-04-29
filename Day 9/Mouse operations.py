
# Mouse operations

# ActioChains class avilable to perform mouse actions

# 1) Mouse hover        #move_to_element(element)
# 2) Right Click        #context_click(element)
# 3) Double Click       #double_click(element)
# 4) Drag and Drop      #drag_and_drop(source,target)

# slider                drag_and_drop_offset(element,X,Y)

 # mouse hover
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("")

ele1 = driver.find_element(By.XPATH, "")
ele2 = driver.find_element(By.XPATH, "")
ele3 = driver.find_element(By.XPATH, "")

action = ActionChains(driver)
action.move_to_element(ele1).move_to_element(ele2).move_to_element(ele3).click().perform()
