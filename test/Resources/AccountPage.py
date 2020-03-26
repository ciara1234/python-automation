from PageObjectLibrary import PageObject


class AccountPage(PageObject) :
    PAGE_URL = "/index.php?controller=my-account"
    PAGE_TITLE = "My account - My Store"

    _locators = {
        "search_box": "id=search_query_top",
        "form_id": "searchbox",
        "submit_search": "submit_search"
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

    def enter_search_term(self, search):
        """Type the given text into the username field """
        self.selib.input_text(self.locator.search_box, search)

    def click_the_search_button(self) :
        """Clicks the submit button on the form

        For illustrative purposes, this uses the low level selenium
        functions for submitting the form
        """

        form = self.driver.find_element_by_xpath("//form[@id='%s']" % self.locator.form_id)

        # since this action causes the page to be refreshed, wrap
        # this in a context manager so it does't return until the
        # new page is rendered

        with self._wait_for_page_refresh() :
            form.submit()
