print('Авторизауия при неправильном логине и правильном пароле')
from playwright.sync_api import sync_playwright

def run(playwright):
#with sync_playwright() as p:
    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    # Здесь вставляешь свой код
    # Переход по URL
    page.goto('https://odetounas.ru/', timeout=0)
    # input()
    # element = page.locator(".//a [text()='Виды тестирования']")
    # page.click("//html/body/div[3]/div[2]/span[1]")
    page.click('//div[@class="reklama_b"]/div')
    page.click('//span [@title="Вход на сайт или зарегистрироваться."]')
    page.fill('//input [@id="username"]', 'uuuuuuuu')
    page.fill('//input [@id="userpas"]', '12344321')
    page.click('//input [@id="sublogin"]')
    if page.locator('//input [@id="sublogin"]').is_visible():
        print('Авторизация не удалась')
    else:
        print('Авторизация ' + page.text_content('//span [@id="svhod"]') + ' прошла успешно')
    input()
    print(page.text_content('//span [@id="svhod"]'))
    # input()
    if page.text_content('//span [@id="svhod"]') != 'aj348':
        print('Неправильный логин')
    else:
        print('Авторизация прошла успешно')
    # page.click("//a [text()='Собеседование']")
    # page.click(element)
    # пеезагрузка страницы
    # page.reload()
    # назад по истории
    # page.go_back()
    # вперед по истории
    # page.go_forward()
    # Кликнуть элемент
    # page.click('Войти')
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)