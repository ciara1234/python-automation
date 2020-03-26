from PageObjectLibrary import PageObject
from selenium.webdriver import ActionChains


class PaymentPage(PageObject) :
    PAGE_URL = "/index.php?controller=order&multi-shipping="
    PAGE_TITLE = "My account - My Store"

    _locators = {
        "bank_wire" : "bankwire"
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

    def pay_by_bank_wire(self) :
        payment_method = self.driver.find_element_by_class_name(self.locator.bank_wire)
        ActionChains(self.driver).move_to_element(payment_method).perform()
        payment_method.click()
