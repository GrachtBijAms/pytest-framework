import allure
import pytest


@allure.feature("Login Functionality")
@allure.title("Test Valid Login")
def test_valid_login(login_page, home_page):
    # Given valid credentials
    username = "standard_user"
    password = "secret_sauce"

    # When I log in with valid credentials
    with allure.step("Navigate to login page and perform login"):
        assert login_page.get_page_title() == "Swag Labs", "Expected page title not found"
    with allure.step("Fill in login credentials and click login button"):
        login_page.login(username, password)

    # Then I should see the welcome text on the home page
    assert home_page.get_page_title() == "Swag Labs", "Expected page title not found"

@allure.feature("Login Functionality")
@allure.title("Test Invalid Login")
def test_invalid_login(login_page):
    # Given invalid credentials
    username = "invalid_user"
    password = "invalid_password"

    # When I log in with invalid credentials
    with allure.step("Navigate to login page and attempt login with invalid credentials"):
        assert login_page.get_page_title() == "Swag Labs", "Expected page title not found"
    login_page.login(username, password)

    # Then I should see an error message
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", "Expected error message not found"