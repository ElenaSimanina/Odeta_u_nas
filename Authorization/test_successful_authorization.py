from src.Test_odetounas.Odeta_u_nas.Fixture.fxture_authorization import authorization


from playwright.sync_api import sync_playwright

def run(playwright):    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    # Здесь вставляешь свой код
    # Переход по URL
    page.goto('https://odetounas.ru/', timeout=0)
    authorization(page)
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)