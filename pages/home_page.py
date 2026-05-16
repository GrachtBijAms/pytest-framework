from core.base_page import BasePage
from playwright.sync_api import Page


class HomePage(BasePage):
    #Selectors - all 
    WELCOME_TEXT = "#welcome-text"
    LOGOUT_BUTTON = "#logout-button"

    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_text = page.locator(self.WELCOME_TEXT)
        self.logout_button = page.locator(self.LOGOUT_BUTTON)

    def is_welcome_text_visible(self) -> bool:
        return self.welcome_text.is_visible()

    def logout(self):
        self.logger.info("Attempting to log out")
        self.logout_button.click()
        self.wait_for_page_load("networkidle")

    def get_page_title(self) -> str:
        return self.page.title()