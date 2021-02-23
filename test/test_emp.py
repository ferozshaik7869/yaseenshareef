from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test02.pageobjects.loginpage import LoginPage
from test02.classBase.Baseclass import Base


class Testlogin(Base):


    @pytest.fixture()
    def setup(self):
        driver=self.launch_browser()
        self.load_url("https://www.facebook.com/")
        yield
        self.quit_browser()
    def test_login(self,setup):
        l=LoginPage(self.driver)
        self.type(l.getTxtUserName(),"mohammadferoz_210@yahoo.co.in")
        self.type(l.getTxtPassWord(),"shareef@yasin")
        self.btn_login(l.getBtnLogin())


#practice of pytest fixtures:
class Testlogin(Base):
    @pytest.fixture()
    def setup(self):
        driver=self.launch_browser()
        self.load_url("https://www.facebook.com/")
        yield
        self.quit_browser()
    def test_login(self,setup):
        l1=LoginPage(self.driver)
        self.type(l1.getTxtUserName(),"mohammad")
        self.type((l1.getTxtPassWord(),"shareefyasin"))
        self.btn_login(l1.getBtnLogin())


#
import pytest
from test02.classBase.Baseclass import Base
from test02.pageobjects.loginpage import LoginPage


class Testlogin(Base):

    @pytest.fixture()
    def setup(self):
        driver = self.launch_browser()
        self.load_url("https://www.facebook.com")
        yield
        self.quit_browser()

    @pytest.mark.parametrize("username,password", [("shaik","7866"),("hello","7899"),("jai","7855")])

    def test_login(self, setup, username,password):
        l2 = LoginPage(self.driver)
        self.type(l2.getTxtUserName(),username)
        self.type(l2.getTxtPassWord(),password)
        self.btn_login(l2.getBtnLogin())
