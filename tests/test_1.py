from pages.CartPage import CartPage


class Test_1:

    def test_add_product_to_cart(self, open_browser, close_browser):
        home_page = open_browser
        product_name, product_price = home_page.add_product_of_the_list()
        assert home_page.get_success_message_from_modal() == "Product successfully added to your shopping cart", "Success message assertion error"
        assert home_page.get_product_name_from_modal() == product_name, "Product name didnt match"
        assert home_page.get_product_price_from_modal() == product_price, "Product price didnt match"
        home_page.click_on_proceed_to_checkout_button()
        cart_page = CartPage(home_page.driver)
        assert cart_page.is_cart_page_displayed()
        assert cart_page.get_product_name_on_cart() == product_name, "Product name didnt match"
        assert cart_page.get_product_quantity() == "1 Product", "Product quantity didnt match"


