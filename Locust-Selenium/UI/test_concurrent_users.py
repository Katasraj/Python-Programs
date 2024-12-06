import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import time
import pytest
import allure

@allure.step("Executing session")
def run_test(session_name):
    """
    Function to run individual Selenium tests.
    Each session gets its own WebDriver instance.
    """
    driver = webdriver.Chrome()  # Each thread creates its own WebDriver instance
    driver.implicitly_wait(10)
    driver.maximize_window()

    try:
        start_time = time.time()
        with allure.step("Opening saucedemo website"):
            driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        with allure.step("Entering Username"):
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(2)

        with allure.step("Entering Password"):
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(2)

        with allure.step("Click on login button"):
            driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        with allure.step("Adding an item to cart"):
            driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Backpack')]/../../..//button").click()
        time.sleep(2)

        with allure.step("Removing an item from cart"):
            driver.find_element(By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]/../../..//button").click()
        time.sleep(2)

        print(f"{session_name}: Test completed successfully")
        end_time = time.time()
        print(f"Page Load Time for {session_name}: {end_time - start_time} seconds")

    except Exception as e:
        print(f"{session_name}: Test failed - {e}")

    finally:
        driver.quit()  # Ensure WebDriver instance is closed for each thread


#@pytest.mark.usefixtures("test_setup")
@allure.description("With 5 users Entering Username and Password and adding/removing an item from cart")
def test_concurrent_sessions():
    """
    Test function that runs Selenium tests in multiple threads.
    """
    @allure.step("Executing Threads")
    def execute_concurrent_sessions():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Create session names for identification
            sessions = [f"Session-{i}" for i in range(5)]
            # Each thread runs `run_test`
            executor.map(run_test, sessions)

    execute_concurrent_sessions()


#//button[contains(text(),'Add to cart')]

#//div[contains(text(),'Sauce Labs Backpack')]/../../..//div[@class='pricebar']//button
#//div[contains(text(),'Sauce Labs Backpack')]/../../..//button