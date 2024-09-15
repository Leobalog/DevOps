import pytest
from time import sleep
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from assertpy import assert_that


class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')
        a = 1

class TestReg(WebBase):
    
    def test_register(self):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements.username.set('plupp')
        RegisterPage(self.driver).elements.password1.set('test1234')
        RegisterPage(self.driver).elements.password2.set('test1234')
        RegisterPage(self.driver).elements.register.click()
        assert_that(RegisterPage(self.driver).elements.username_registered.text).is_equal_to('User already exists!')
        # assert_that(RegisterPage(self.driver).elements.username_logged_in.text).is_equal_to(unique_username)
        a = 2