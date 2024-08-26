import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import pytest
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"
alert_text = "=="


# Делаю тест через xfail с намеренной ошибкой (правильно было бы assert alert_text != None),
# чтобы получить вывод текста text_alert (просто распечатать не получается
@pytest.mark.xfail
class TestBooking:
    def calc(self, x):
        return str(math.log(abs(12 * math.sin(x))))

    def test_booking(self, browser):
        browser.get(link)

        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(
            (By.ID, 'price'),text_= '100'))
        browser.find_element(By.ID, 'book').click()

        x_element = browser.find_element(By.CSS_SELECTOR, "label > span:nth-child(2)")
        y = self.calc(int(x_element.text))

        browser.find_element(By.ID, "answer").send_keys(y)

        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve"))).click()

        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.accept()

        assert alert_text == None, f"The test is flaky. If any exception occur, try the test again"
        time.sleep(2)


# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))

