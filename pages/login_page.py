from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    submit = (By.ID, "submit")
    error = (By.ID, "error")

    def load(self):
        self.driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.submit).click()

    def get_error(self):
        return self.driver.find_element(*self.error).text
