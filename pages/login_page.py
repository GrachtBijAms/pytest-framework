from core.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):

    #Selectors - all 
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MSG = "[data-test='error']"


    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator(self.USERNAME)
        self.password_input = page.locator(self.PASSWORD)
        self.login_button = page.locator(self.LOGIN_BUTTON)
        self.error_message = page.locator(self.ERROR_MSG)

    def login(self, username: str, password: str):
        self.logger.info(f"Attempting to log in with username: {username}")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.wait_for_page_load("networkidle")

    def navigate_to_login(self, base_url: str):  
        # navigate to base_url + "/login"
        self.navigate(base_url)

    def get_error_message(self) -> str:
        # return error message text
        return self.error_message.text_content().strip()

    def is_login_successful(self) -> bool:
        # return true if welcome text is visible
        return self.is_visible("#welcome-text")
    
    def get_page_title(self) -> str:
        # return page title
        return self.page.title()