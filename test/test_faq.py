import pytest
import allure

from pages.main_page import MainPage
from data import FAQ_DATA


class TestFAQ:

    @allure.title("Проверка ответов в FAQ")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", FAQ_DATA)
    def test_faq_answers(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)

        main_page.accept_cookies()
        main_page.open_question(question_locator)

        assert main_page.get_answer_text(answer_locator) == expected_text