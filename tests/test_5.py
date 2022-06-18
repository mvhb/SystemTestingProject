from pages.ProductInformationPage import ProductInformationPage


class Test_5:

    def test_verify_info_product_page(self, open_browser, close_browser):
        home_page = open_browser
        product_name, product_price = home_page.click_on_more_of_product()
        product_information_page = ProductInformationPage(home_page.driver)
        assert product_information_page.get_product_name() == product_name, "Product name didnt match"
        assert product_information_page.get_product_price() == product_price, "Product price didnt match"
        assert product_information_page.is_add_to_cart_button_present()
