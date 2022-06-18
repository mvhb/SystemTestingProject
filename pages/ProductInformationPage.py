from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.MainPage import MainPage


class ProductInformationPage(MainPage):

    SHORT_SECONDS = 10

    css_product_name = ".pb-center-column > h1"
    id_product_price = "our_price_display"
    id_add_to_cart = "add_to_cart"

    def __init__(self, driver):
        super(ProductInformationPage, self).__init__(driver=driver)

    def get_product_name(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.css_product_name)))
        return self.driver.find_element(By.CSS_SELECTOR, self.css_product_name).text

    def get_product_price(self):
        return self.driver.find_element(By.ID, self.id_product_price).text

    def is_add_to_cart_button_present(self):
        try:
            self.driver.find_element(By.ID, self.id_add_to_cart)
            return True
        except NoSuchElementException:
            return False


