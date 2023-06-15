from selenium.webdriver.common.by import By


def test_check_button(browser,language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    print(link)
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button, "button was not found"