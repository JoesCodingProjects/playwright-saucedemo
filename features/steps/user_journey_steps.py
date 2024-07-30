from behave import given, when, then
from playwright.sync_api import sync_playwright

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    # Start Playwright and launch the browser in non-headless mode
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)  # Set headless=False
    context.page = context.browser.new_page()
    context.page.goto("https://www.saucedemo.com")

@when('the user logs in with valid credentials')
def step_when_user_logs_in_with_valid_credentials(context):
    context.page.fill('#user-name', 'standard_user')
    context.page.fill('#password', 'secret_sauce')
    context.page.click('#login-button')

@when('the user logs in with invalid credentials')
def step_when_user_logs_in_with_invalid_credentials(context):
    context.page.fill('#user-name', 'fakeUsername')
    context.page.fill('#password', 'incorrectPassword')
    context.page.click('#login-button')
    context.page.wait_for_selector('[data-test="error"]')  # Wait for the error message to appear

@when('the user adds an item to the cart')
def step_when_user_adds_item_to_cart(context):
    context.page.click('.inventory_item:nth-child(1) .btn_primary')
    context.page.click('.shopping_cart_link')

@when('the user proceeds to checkout')
def step_when_user_proceeds_to_checkout(context):
    context.page.click('.checkout_button')
    context.page.fill('#first-name', 'Joe')
    context.page.fill('#last-name', 'McCay')
    context.page.fill('#postal-code', 'BT829EQ')
    context.page.click('#continue')
    context.page.click('#finish')

@then('the purchase should be successful')
def step_then_purchase_successful(context):
    assert context.page.locator('.complete-header').inner_text() == "Thank you for your order!"
    context.page.close()
    context.browser.close()
    context.playwright.stop()  # Stop Playwright when done

@then('an error message should be displayed')
def step_then_error_message_displayed(context):
    error_message = context.page.query_selector('[data-test="error"]')
    assert error_message is not None
    assert "Username and password do not match any user in this service" in error_message.text_content()
    context.page.close()
    context.browser.close()
    context.playwright.stop()  # Stop Playwright when done
