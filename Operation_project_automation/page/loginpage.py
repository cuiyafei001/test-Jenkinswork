from Operation_project_automation.common.base import Base
from selenium import webdriver

# 继承过来的类，里面的方法可以直接self.调用，不需要实例化


class LoginPage(Base):
    """登录页面"""
    user_loc = ("xpath", ".//*[@type='text']")  # 输入账号
    psw_loc = ("xpath", ".//*[@type='password']")  # 输入密码
    sub_loc = ("xpath", ".//*[@type='button']")    # 点登录
    zhanghao_loc = ("xpath", ".//*[@class='tooltip-name']")

    def open_login_page(self):
        self.driver.get("http://10.111.2.162:8899/#/login")

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies()  # 删除所有的cookies
        self.driver.refresh()

    def input_username(self,usrname):
        '''输入账号'''
        self.sendKeys(self.user_loc, usrname)

    def input_psw(self, psw):
        '''输入密码'''
        self.sendKeys(self.psw_loc, psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click(self.sub_loc)

    def login(self, username, psw):
        '''登录流程:'''
        self.open_login_page()
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            t = self.findElement(self.zhanghao_loc).text
            print(t)
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    a = LoginPage(driver)
    a.open_login_page()
    a.login(username='ss', psw='45')
    a.get_login_result()
    driver.quit()


