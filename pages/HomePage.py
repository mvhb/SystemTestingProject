from random import randint

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.MainPage import MainPage


class HomePage(MainPage):
    SHORT_SECONDS = 10
    URL = "http://automationpractice.com/index.php"

    css_popular_products = "#homefeatured > .ajax_block_product"
    class_add_to_cart = "ajax_add_to_cart_button"
    class_product_name = "product-name"
    class_product_price = "content_price"
    css_success_message = ".layer_cart_product > h2"
    id_product_name_modal = "layer_cart_product_title"
    id_product_price_modal = "layer_cart_product_price"
    css_proceed_to_checkout_button = "#layer_cart > div > div:nth-child(2) > div:nth-child(5) > a"
    class_sign_in = "header_user_info"
    class_more_option = "lnk_view"
    css_dresses_menu_option = ".menu-content > li:nth-child(2)"

    def __init__(self):
        super(HomePage, self).__init__()

    def open_home_page(self):
        self.driver.get(self.URL)

    def find_a_random_product(self):
        product_card = self.driver.find_elements(By.CSS_SELECTOR, self.css_popular_products)
        random_product = randint(0, len(product_card) - 1)
        product_element = product_card[random_product]
        product_name, product_price = product_card[random_product].text.split("\n")
        product_price = product_price[:6]  # Getting current price
        return product_element, product_name, product_price

    def add_product_of_the_list(self):
        product_element, product_name, product_price = self.find_a_random_product()
        ActionChains(self.driver).move_to_element(product_element).perform()
        product_element.find_element(By.CLASS_NAME, self.class_add_to_cart).click()
        return product_name, product_price

    def click_on_more_of_product(self):
        product_element, product_name, product_price = self.find_a_random_product()
        ActionChains(self.driver).move_to_element(product_element).perform()
        product_element.find_element(By.CLASS_NAME, self.class_more_option).click()
        return product_name, product_price

    def get_success_message_from_modal(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.css_success_message)))
        return self.driver.find_element(By.CSS_SELECTOR, self.css_success_message).text

    def get_product_name_from_modal(self):
        return self.driver.find_element(By.ID, self.id_product_name_modal).text

    def get_product_price_from_modal(self):
        return self.driver.find_element(By.ID, self.id_product_price_modal).text

    def click_on_proceed_to_checkout_button(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.css_proceed_to_checkout_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.css_proceed_to_checkout_button).click()

    def click_on_sign_in(self):
        self.driver.find_element(By.CLASS_NAME, self.class_sign_in).click()

    def click_on_dresses_menu_option(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_dresses_menu_option).click()
