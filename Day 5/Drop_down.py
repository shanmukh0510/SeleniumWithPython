
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
dropdown_ele = driver.find_element(By.XPATH, "")
dropdown = Select(dropdown_ele)
#select option from the dropdown
# dropdown.select_by_visible_text("")
# dropdown.select_by_value("")
# dropdown.select_by_index()

#capture all the options and print them
alloptions = dropdown.options
print("total number of options:",len(alloptions))



for option in alloptions:
    print(option.text)

#select option from dropdown without using built in functions

for option in alloptions:
    if option.text =="":
        option.click()
        break

#without select tag we can print like this


