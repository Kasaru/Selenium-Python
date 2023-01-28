from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def calc(a,b,c):
    if b in '+и':
        return int(a)+int(c)
    elif b == '-':
        return int(a)-int(c)
    elif b == '*':
        return int(a)*int(c)
    else:
        return int(a)/int(c)

try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, ".nowrap:nth-child(3)")
    b = b_element.text
    c_element = browser.find_element(By.ID, "num2")
    c = c_element.text
    y = calc(a,b,c)
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(str(y))
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()