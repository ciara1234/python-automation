import time as t
from datetime import datetime

from PageObjectLibrary import PageObject
from selenium.webdriver import ActionChains


class SearchResultsPage(PageObject) :
    PAGE_URL = "/index.php?controller=search"
    PAGE_TITLE = "Search - My Store"

    _locators = {
        "women" : "href=women",
        "product_list" : "class=product_list",
        "layer_cart" : "layer_cart",
        "close_window" : "cross"
    }

    def _is_current_page(self) :
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location, and raise an appropriate error if
        # we are not on the correct page
        location = self.selib.get_location()
        if not location.contains(self.PAGE_TITLE) :
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def click_add_to_cart(self, index) :
        """Clicks the quick view button on the image
        """
        products = self.driver.find_elements_by_css_selector("li[class*=ajax_block_product]")
        ActionChains(self.driver).move_to_element(products[index]).perform()
        self.driver.find_element_by_css_selector("a.ajax_add_to_cart_button").click()

    def product_is_added_to_cart(self) :
        element = self.driver.find_element_by_id(self.locator.layer_cart).text
        print(element)
        message = 'Product successfully added to your shopping cart'
        if message in element :
            return True
        else:
            raise Exception('Product not added!')

    def close_dialog(self):
        self.driver.find_element_by_class_name(self.locator.close_window).click()

    def go_to_cart(self):
        cart_element = self.driver.find_element_by_xpath(
            ".//a[contains(@title,'View my shopping cart')]")
        ActionChains(self.driver).move_to_element(cart_element).perform()
        cart_element.click()

    def proceed_to_checkout(self):
        self.driver.find_element_by_xpath("//span[normalize-space(text())='Proceed to checkout']").click()

