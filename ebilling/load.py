from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


username = "hyderabad"
password = "OscarMike!)!$"
# dealer = input("Enter the dealer name: ")
# amount = input("Enter the amount: ")
driver = webdriver.Firefox()

class Dealer():

    def __init__(self, username, password, dealer, amount):
        self.username = username
        self.password = password
        self.dealer = dealer
        self.dealer_amount = amount
  
    def login(self, username, password):
    
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://ebilling.ispworld.co")

        username_elem = driver.find_element(By.XPATH, "//input[@name='username']")
        username_elem.send_keys(username)

        password_elem = driver.find_element(By.XPATH, "//input[@name='password']")
        password_elem.send_keys(password)

        login_elem = driver.find_element(By.XPATH, "//button[@name='login_user']")
        login_elem.click()

        driver.implicitly_wait(5)

       

    def selectingDealer(self, dealer):

        dealer_elem1 = driver.find_element(By.XPATH, "//a[@href='dealerlist.php']//p[1]")
        dealer_elem1.click()

        dealer_elem = driver.find_element(By.XPATH, f"//a[contains(text(), '{dealer}')]")
        dealer_elem.click()


    def load(self, amount):
        rechargeBtn = driver.find_element(By.XPATH, "//button[@id='recharge']")
        rechargeBtn.click()
        driver.implicitly_wait(1)
    
        topup_type = Select(driver.find_element(By.XPATH, "//select[@id='topup_type']"))
        time.sleep(2)
        topup_type.select_by_index(2)

        value = driver.find_element(By.XPATH, "//input[@type='number' and @name='value']")
        value.clear()
        value.send_keys(str(amount))
        

        submitBtn = driver.find_element(By.XPATH, "//button[@id='submit_topup']")
        submitBtn.click()



# load = Dealer(username, password, dealer, amount)
# load.login(username, password)
# load.selectingDealer(dealer)
# load.load(amount)
if __name__=="__main__":
    dealer = input("Enter the dealer name: ")
    amount = input("Enter the amount: ")
    load = Dealer(username, password, dealer, amount)
    load.login(username, password)
    load.selectingDealer(dealer)
    load.load(amount)