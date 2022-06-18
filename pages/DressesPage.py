from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.MainPage import MainPage


class DressPage(MainPage):

    SHORT_SECONDS = 10

    css_lowest_first = "#selectProductSort > option:nth-child(2)"
    css_loading = ".product_list > p"
    css_dresses_products = ".product_list > li"
    xpath_product_price = "//*[@id='center_column']/ul/li[%s]/div/div[2]/div[1]/span[1]"

    def __init__(self, driver):
        super(DressPage, self).__init__(driver=driver)

    def click_on_lowest_first_filter(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.css_lowest_first).click()

    def wait_loading(self):
        WebDriverWait(self.driver, self.SHORT_SECONDS).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.css_loading)))
        WebDriverWait(self.driver, self.SHORT_SECONDS).until_not(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.css_loading)))

    def get_products_value(self):
        dresses_card = self.driver.find_elements(By.CSS_SELECTOR, self.css_dresses_products)
        dresses_count = len(dresses_card)
        list_lowest_first = []
        for dress_position in range(dresses_count):
            dress = dresses_card[dress_position]
            dress_price = self.xpath_product_price % (dress_position + 1)
            dress_price = dress.find_element(By.XPATH, dress_price).text
            list_lowest_first.append(dress_price[:6])
        return list_lowest_first
