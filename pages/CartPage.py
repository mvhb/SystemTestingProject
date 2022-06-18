from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.MainPage import MainPage


class CartPage(MainPage):
    SHORT_SECONDS = 10
    URL = "http://automationpractice.com/index.php?controller=order"

    css_product_name = ".cart_description > .product-name"
    id_product_quantity = "summary_products_quantity"
    css_product_total_price = ".cart_total > span"
    css_proceed_to_checkout = ".cart_navigation > .button-medium"
    css_delivery_address_label = "#address_delivery > .address_title"
    css_billing_address_label = "#address_invoice > .address_title"
    class_page_heading = "page-heading"
    id_terms_of_service = "cgv"
    class_bank_wire = "bankwire"
    css_confirmation_price = ".box > .price"
    class_error_message = "fancybox-error"
    class_trash_icon = "icon-trash"
    class_warning_alert = "alert-warning"

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def get_product_name_on_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_product_name).text

    def get_product_quantity(self):
        return self.driver.find_element(By.ID, self.id_product_quantity).text

    def is_cart_page_displayed(self):
        return super().is_page_correct(self.URL)

    def get_total_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_product_total_price).text

    def click_on_proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_proceed_to_checkout).click()

    def get_delivery_address_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_delivery_address_label).text.upper()

    def get_billing_address_label(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_billing_address_label).text.upper()

    def get_page_header(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_page_heading).text.upper()

    def mark_terms_of_service(self):
        self.driver.find_element(By.ID, self.id_terms_of_service).click()

    def click_on_bank_wire(self):
        self.driver.find_element(By.CLASS_NAME, self.class_bank_wire).click()

    def click_on_confirm_my_order(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_proceed_to_checkout).click()

    def get_confirmation_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_confirmation_price).text

    def get_error_message(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.class_error_message)))
        return self.driver.find_element(By.CLASS_NAME, self.class_error_message).text.lower()

    def click_on_trash_icon(self):
        self.driver.find_element(By.CLASS_NAME, self.class_trash_icon).click()

    def get_warning_message(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.class_warning_alert)))
        return self.driver.find_element(By.CLASS_NAME, self.class_warning_alert).text

