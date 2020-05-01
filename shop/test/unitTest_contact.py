import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class MS_Test6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_contact(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://onlineshopmusic.herokuapp.com/")
        login_button = driver.find_element_by_xpath('/html/body/nav/button/span').click()
        contact = driver.find_element_by_xpath('/html/body/nav/div/ul/li[2]/a').click()


        try:
            # create account
            cname = driver.find_element_by_id("id_name")
            cname.send_keys("sandhya")

            cmail = driver.find_element_by_id("id_from_email")
            cmail.send_keys("sandhyamishra@unomaha.edu")

            contact_subject = driver.find_element_by_id("id_subject")
            contact_subject.send_keys("about faulty product")

            contact_message = driver.find_element_by_id("id_message")
            contact_message.send_keys("This is a test message about faulty product")
            submit_button = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()

            assert True
        except NoSuchElementException:
            self.fail("unable to send message")
            assert False


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
