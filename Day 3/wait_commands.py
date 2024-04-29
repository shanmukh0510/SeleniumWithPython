#wait commands
# 1) implicitly_ wait()
# 2) explicitly_wait()


# we use wait commands to solve synchronization problems(between application and script)
# time.sleep(seconds)
#          Advantages
#          * easy to use
#          Disadvantages
#          * performance of the script is very poor
#          * if the element is not available in the within time mentioned still there is a chance of getting exception

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Date pickers']").click()
driver.close()


# 1) implicitly_ wait()
#          Advantages
#            * single statement
#            * performance will not be reduced.(if the element is available within the time it proceed to execute further statement)
#          Disadvantages
#             * if the element is not available in the within time mentioned still there is a chance of getting exception

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Date pickers']").click()
driver.close()



# 2) explicitly_wait()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10)
driver.maximize_window()
driver.get("http://demo.seleniumeasy.com/")
#driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Date pickers']").click()
mywait.until(EC.presence_of_element_located(By.XPATH,))
driver.close()
