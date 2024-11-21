from selenium import webdriver
from selenium.webdriver.common.by import By

class Cred:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def Inatialize(self,url):
        return self.driver(url)


# if __name__ == '__main__':
#     obj = Cred()
#     obj.Inatialize('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')