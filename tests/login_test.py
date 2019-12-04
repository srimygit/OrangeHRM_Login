import allure
#import moment
from selenium import webdriver
import time
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    #pass the test_setup parameter so that it is taken as the pytest fixture
    # the argument "self" should be used when we have a class defined
    def test_login(self):
        print("Starting the test")
        driver = self.driver
        driver.get(utils.URL)

        #Object of Loginpage
        login = LoginPage(driver)
        login.enter_username(utils.Username)
        login.enter_password(utils.Password)
        login.click_login()

    #pass the test_setup parameter so that it is taken as the pytest fixture
    # the argument "self" should be used when we have a class defined
    def test_logout(self):
        #try exception block
        try:
            #Object of HomePage
            driver = self.driver
            home = HomePage(driver)
            home.click_welcome()
            home.click_firstitem_leaveoptions()
            y = driver.title
            assert y == "OrangeHRM"
            #home.click_logout()

        except AssertionError as Asserror:
            print("Assertion error occurred")
            print(Asserror)
 #           currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testname = utils.whoami()
            AssertionScreenshot = testname + "Assertion Screenshot"#currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=AssertionScreenshot,
                          attachment_type=allure.attachment_type.PNG)
            raise

        except Exception as excerror:
            print("There was an exception")
            print(excerror)
            testname = utils.whoami()
            ExceptionScreenshot = testname + "Exception Screenshot"  # currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=ExceptionScreenshot,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Srinath/PycharmProjects/AutomationFramework_1/screenshots/" + ExceptionScreenshot + ".png")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")
        #home.click_logout()



