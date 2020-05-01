import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MS_Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://onlineshopmusic.herokuapp.com/")
        login_dropdown = driver.find_element_by_xpath('/html/body/nav/button/span').click()
        login_user = driver.find_element_by_xpath('/html/body/nav/div/ul/li[5]/a').click()
        time.sleep(3.0)
        login_email_address = driver.find_element_by_id("id_username")
        login_email_address.send_keys("sandhya")
        time.sleep(3.0)
        login_email_pwd = driver.find_element_by_id("id_password")
        login_email_pwd.send_keys("password")
        time.sleep(3.0)
        sign_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/button').click()
        try:
            # create account
            create_login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            time.sleep(3.0)
            assert True
        except NoSuchElementException:
            self.fail("Login Failed create account")
            assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
