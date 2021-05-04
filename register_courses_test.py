from selenium.webdriver.common.by import By
from register_courses_page import RegisterCoursesPage
from teststatus import TestStatus
from ddt import ddt, data, unpack
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners"), ("Python"))
    def test_invalidLogin(self, course_name):
        self.lp.register(email="test@email.com", password="abcabc", course=course_name)
        self.lp.driver.get("https://letskodeit.com/courses/")