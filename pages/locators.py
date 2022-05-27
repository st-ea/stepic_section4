from selenium.webdriver.common.by import By


class MainPageLocators():
    link = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocatore():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    lg_username = (By.CSS_SELECTOR, "#id_login-username")
    lg_password = (By.CSS_SELECTOR, "#id_login-password")
    lg_submit = (By.CSS_SELECTOR, ".login_submit")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    #BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")


class BasketPageLocators:
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    LBL_GOODS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6")
    LBL_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")