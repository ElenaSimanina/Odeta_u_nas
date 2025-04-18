
def authorization(page):
    username = 'aj348'
    userpas = '12344321'

    page.click('//div[@class="reklama_b"]/div')
    page.click('//span [@title="Вход на сайт или зарегистрироваться."]')
    page.fill('//input [@id="username"]', username)
    page.fill('//input [@id="userpas"]', userpas)
    page.click('//input [@id="sublogin"]')
    if page.text_content('//span [@id="svhod"]') == 'aj348':
        print('Авторизация для aj348 прошла успешно')
    else:
        print('NOT OK')
        exit()
    return()
