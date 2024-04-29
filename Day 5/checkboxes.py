import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
driver.find_element(By.XPATH,"//a[@class='dropdown-toggle'][normalize-space()='Input Forms']").click()
driver.find_element(By.LINK_TEXT,"Checkbox Demo").click()
checkboxs = driver.find_elements(By.XPATH,"//input[@class='cb1-element']")
# print(len(checkboxs))
#
# #select all checkboxes
# #approch 1
# for checkbox in checkboxs:
#     checkbox.click()
#
#
# #approch 2
# for i in range(len(checkboxs)):
#     checkboxs[i].click()

#select multiple checkboxes by choice
time.sleep(5)
for checkbox in checkboxs:
    checkboxname = checkbox.text
    if checkboxname == 'Option 3' or checkboxname == 'Option 1':
        checkbox.click()
        time.sleep(5)




