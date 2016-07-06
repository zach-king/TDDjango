import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe"


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She is invited to enter a to-do right away
        # She types "Buy shrubbery" into a text box
        inputbox.send_keys('Buy shrubbery')

        # When she hits enter, the page updates, and now the page
        # lists "1: Buy shrubbery" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '1: Buy shrubbery',
            [row.text for row in rows]
        )

        # There is still a text box inviting her to add another item. She
        # enters "Praise the shrubbery"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Praise the shrubbery')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now both items are on the list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy shrubbery', [row.text for row in rows])
        self.assertIn(
            '2: Praise the shrubbery',
            [row.text for row in rows]
        )

        # Edith wonders whether the site will remember her list. Then she
        # sees that the site has generated a unique URL for her -- there is
        # some explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do is still There
        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()
