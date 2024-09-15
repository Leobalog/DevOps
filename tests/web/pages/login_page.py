from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'login': Element('//button[@id="login"]', self),
        }

        self.elements = munchify(self.page_elements)


class Registerpage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'register': Element('//button[@id="register"]', self),
        }

        self.elements = munchify(self.page_elements)