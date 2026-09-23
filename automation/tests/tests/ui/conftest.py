from playwright.sync_api import Page
from collections.abc import Generator
from pytest import fixture

@fixture
def page(browser) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page

    context.close()