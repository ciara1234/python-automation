from PageObjectLibrary import PageObject


class ShippingPage(PageObject) :
    PAGE_URL = "/index.php?controller=order"
    PAGE_TITLE = "My account - My Store"

    _locators = {
        "check_box": "cgv",
        "process_carrier": "processCarrier"
    }

    def _is_current_page(self) :
        # this site uses the same title for many pages,
        # so we can't rely on the default implementation
        # of this function. Instead, we'll check the page
        # location:
        self._wait_for_page_refresh()
        location = self.selib.get_location()
        if not location.endswith(self.PAGE_URL) :
            message = "Expected location to end with " + \
                      self.PAGE_URL + " but it did not"
            raise Exception(message)
        return True

    def agree_to_terms_of_service(self) :
        checkbox = self.driver.find_element_by_name(self.locator.check_box)
        checkbox.click()

    def shipping_page_proceed_to_checkout(self) :
            btn = self.driver.find_element_by_name(self.locator.process_carrier)
            with self._wait_for_page_refresh() :
                btn.click()

