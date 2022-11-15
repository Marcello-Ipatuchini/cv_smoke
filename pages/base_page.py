from webbrowser import Chrome


class BasePage():
    def __init__(self, browser, url):
        self.browser = Chrome()
        self.url = 'https://dev:cvdev321@staging.clearvin.com/en/user/login/'

    def open(self):
        self.browser.get(self.url)
