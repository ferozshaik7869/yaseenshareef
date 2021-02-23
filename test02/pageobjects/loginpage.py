from selenium import webdriver
from selenium.webdriver.common.by import By
from test02.classBase.Baseclass import Base
# from test02.locatorss import btn_login_xpath
from test02 import locatorss
import pytest


class LoginPage:
    def __init__(self,driver):
        self.txt_username=driver.find_element(By.ID,locatorss.txt_username_id)
        self.txt_password=driver.find_element(By.ID,locatorss.txt_password_id)
        self.btn_login=driver.find_element(By.ID,locatorss.btn_login_xpath)
        # self.btn_create_new=driver.find_element(By.XPATH,locator.btn_create_newxpath)

    def getTxtUserName(self):
        return self.txt_username
    def getTxtPassWord(self):
        return self.txt_password
    def getBtnLogin(self):
        return self.btn_login
    # def getBtnCreateNew(self):
    #     return self.btn_create_new

