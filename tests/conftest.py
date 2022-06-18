import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.fixture()
def open_browser():
    home_page = HomePage()
    home_page.open_home_page()
    home_page.maximize_window()
    yield home_page


@pytest.fixture()
def sign_in(open_browser):
    home_page = open_browser
    home_page.click_on_sign_in()
    login_page = LoginPage(home_page.driver)
    login_page.type_in_email_field(email="hevatom389@exoacre.com")
    login_page.type_in_password_field(password="123123")
    login_page.click_on_sign_in_button()
    login_page.click_on_home_icon()
    yield login_page


@pytest.fixture()
def close_browser(open_browser):
    yield
    home_page = open_browser
    home_page.close_page()
