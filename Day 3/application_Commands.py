# Commands

# 1)get commands 0r application specific commands
# 2)conditional commands
# 3)browser commands
# 4)navigational commands
# 5)wait commands

# get commands 0r application specific commands

# 1)get()         - Opening the application url
# 2)title         -to capture the title of the current web page
# 3)current_url   -to capture the url of the current web page
# 4)page_source   _to capture the page_source of the current web page

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.maximize_window()
exp_title = driver.title
exp_url = driver.current_url
exp_pagesource = driver.page_source
print(exp_title)
print(exp_url)
print(exp_pagesource)
driver.close()


