from pages.login_page import LoginPage
from utils.driver_factory import create_driver

def test_invalid_login_shows_error():
    driver = create_driver()
    login = LoginPage(driver)

    try:
        login.load()
        login.login("wrongUser", "wrongPass")

        error = login.get_error()
        assert "invalid" in error.lower()
    finally:
        driver.quit()
