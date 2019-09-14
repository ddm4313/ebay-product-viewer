from selenium import webdriver
import uuid, time, names

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False);
options.add_argument("disable-infobars")
options.add_argument('disable-extensions')
driver = webdriver.Chrome(options=options)
link = input("eBay Product Link: ")
while True:
    driver.delete_all_cookies()
    driver.get('https://reg.ebay.com/reg/PartialReg?ru=https%3A%2F%2Fwww.ebay.com%2F')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@id="firstname"]').send_keys(names.get_first_name())
    driver.find_element_by_xpath('//input[@id="lastname"]').send_keys(names.get_last_name())
    driver.find_element_by_xpath('//input[@id="email"]').send_keys('%s@gmail.com' % uuid.uuid4())
    driver.find_element_by_xpath('//input[@id="PASSWORD"]').send_keys('Steve3142145$DSADAS525151')
    time.sleep(0.75)
    driver.execute_script("document.getElementById('ppaFormSbtBtn').click()")
    driver.get(link)
    time.sleep(0.65)
    driver.find_element_by_xpath('//span[@class="vi-atw-txt"]').click()
