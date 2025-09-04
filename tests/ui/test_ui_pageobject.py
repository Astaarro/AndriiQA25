from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_usermane_page_object():
    # Стрворення обєкту сторніки
    sign_in_page = SignInPage()
    # Відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # Виконуємо спробу увійти в GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    # Перевіряємо чи назва стоірнки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Зариваємо браузер
    sign_in_page.close()