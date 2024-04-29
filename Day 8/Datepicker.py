
# Date Picker
# 1) standard
# 2) non standard(customized)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//input[@class='hasDatepicker']").send_keys("08/10/2023")
# time.sleep(5)
date = "31"
month = "December"
year = "2010"

driver.find_element(By.XPATH, "//input[@class='hasDatepicker']").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yer = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yer == year:
        break
    else:
        #driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

time.sleep(5)
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody//tr//td//a") # next arrow
time.sleep(5)
for ele in dates:
    if ele.text == date:
        ele.click()
        break
    print(ele.text)
time.sleep(5)






