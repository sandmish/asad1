import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MS_Test3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_contshop(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://onlineshopmusic.herokuapp.com/")
        login_dropdown = driver.find_element_by_xpath('/html/body/nav/button/span').click()
        login_user = driver.find_element_by_xpath('/html/body/nav/div/ul/li[5]/a').click()
        time.sleep(1.0)
        login_email_address = driver.find_element_by_id("id_username")
        login_email_address.send_keys("sandhya")
        time.sleep(1.0)
        login_email_pwd = driver.find_element_by_id("id_password")
        login_email_pwd.send_keys("password")

        sign_button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/button').click()

        try:
            # main page
            elem_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/h1')
            time.sleep(1.0)
            continue_test = True
        except NoSuchElementException:
            self.fail("unable to see main page")
            assert False

        if continue_test:
            elem_button1 = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[1]/a/img').click()

        try:
            # main page
            product_page = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/p[1]')

            continue_test = True
        except NoSuchElementException:
            self.fail("unable to see product page")
            assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
