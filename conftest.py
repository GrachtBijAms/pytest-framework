import pytest
from playwright.sync_api import sync_playwright
from config.config_loader import get_config
from core.logger import get_logger
from pathlib import Path

logger = get_logger(__name__)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

#config fixture to load config once per session and provide it to tests
@pytest.fixture(scope="session")
def config():
    return get_config()

#browser fixture to launch and close browser for each test function
@pytest.fixture(scope="function")
def browser(config):
    with sync_playwright() as p:
        browser = getattr(p, config.browser).launch(headless=config.headless,slow_mo=config.slow_mo)
        logger.info(f"Launching {config.browser} browser with headless={config.headless}")
        yield browser
        browser.close()
        logger.info(f"Closed {config.browser} browser")

#page fixture to create a new page for each test function
@pytest.fixture(scope="function")
def page(browser, config):
    context = browser.new_context(viewport={"width": 1280, "height": 720}, ignore_https_errors=True)
    page = context.new_page()
    page.set_default_timeout(config.timeout)
    logger.info(f"Created new page for {config.browser} browser")
    yield page
    page.close()
    logger.info(f"Closed page for {config.browser} browser")
    context.close()
    logger.info(f"Closed context for {config.browser} browser")


#screenshot fixture to take screenshot on test failure
@pytest.fixture(scope="function",autouse=True)
def screenshot_on_failure(request, page, config):
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed and config.screenshot_on_failure:
        test_name = request.node.name
        path = Path("reports")/"screenshots"/f"{test_name}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=path)
        logger.info(f"Test failed. Screenshot saved to {path}")