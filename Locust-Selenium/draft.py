import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
t = driver.title
print(type(t))   # Swag Labs
driver.quit()