from playwright.sync_api import Page
from core.logger import get_logger
from pathlib import Path



class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_page_load(self, state: str = "networkidle"):
        self.logger.info(f"Waiting for page to load with state: {state}")
        self.page.wait_for_load_state(state)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)
        self.wait_for_page_load("networkidle")

    def click(self, selector: str):
        self.logger.info(f"Clicking on element with selector: {selector}")
        # wait for element to be visible
        self.page.wait_for_selector(selector, state="visible")
        # then click it
        self.page.click(selector)

    def type_text(self, selector: str, text: str):
        self.logger.info(f"Typing text into element with selector: {selector}")
        # wait for element
        self.page.wait_for_selector(selector, state="visible")
        # clear existing text first
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.logger.info(f"Getting text from element with selector: {selector}")
        # wait for element
        self.page.wait_for_selector(selector, state="visible")
        # return its inner text
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        self.logger.info(f"Checking visibility of element with selector: {selector}")
        # return true/false if element is visible
        return self.page.is_visible(selector)
    
    def take_screenshot(self, name: str):
        path = Path("reports")/"screenshots"/f"{name}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        self.logger.info(f"Taking screenshot: {path}")
        self.page.screenshot(path=path)