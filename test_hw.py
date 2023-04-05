from datetime import time


def test_dark_theme():
    """
    Протестируйте правильность переключения темной темы на сайте
    """
    current_time = time(hour=23)
    is_dark_theme = None
    if time(6) <= current_time >= time(22):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True

    current_time = time(hour=20)
    is_dark_theme = None
    dark_theme_enabled = True
    if dark_theme_enabled:
        is_dark_theme = True
    elif time(6) <= current_time >= time(22):
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suiable_user = [user for user in users if user["name"] == "Olga"][0]
    assert suiable_user == {"name": "Olga", "age": 45}

    suiable_users = [user for user in users if user["age"] < 20]
    assert suiable_users == [{"name": "Stanislav", "age": 15}, {"name": "Maria", "age": 18}]


def refactor_name_function(func_name, *args):
    a = f'{func_name.__name__.replace("_", " ").title()} [{", ".join(args)}]'
    print(a)
    return a


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = refactor_name_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = refactor_name_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = refactor_name_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

