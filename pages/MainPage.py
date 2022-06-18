from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MainPage:

    class_home_icon = "home"

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            chrome_driver = ChromeService(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_driver)

    def maximize_window(self):
        self.driver.maximize_window()

    def close_page(self):
        self.driver.quit()

    def is_page_correct(self, url):
        is_url_correct = self.driver.current_url == url
        return is_url_correct

    def click_on_home_icon(self):
        self.driver.find_element(By.CLASS_NAME, self.class_home_icon).click()
