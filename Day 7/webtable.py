# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# # count number of rows and columns in table
# driver.get("https://testautomationpractice.blogspot.com/")
# numberofrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
# print("no of rows", len(numberofrows))
#
# numberofcoloumns = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")
# print("no of colm",len(numberofcoloumns))
#
# # Read specific data from roe and column
# data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[7]/td[1]").text
# print(data)
#
# # read all the rows and columns in data table
# #
# # for r in range(1, numberofrows+1):
# #     for c in range(1, numberofcoloumns+1):
# #         alldata = driver.find_element(By.XPATH,"table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
# #         print(alldata,end='')
#
# for r in range(1, numberofrows + 1):
#     for c in range(1, numberofcoloumns + 1):
#         alldata = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
#         print(alldata, end='')

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
# count number of rows and columns in table
driver.get("https://testautomationpractice.blogspot.com/")
numberofrows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print("no of rows", numberofrows)

numberofcoloumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
print("no of colm", numberofcoloumns)

# Read specific data from row and column
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[7]/td[1]").text
print(data)

# read all the rows and columns in data table
for r in range(1, numberofrows + 1):
    for c in range(1, numberofcoloumns + 1):
        alldata = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(alldata, end='')
