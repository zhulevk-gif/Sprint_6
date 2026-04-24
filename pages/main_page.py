import allure

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Принять cookies")
    def accept_cookies(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step("Открыть вопрос FAQ")
    def open_question(self, question_locator):
        self.click_with_scroll(question_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_bottom_order_button(self):
        self.click_with_scroll(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Проверить, что открыта главная страница Самоката")
    def is_on_main_page(self):
        return "/order" not in self.driver.current_url

    @allure.step("Проверить, что открылась страница Дзена")
    def is_dzen_opened(self):
        return "dzen.ru" in self.driver.current_url or "ya.ru" in self.driver.current_url