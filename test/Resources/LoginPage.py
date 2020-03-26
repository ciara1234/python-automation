from PageObjectLibrary import PageObject


class LoginPage(PageObject) :
    PAGE_URL = "/index.php?controller=authentication&back=my-account"
    PAGE_TITLE = "Login - My Store"

    _locators = {
        "email" : "id=email",
        "password" : "id=passwd",
        "form_id" : "login_form",
        "submit_login" : "SubmitLogin"
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

    def enter_username(self, email) :
        """Type the given text into the username field """
        self.selib.input_text(self.locator.email, email)

    def enter_password(self, password) :
        """Type the given text into the password field"""
        self.selib.input_text(self.locator.password, password)

    def click_the_login_button(self) :
        """Clicks the submit button on the form

        For illustrative purposes, this uses the low level selenium
        functions for submitting the form
        """

        form = self.driver.find_element_by_xpath("//form[@id='%s']" % self.locator.form_id)

        # since this action causes the page to be refreshed, wrap
        # this in a context manager so it does't return until the
        # new page is rendered

        btn = self.driver.find_element_by_id(self.locator.submit_login)

        with self._wait_for_page_refresh() :
            btn.click()
