import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# #1) scroll down the page by pixel

# driver.execute_script("window.scrollBy(0,1200)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("number of pixels moved :", value)
# time.sleep(5)


# #2) scroll down page till element is visible

# ele = driver.find_element(By.XPATH, "//h2[normalize-space()='Web Table']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# value = driver.execute_script("return window.pageYOffset;")
# print("number of pixels moved :", value)

# scroll down till end of the page(

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")   # scroll top to bottom
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved :", value)

# scroll up to starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")   # scroll top to bottom
value = driver.execute_script("return window.pageYOffset;")
print("number of pixels moved :", value)

