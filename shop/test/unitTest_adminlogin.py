import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MS_Test7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_adminaddpro(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://onlineshopmusic.herokuapp.com/admin/login/?next=/admin/")
        login_email = driver.find_element_by_id("id_username")
        login_email.send_keys("instructor")
        login_email_pwd = driver.find_element_by_id("id_password")
        login_email_pwd.send_keys("maverick1a")
        login = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click()

        try:
            # create account
            create_login = driver.find_element_by_xpath('/html/body/div/div[2]/h1')
            assert True
        except NoSuchElementException:
            self.fail("fail to login to admin page")
            assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
