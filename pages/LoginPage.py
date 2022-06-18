from selenium.webdriver.common.by import By

from pages.MainPage import MainPage


class LoginPage(MainPage):

    URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    id_email_input = "email"
    id_password_input = "passwd"
    id_sign_in_button = "SubmitLogin"

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver=driver)

    def open_login_page(self):
        self.driver.get(self.URL)

    def type_in_email_field(self, email="hevatom389@exoacre.com"):
        email_field = self.driver.find_element(By.ID, self.id_email_input)
        email_field.send_keys(email)

    def type_in_password_field(self, password="123123"):
        password_field = self.driver.find_element(By.ID, self.id_password_input)
        password_field.send_keys(password)

    def click_on_sign_in_button(self):
        self.driver.find_element(By.ID, self.id_sign_in_button).click()

