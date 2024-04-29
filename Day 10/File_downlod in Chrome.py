import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()

def chrome_setup():
    # download files in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

my_driver = chrome_setup()

my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.maximize_window()
my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()



