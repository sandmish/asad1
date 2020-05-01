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
            driver.get("https://onlineshopmusic.herokuapp.com/")
            time.sleep(1.0)
            continue_test = True
        except NoSuchElementException:
            self.fail("unable to see main page")
            assert False

        if continue_test:
            elem_button1 = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[1]/a/img').click()
            time.sleep(1.0)
        try:
            # main page
            product_page = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/h1')
            time.sleep(1.0)
            continue_test = True
        except NoSuchElementException:
            self.fail("unable to see product page")
            assert False

        if continue_test:
            add_cart = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/a/button').click()
            time.sleep(1.0)
        try:
            # main page
            product_page = driver.find_element_by_xpath('/html/body/div[1]/div')
            time.sleep(1.0)
            continue_test = True
        except NoSuchElementException:
            self.fail("unable to see product page")
            assert False


        if continue_test:
            del_item=driver.find_element_by_xpath('/html/body/div[2]/div[1]/table/tbody/tr/td[4]/a[3]/i').click()
            time.sleep(1.0)

        try:
            empty_cart = driver.find_element_by_xpath('/html/body/div/h1')
            time.sleep(1.0)
            assert True
        except NoSuchElementException:
            self.fail("unable to modify product")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
