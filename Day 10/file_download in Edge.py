import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()
print(location)
def edge_setup():
    # download files in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(options=ops)
    return driver

my_driver = edge_setup()

my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
my_driver.maximize_window()
time.sleep(5)
my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)