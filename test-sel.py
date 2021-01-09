#! /usr/bin/python3


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"


options = webdriver.ChromeOptions()
options.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
driver.get("https://www.imbd.com")

#print(driver.page_source.encode('utf-8'))
print("landing page ------------------>")
print("current_url", driver.current_url)
print("title", driver.title)

WAIT_ELEMENT = 30
XPATH_VALUE = "//*[@id=\"imdbHeader\"]/div[2]/div[5]/a/div"
x = WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.PATH,XPATH_VALUE)))
outer = x.get_attribute('outerHTML')
print("outerHTML")
time.sleep(5)
x.click()

print("\n", "signinin page ----->")
print("current_url", driver.current_url)
print("title", driver.title)


driver.close()
driver.quit()




