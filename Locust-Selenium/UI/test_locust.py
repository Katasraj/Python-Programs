import time

from locust import User,HttpUser, task, between
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

class SeleniumUser(HttpUser):
    host = os.getenv("LOCUST_HOST")
    wait_time = between(1, 10)  # Time between tasks

    def on_start(self):
        """Setup Selenium WebDriver"""
        options = Options()
        options.add_argument("--headless")  # Optional: Run in headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service("path/to/chromedriver")  # Update with the path to your ChromeDriver
        #self.driver = webdriver.Chrome(service=service, options=options)
        self.driver = webdriver.Chrome()


    @task
    def on_stop(self):
        """Quit the WebDriver session"""
        self.driver.quit()

    @task
    def login_test(self):
        """Perform login functionality"""
        self.driver.get("https://www.saucedemo.com/")


        # Simulate login
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce1")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Verify login success
        assert "Swag Labs" in self.driver.title

        #self.driver.quit()

