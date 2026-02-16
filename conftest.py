from playwright.sync_api import sync_playwright

import pytest

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    # page.set_default_timeout(60000)
    # page.set_default_navigation_timeout(60000)
    yield page
    page.close()        