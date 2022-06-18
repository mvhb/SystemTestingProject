from pages.CartPage import CartPage


class Test_4:

    def test_remove_product_from_cart(self, open_browser, close_browser):
        home_page = open_browser
        product_name, product_price = home_page.add_product_of_the_list()
        home_page.click_on_proceed_to_checkout_button()
        cart_page = CartPage(home_page.driver)
        assert cart_page.is_cart_page_displayed()
        assert cart_page.get_product_quantity() == "1 Product", "Product quantity didnt match"
        cart_page.click_on_trash_icon()
        assert cart_page.get_warning_message() == "Your shopping cart is empty."