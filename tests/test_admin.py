from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.config import Config


def test_search_user(page):
    login_page = LoginPage(page)
    admin_page = AdminPage(page)

    login_page.login(Config.USERNAME, Config.PASSWORD)
    page.wait_for_url("**/dashboard/**")

    admin_page.search_user("Admin")
    page.wait_for_timeout(2000)

    assert "Admin" in admin_page.get_search_result().text_content()