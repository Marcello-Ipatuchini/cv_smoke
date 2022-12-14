from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    #link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"
    page = MainPage(browser)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.email_input_random()
    # выполняем метод страницы — переходим на страницу логина
