from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
login_form = driver.find_element(By.ID, 'login_form')