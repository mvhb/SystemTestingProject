from pages.CartPage import CartPage


class Test_3:

    def test_is_not_possible_to_complete_order_without_terms_of_service(self, open_browser, sign_in, close_browser):
        home_page = open_browser
        product_name, product_price = home_page.add_product_of_the_list()
        home_page.click_on_proceed_to_checkout_button()
        cart_page = CartPage(home_page.driver)
        assert cart_page.is_cart_page_displayed()
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_page_header() == "ADDRESSES"
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_page_header() == "SHIPPING"
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_error_message() == "you must agree to the terms of service before continuing."
