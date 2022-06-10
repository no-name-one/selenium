import time
from selenium.webdriver.common.by import By

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/simple_form_find_task.html")

# Метод find_element_by_css_selector позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
first = driver.find_element_by_css_selector(".form-control")
# textarea = driver.find_element_by_id('ember537')
# Напишем текст ответа в найденное поле
first.clear()
first.send_keys("no")

last = driver.find_element(By.NAME, "last_name")
last.clear()
last.send_keys("name")

city = driver.find_element(By.CSS_SELECTOR, ".city")
city.clear()
city.send_keys("clever")

country = driver.find_element(By.ID, 'country')
country.clear()
country.send_keys("Kingdom Clever")
# Найдем кнопку, которая отправляет введенное решение
submit = driver.find_element(By.ID,"submit_button")

driver.save_screenshot('t.png')
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit.click()
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()
