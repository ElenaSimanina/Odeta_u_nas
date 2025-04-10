print('Увеличение количества товара в корзине')
from playwright.sync_api import sync_playwright

def run(playwright):

    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://odetounas.ru/', timeout=0)   
    page.click('//div[@class="reklama_b"]/div')
    #input()
    page.click('//span[@id="skorzina"]')
    #input()
    page.click('//div [@id="korzinah"]/div')
    #input()
    page.click("//a [text()='Каталог']")
    page.click('(//div [@id="p_obview_g641271" ])[1]')
    page.click('//select [@id="rost641271" ]')
    page.select_option('//select [@id="rost641271"]', '164')
    #input(3)
    page.click('//select [@id="razm641271"]')
    page.select_option('//select [@id="razm641271"]', '42')
    #input(3)
    page.click('//div [@id="v_razm_boot"]')
    page.click('//span [@id="skorzina"]')
    page.click('//div [@title="Прибавить."]')
    input(3)
    print (page.locator('(//span [@class="k_item_data_cs"])[2]'))
    assert page.locator('(//span [@class="k_item_data_cs"])[2]')

    input(5)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)