import pytest
from tests.web.test_base import WebBase
from tests.web.pages.login_page import Registerpage

class TestWeb(WebBase):

    def test_register(self):
        Registerpage(self.driver).elements.register.click()
        Registerpage(self.driver).elements.username.set('')
        Registerpage(self.driver).elements.password1.set('')
        Registerpage(self.driver).elements.password2.set('')
        Registerpage(self.driver).elements.register.click()
        