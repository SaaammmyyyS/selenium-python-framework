from basepage import BasePage
import custom_logger as cl
import logging
import time

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Sign Up or Log In"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@type='submit']"
    _search_box = "search"
    _enter_search = "//button[@type='submit']"
    _choice_course = "//h4[@class='dynamic-heading']"
    _enroll_course = "//span[@class='fas fa-arrow-circle-right btn-icon-after']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"



    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def enterCourse(self, course):
        self.sendKeys(course, self._search_box, locatorType="id")

    def clickSearch(self):
        self.elementClick(self._enter_search, locatorType="xpath")

    def clickCourse(self):
        self.elementClick(self._choice_course, locatorType="xpath")

    def clickEnroll(self):
        self.elementClick(self._enroll_course, locatorType="xpath")

    def enterNum(self, num):
        self.switchToFrame(index=0)
        self.sendKeys(num, self._cc_num, "xpath")




    def register(self, email="", password="", course="", num=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(2)
        self.enterCourse(course)
        self.clickSearch()
        self.clickCourse()
        self.clickEnroll()
        self.webScroll(direction="down")
        # self.enterNum(num)
        time.sleep(2)