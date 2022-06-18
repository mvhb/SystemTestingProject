from pages.DressesPage import DressPage


class Test_6:

    def test_check_lowest_first_filter(self, open_browser, close_browser):
        home_page = open_browser
        home_page.click_on_dresses_menu_option()
        dress_page = DressPage(home_page.driver)
        dress_page.click_on_lowest_first_filter()
        dress_page.wait_loading()
        assert dress_page.get_products_value() == ["$16.40", "$26.00", "$28.98", "$30.50", "$50.99"], "Filter didnt worked"

