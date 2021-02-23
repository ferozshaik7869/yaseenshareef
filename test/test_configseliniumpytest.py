# from lib2to3.pgen2 import driver
#
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#
from test02.classBase.Baseclass import Base
from test02.pageobjects.loginpage import LoginPage
from test02.classBase.Baseclass import Base
from test02.pageobjects import locator

class TestEmployee():
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\Admin\PycharmProjects\ferozproject\Chrome\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        yield
        self.driver.quit()

    def test_login(self,setup):
        txt_username = self.driver.find_element(By.ID, "email")
        txt_username.send_keys("mohammadferoz_210@yahoo.co.in")
        txt_password = self.driver.find_element(By.ID, "pass")
        txt_password.send_keys("shareef@yasin")

        btn_lgn = self.driver.find_element(By.XPATH, "//button[@value='1']")
        btn_lgn.click()

