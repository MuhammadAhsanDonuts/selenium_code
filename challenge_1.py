from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://www.seleniumhq.org/")

"""
Locating elements
"""

elem = driver.find_element(By.ID, "q")
print(elem)

elem = driver.find_element(By.NAME, "q")
print(elem)

"""elem = driver.find_element(By.XPATH, "//")"""

elem = driver.find_element(By.CLASS_NAME, "selenium-sponsers")
print(elem)