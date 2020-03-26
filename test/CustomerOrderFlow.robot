*** Variables ***
${BROWSER} =  chrome
${START_URL} =  http://automationpractice.com
${VALID_EMAIL} =  ciara.brennan@gmail.com
${VALID_PASSWORD} =  Password123!
${SEARCH_TERM} =  PRINTED SUMMER DRESS


*** Keywords ***
Failed Case Handle  capture page Screenshot

*** Settings ***
Library    SeleniumLibrary
Library    PageObjectLibrary
Library   ${CURDIR}/Resources/LoginPage.py
Library   ${CURDIR}/Resources/AccountPage.py
Library   ${CURDIR}/Resources/SearchResultsPage.py
Library   ${CURDIR}/Resources/OrderPage.py
Library   ${CURDIR}/Resources/AddressesOrderPage.py
Library   ${CURDIR}/Resources/PaymentPage.py
Library   ${CURDIR}/Resources/ShippingPage.py
Library   ${CURDIR}/Resources/OrderSummaryPage.py
Library   ${CURDIR}/Resources/OrderConfirmationPage.py

Suite Setup  Open browser  ${START_URL}  ${BROWSER}
Suite Teardown  Close all browsers

Test Teardown  run keyword if test failed  Failed Case Handle


*** Test Cases ***

Valid Login
    [Documentation]  Verify that a user can successfully log in to the store
    [Setup]  Go to page  LoginPage
    Enter username  ${VALID_EMAIL}
    Enter password  ${VALID_PASSWORD}
    Click the login button
    sleep  5s
    The current page should be  AccountPage


Logged in user can place an order
    [Documentation]  Verify that a logged in user can search for a product, add to cart and checkout
    [Setup]  Go to page  AccountPage
    Enter search term  ${SEARCH_TERM}
    Click the search button
    Click Add To Cart  ${0}
    sleep  3s
    Product Is Added To Cart
    Proceed To Checkout
    The current page should be  OrderPage
    sleep  3s
    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight)
    Order Page Proceed To Checkout
    sleep  3s
    The current page should be  AddressesOrderPage
    Select Delivery Address
    Addresses Page Proceed To Checkout
    Agree To Terms of Service
    Shipping Page Proceed To Checkout
    Pay By Bank Wire
    Confirm Order
    Order is Confirmed








