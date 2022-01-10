from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    print (element)
    button = browser.find_element_by_id("book")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
    option1 = browser.find_element_by_id("input_value")
    browser.execute_script('return arguments[0].scrollIntoView(true);', option1)
    x = option1.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', input1)
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

    #message = browser.find_element_by_id("verify_message")
    #assert "successful!" in message.text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
