from PageObjectLibrary import PageObject
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

class AddressesOrderPage(PageObject) :
    PAGE_URL = "/index.php?controller=order&step=1"
    PAGE_TITLE = "Order - My Store"

    _locators = {
        "process_address" : "processAddress",
        "address_select" : "id_address_delivery"
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

    def select_delivery_address(self) :
        select = Select(self.driver.find_element_by_id(self.locator.address_select))
        select.select_by_visible_text('OFFICE')

    def addresses_page_proceed_to_checkout(self) :
        btn = self.driver.find_element_by_name(self.locator.process_address)
        with self._wait_for_page_refresh() :
            btn.click()
