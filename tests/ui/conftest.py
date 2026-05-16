import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture
def login_page(page, config):
    # create LoginPage
    login_page = LoginPage(page)
    # navigate to login
    login_page.navigate_to_login(config.base_url)
    # return it
    return login_page

@pytest.fixture  
def home_page(page):
    # create HomePage
    home_page = HomePage(page)
    # return it
    return home_page