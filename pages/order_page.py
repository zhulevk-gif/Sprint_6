import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)

        metro_input = self.wait_visible(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys("Черкизовская")
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, color, comment):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)

        date_input = self.wait_visible(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(Keys.ESCAPE)
        self.wait.until(
            EC.invisibility_of_element_located(OrderPageLocators.DATE_PICKER_POPUP)
        )

        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        if color == "black":
            self.click(OrderPageLocators.RENTAL_PERIOD_ONE_DAY)
            self.click(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        else:
            self.click(OrderPageLocators.RENTAL_PERIOD_TWO_DAYS)
            self.click(OrderPageLocators.GREY_COLOR_CHECKBOX)

        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить текст успешного оформления заказа")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_MODAL)