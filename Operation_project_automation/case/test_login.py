# coding:utf-8
from Operation_project_automation.page.loginpage import LoginPage
from selenium import webdriver
import unittest


class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpage = LoginPage(cls.driver)

    # def login_case(self, username, psw):
    #     """lonin"""
    #     pass
    #     # self.loginpage.login(username, psw)
    #     # result = self.loginpage.get_login_result()
    #     # return result

    def test_login1(self, username='cyf-01', psw='Abc123456.'):  #
        """SuccessCase"""
        self.loginpage.login(username, psw)
        result = self.loginpage.get_login_result()
        self.assertTrue(result == 'cyf-01')

    def test_login2(self, username='cyf-1245', psw='123456'):
        """failcase"""
        self.loginpage.login(username, psw)
        result = self.loginpage.get_login_result()
        self.assertTrue(result == 'cyf-01')

    # def log_out(self):
    #     self.loginpage.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
