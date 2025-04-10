print('Просмотр товара')
from playwright.sync_api import sync_playwright

def run(playwright):
#with sync_playwright() as p:
    
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://odetounas.ru/', timeout=0)   
    page.click('//div[@class="reklama_b"]/div')
    #input()
    page.click("//a [text()='Каталог']")
    page.click('(//div [@id="p_obview_g641271" ])[1]')
    #input()
    if page.locator('//img [@id="641271_0"]'):
        print('OK')
    else:
        print('product viewing error')
        #page.click('//div [@id="loginpodh"]/div')
    input()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)