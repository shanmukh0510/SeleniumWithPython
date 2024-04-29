# Conditional Commands

# 1) is_displayed  - used for any kind of element
# 2) is_enabled    - used for any kind of element
# 3) is_selected   - used for radio buttons and check boxes

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
username_textbox = driver.find_element(By.ID, "email")
print(username_textbox.is_displayed())              #is_displayed
print(username_textbox.is_enabled())                #is_enabled
driver.close()


#is _selected
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/basic-radiobutton-demo.html")
rb_male = driver.find_element(By.XPATH, "//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[1]/input")
rb_female = driver.find_element(By.XPATH, "//*[@id='easycont']/div/div[2]/div[1]/div[2]/label[2]/input")
print(rb_male.is_selected())
print(rb_female.is_selected())
driver.close()