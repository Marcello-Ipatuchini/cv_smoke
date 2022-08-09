from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #жмем кнопку
    bttn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    bttn.click()
    #переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

# Ваш код, который решает пример
    number = browser.find_element(By.ID, 'input_value')
    x = int(number.text)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    # Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, 'answer')
    answer_input.send_keys(y)



    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)

    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()