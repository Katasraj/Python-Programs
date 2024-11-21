import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture()
def test_setup():
    # Use ChromeDriverManager to automatically manage ChromeDriver installation
    global driver
    # driver_service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()

@allure.description("Validates OrangeHRM with valid login credentials")
@allure.severity(severity_level="CRITICAL")
def test_ValidateLogin(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.find_element(By.XPATH,"//input[@name='username']").clear()
    enter_username('Admin')
    #driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
    driver.find_element(By.XPATH,"//input[@type='password']").clear()
    enter_password('admin123')
    #driver.find_element(By.XPATH,"//input[@type='password']").send_keys('admin123')
    driver.find_element(By.XPATH,"//button[@type='submit' and normalize-space()]").click()
    current_url = driver.current_url
    assert 'dashboard' in current_url
    time.sleep(5)

@allure.description("Validates OrangeHRM with Invalid login credentials")
@allure.severity(severity_level="NORMAL")
def test_InvalidLogin(test_setup):
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.find_element(By.XPATH,"//input[@name='username']").clear()
    enter_username('Admin')
    driver.find_element(By.XPATH,"//input[@type='password']").clear()
    enter_password('admin124')
    driver.find_element(By.XPATH,"//button[@type='submit' and normalize-space()]").click()
    time.sleep(10)
    current_url = driver.current_url
    try:
        assert 'dashboard' in current_url
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name='Invalid Credentials',attachment_type=allure.attachment_type.PNG)
    time.sleep(5)

@allure.step("Entering Username as {0}")
def enter_username(username):
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)

@allure.step("Entering Password as {0}")
def enter_password(password):
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

# def test_teardown():
#     driver.quit()