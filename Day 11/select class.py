import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("ind")
time.sleep(5)
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for country in countries:
    # print(country.text)
    if "ind" in country.text.lower():
        print(country.text)




