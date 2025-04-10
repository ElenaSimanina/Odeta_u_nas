print('Авторизация при некорректном количестве символов в пароле')
from playwright.sync_api import sync_playwright

def run(playwright):
#with sync_playwright() as p:
    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://odetounas.ru/', timeout=0)
    # input()
    page.click('//div[@class="reklama_b"]/div')
    page.click('//span [@title="Вход на сайт или зарегистрироваться."]')
    # заполнение текстового поля логин
    page.fill('//input [@id="username"]', 'aj348')
    # заполнение текстового поля пароль
    page.fill('//input [@id="userpas"]', '12344321')
    page.click('//input [@id="sublogin"]')
    # проверка отображения элемента на странице
    if page.locator("//span [@id='viv_pass']/* [text() = 'Не менее 8 символов.']").is_visible():
        print('Авторизация не удалась. Пароль должен быть не менее 8  символов')
    else:
        print('Авторизация ' + page.text_content('//span [@id="svhod"]') + ' прошла успешно')
    input()
    print(page.text_content('//span [@id="svhod"]'))
    # input()
    # получение текстового содержания элемента
    if page.text_content('//span [@id="svhod"]') != 'aj348':
        print('Неправильный логин')
    else:
        print('Авторизация прошла успешно')
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)