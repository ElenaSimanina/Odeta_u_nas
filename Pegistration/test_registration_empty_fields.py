print('Регистрация с незаполненными полями')
from playwright.sync_api import sync_playwright
def run(playwright):
#with sync_playwright() as p:
    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://odetounas.ru/', timeout=0)    
    page.click('//div[@class="reklama_b"]/div')
    page.click('//span [@title="Вход на сайт или зарегистрироваться."]')
    page.click('//span [text() = "Зарегистрироваться."]')    
    page.fill('//input [@id="userfamreg"]', '')
    page.fill('//input [@id="userimyreg"]', '')
    page.fill('//input [@id="userotchreg" ]', '')
    page.fill('//input [@id="usernamereg"]', '')
    page.fill('//input [@id="usertelefonreg"]', '')
    page.fill('//input [@id="usermailreg"]', '')
    page.fill('//input [@id="userpasreg"]', '')
    page.fill('//input [@id="userpasreg1"]', '')    
    page.click('//input [@id="subloginreg"]')
    #input()
    if page.locator('//div [@id="login" ]'):
        print('Ошибка')
    else:
        print('OK')
        page.click('//div [@id="loginpodh"]/div')
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)