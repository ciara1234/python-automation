from PageObjectLibrary import PageObject
from selenium.webdriver import ActionChains


class OrderPage(PageObject) :
    PAGE_URL = "/index.php?controller=order"
    PAGE_TITLE = "Order - My Store"

    _locators = {
    }

    def _is_current_page(self) :
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location, and raise an appropriate error if
        # we are not on the correct page
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL) :
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def increase_quantity(self) :
        self.driver.find_element_by_xpath(
            ".//a[contains(@class, 'cart_quantity_up') and contains(@title, 'Add')]").click()

    def go_to_cart_from_order_page(self) :
        self.driver.find_element_by_xpath(
            ".//a[contains(@title, 'View my shopping cart')]").click()

    def order_page_proceed_to_checkout(self) :
        self.driver.find_element_by_xpath("//a[@href='http://automationpractice.com/index.php"
                                          "?controller=order&step=1']").click()
