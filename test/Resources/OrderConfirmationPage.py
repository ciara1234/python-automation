import time as t
from datetime import datetime

from PageObjectLibrary import PageObject
from selenium.webdriver import ActionChains


class OrderConfirmationPage(PageObject) :
    PAGE_URL = "/index.php?controller=order-confirmation"
    PAGE_TITLE = "Order Confirmation - My Store"

    _locators = {

    }

    def _is_current_page(self) :
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location, and raise an appropriate error if
        # we are not on the correct page
        location = self.selib.get_title()
        if not location.contains(self.PAGE_TITLE) :
            message = "Expected location to have " + \
                      self.PAGE_TITLE + " but it did not"
            raise Exception(message)
        return True


    def order_is_confirmed(self) :
        element = self.driver.find_element_by_xpath("//p[@class=\"cheque-indent\"]").text
        print(element)
        message = 'Your order on My Store is complete.'
        if message in element :
            return True
        else:
            raise Exception('Product not added!')

