
from playwright.sync_api import Page, expect

def test_valid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    expect(page.get_by_placeholder("Password")).to_have_attribute("type", "password")

    page.get_by_role("button", name="WrongLogin").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_invalid_login(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("invalid_user")
    page.get_by_placeholder("Password").fill("invalid_password")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Username and password do not match")).to_be_visible()


def test_username_required(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Username is required")).to_be_visible()


def test_password_required(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Password is required")).to_be_visible()