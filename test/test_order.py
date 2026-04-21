import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ORDER_DATA


class TestOrder:

    @allure.title("Заказ самоката через верхнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, phone, date, color, comment", [ORDER_DATA[0]])
    def test_order_by_top_button(self, driver, name, surname, address, phone, date, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, color, comment)

        assert "Заказ оформлен" in order_page.get_success_text()

    @allure.title("Заказ самоката через нижнюю кнопку")
    @pytest.mark.parametrize("name, surname, address, phone, date, color, comment", [ORDER_DATA[1]])
    def test_order_by_bottom_button(self, driver, name, surname, address, phone, date, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(date, color, comment)

        assert "Заказ оформлен" in order_page.get_success_text()

    @allure.title("Переход по логотипу Самоката")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.accept_cookies()
        main_page.click_top_order_button()
        main_page.click_scooter_logo()

        assert "/order" not in driver.current_url

    @allure.title("Переход по логотипу Яндекса")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)

        main_page.accept_cookies()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()

        assert "dzen" in driver.current_url or "ya.ru" in driver.current_url