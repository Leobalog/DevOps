import pytest
from time import sleep
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.calculate_page import CalculatePage
from assertpy import assert_that


class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')
        a = 1



class Testcalculator(WebBase):
    def test_add(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()
        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('3')

        a = 3
 
class Testcalculator(WebBase):
    def test_sub(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keysubtract.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyequals.click()
        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('1')

        a = 4


class Testcalculator(WebBase):
    def test_multiply(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keymultiply.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyequals.click()
        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('2')

        a = 5


class Testcalculator(WebBase):
    def test_div(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keydivide.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyequals.click()
        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('2')

        a = 6

class Testhistory(WebBase):
    def test_history(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()

        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        CalculatePage(self.driver).elements.key5.click()
        CalculatePage(self.driver).elements.keysubtract.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        CalculatePage(self.driver).elements.historybutton.click()        

        assert_that(CalculatePage(self.driver).elements.historypanel.value).is_equal_to('1+2=3\n5-2=3\n')

        a = 7