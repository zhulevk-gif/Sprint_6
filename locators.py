from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    ORDER_BUTTON_TOP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    FAQ_QUESTION_0 = (By.ID, "accordion__heading-0")
    FAQ_QUESTION_1 = (By.ID, "accordion__heading-1")
    FAQ_QUESTION_2 = (By.ID, "accordion__heading-2")
    FAQ_QUESTION_3 = (By.ID, "accordion__heading-3")
    FAQ_QUESTION_4 = (By.ID, "accordion__heading-4")
    FAQ_QUESTION_5 = (By.ID, "accordion__heading-5")
    FAQ_QUESTION_6 = (By.ID, "accordion__heading-6")
    FAQ_QUESTION_7 = (By.ID, "accordion__heading-7")

    FAQ_ANSWER_0 = (By.ID, "accordion__panel-0")
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-1")
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-2")
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-3")
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-4")
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-5")
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-6")
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-7")


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_POPUP = (By.CLASS_NAME, "react-datepicker")

    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_PERIOD_ONE_DAY = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and normalize-space()='сутки']"
    )
    RENTAL_PERIOD_TWO_DAYS = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and normalize-space()='двое суток']"
    )

    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")