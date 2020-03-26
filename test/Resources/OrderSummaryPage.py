from PageObjectLibrary import PageObject


class OrderSummaryPage(PageObject):
    PAGE_URL = "/index.php?controller=order"
    PAGE_TITLE = "My account - My Store"

    _locators = {
        "comfirm_button": "button"
    }

    def _is_current_page(self):
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location:
        self._wait_for_page_refresh()
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL):
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def confirm_order(self):
        button = self.driver.find_element_by_xpath("//*[@id=\"cart_navigation\"]/button")
        button.click()
