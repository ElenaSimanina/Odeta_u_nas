print('Успешная регистрация')
from playwright.sync_api import sync_playwright

def run(playwright):
#with sync_playwright() as p:
    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://odetounas.ru/', timeout=0)
    # input()
    page.click('//div[@class="reklama_b"]/div')
    page.click('//span [@title="Вход на сайт или зарегистрироваться."]')
    page.click('//span [text() = "Зарегистрироваться."]')
    #input()
    page.fill('//input [@id="userfamreg"]', 'Анакондов')
    page.fill('//input [@id="userimyreg"]', 'Удав')
    page.fill('//input [@id="userotchreg" ]', 'Аскаридович')
    page.fill('//input [@id="usernamereg"]', 'Anacond')
    page.fill('//input [@id="usertelefonreg"]', '+79176201184')
    page.fill('//input [@id="usermailreg"]', 'anac@mail.ru')
    page.fill('//input [@id="userpasreg"]', 'anacond84')
    page.fill('//input [@id="userpasreg1"]', 'anacond84')
    #page.click('//a [text() = "Условиями"]')
    page.click('//input [@id="subloginreg"]')
    if page.locator('//span[text() = "Подтверждение почты."]'):
        print('Регистрация  прошла успешно')
    else:
        print('NOT OK')
        page.click('//div [@id="loginpodh"]/div')
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)