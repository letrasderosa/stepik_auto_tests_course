# stepik_auto_tests_corse

Learning auto testing with Python, using Selenium and Pytest.<br>
*<https://stepik.org/course/575/syllabus>* 

Starting to work with Git via Git Bash and via PyCharm. <br>
The repository contains some homeworks for the course.  

+ ***( ! )*** -- You might need to create ***venv*** or install some additional libraries listed in ***requirements.txt***  

### homework_1_booking_house.py
*<u>Задание:</u> ждем нужный текст на странице*


Написать программу, которая будет бронировать нам дом для отдыха по строго заданной
цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет
забронировать кто-то другой.

Написать программу, которая будет выполнять следующий сценарий:

- Открыть страницу *<http://suninjuly.github.io/explicit_wait2.html>*
- Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не
меньше 12 секунд)
- Нажать на кнопку "Book"
- Решить уже известную нам математическую задачу и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте
метод ***text_to_be_present_in_element*** из библиотеки ***expected_conditions***.

Если все сделано правильно и быстро, то вы увидите окно с числом.
