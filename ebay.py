import requests
import bs4
import names
import random
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


product_link = input("Product Link: ")
class EbayBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False);
        options.add_argument("disable-infobars")
        options.add_argument('disable-extensions')
        self.driver = webdriver.Chrome(options=options)
    def watchitem(self):
        first_name = names.get_first_name().replace(" ", "")
        last_name = names.get_last_name().replace(" ", "")
        email = f"{first_name.lower()}.{last_name.lower()}@hotmail.rs"
        password = f"{first_name}{random.randrange(1, 10000)}{random.choice(['$#@', '$%', '$*^()'])}"
        sys.stdout.write(f"\rFull Name: {first_name} {last_name} | Email: {email} | Password: {password}")
        sys.stdout.flush()
        self.driver.get("https://reg.ebay.com/reg/PartialReg")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@class="giant-text-2"]')))
        self.driver.find_element_by_xpath('//input[@name="firstname"]').send_keys(first_name)
        self.driver.find_element_by_xpath('//input[@name="lastname"]').send_keys(last_name)
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys(email)
        self.driver.find_element_by_xpath('//input[@name="PASSWORD"]').send_keys(password)
        self.driver.execute_script('document.querySelector("#ppaFormSbtBtn").click()')
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Daily Deals')]")))

eBay = EbayBot()
eBay.watchitem()

