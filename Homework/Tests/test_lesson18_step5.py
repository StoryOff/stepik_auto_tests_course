import time
import pytest
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

answer = ""


@pytest.mark.parametrize('link', links)
class TestStepik:
    def test_get_secret_message(self, browser, link):
        # login part
        browser.get(link)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#ember33'))).click()
        login_input = browser.find_element(By.CSS_SELECTOR, '#id_login_email')
        login_input.send_keys('123@mail.ru')
        password_input = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
        password_input.send_keys('123')
        browser.find_element(By.CLASS_NAME, 'button_with-loader').click()
        time.sleep(3)
        # get secret message part
        browser.find_element(By.CLASS_NAME, 'ember-text-area').send_keys(str(math.log(int(time.time()))))
        time.sleep(2)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        time.sleep(2)
        result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        if result != 'Correct!':
            answer.join(result)
        print(answer)
