from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    #confirm = browser.switch_to.alert
    #confirm.accept()
    new_window = browser.window_handles[1]

    print (new_window)
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    #[id = 'input_value']
    print (x)

    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_class_name("btn.btn-primary")

    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла