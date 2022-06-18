from pages.CartPage import CartPage


class Test_2:

    def test_complete_an_order(self, open_browser, sign_in, close_browser):
        home_page = open_browser
        product_name, product_price = home_page.add_product_of_the_list()
        home_page.click_on_proceed_to_checkout_button()
        cart_page = CartPage(home_page.driver)
        assert cart_page.is_cart_page_displayed()
        assert cart_page.get_product_name_on_cart() == product_name, "Product name didnt match"
        assert cart_page.get_product_quantity() == "1 Product", "Product quantity didnt match"
        assert cart_page.get_total_price() == product_price, "Product price didnt match"
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_page_header() == "ADDRESSES"
        assert cart_page.get_delivery_address_label() == "YOUR DELIVERY ADDRESS"
        assert cart_page.get_billing_address_label() == "YOUR BILLING ADDRESS"
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_page_header() == "SHIPPING"
        cart_page.mark_terms_of_service()
        cart_page.click_on_proceed_to_checkout()
        assert cart_page.get_page_header() == "PLEASE CHOOSE YOUR PAYMENT METHOD"
        cart_page.click_on_bank_wire()
        assert cart_page.get_page_header() == "ORDER SUMMARY"
        cart_page.click_on_confirm_my_order()
        assert cart_page.get_page_header() == "ORDER CONFIRMATION"






