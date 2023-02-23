from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

username = "hyderabad"
password = "OscarMike!)!$"
print("WELCOME TO EBILLING CLI")
panel_name = input("Please enter the panel name: ")
date = input("Please enter the date in this format yy-mm-dd: ")

driver = webdriver.Firefox()
class rechargeUser():

    def __init__(self, panel_name, username, password, date):
        self.panel_name = panel_name
        self.username = username
        self.password = password
        self.date = date
        
    def login(self):
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://ebilling.ispworld.co")

        username_elem = driver.find_element(By.XPATH, "//input[@name='username']")
        username_elem.send_keys(self.username)

        password_elem = driver.find_element(By.XPATH, "//input[@name='password']")
        password_elem.send_keys(self.password)

        login_elem = driver.find_element(By.XPATH, "//button[@name='login_user']")
        login_elem.click()

        driver.implicitly_wait(5)

       
    # def selectDealer(self):
    #     Dealer.selectingDealer()

    def selectCustomerList(self):
        driver.find_element(By.XPATH, "//i[@class='nc-icon nc-circle-10']//following-sibling::p").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//a[@href='userlist.php']//span[contains(text(), 'User List')]").click()
       

    def selectDealer(self):
        dealer = driver.find_element(By.XPATH, "//a[@class='chosen-single']//span[1]")
        dealer.click()
        driver.implicitly_wait(2)
        
        search = driver.find_element(By.XPATH, "//div[@class='chosen-search']//input[1]")
        search.send_keys(self.panel_name)

        driver.find_element(By.XPATH, "//ul[@class='chosen-results']//li[1]").click()
        driver.implicitly_wait(2)


    def selectUser(self): 

        tbody = driver.find_element(By.XPATH, "//tbody[@id='tbodys']")
        user = tbody.find_element(By.XPATH, "//td[@class='sorting_1']//a[1]")
        user.click()
        driver.implicitly_wait(2)

        #Setting Date of the user

        calender = driver.find_element(By.XPATH, "//input[@class='form-control' and @type='date']")
        calender.clear()
        calender.send_keys(self.date)

        #Update User

        update = driver.find_element(By.NAME, "update_franchise_user")
        update.click()







recharge = rechargeUser(panel_name, username, password, date)
recharge.login()
recharge.selectCustomerList()
recharge.selectDealer()
recharge.selectUser()
recharge


    
