# tests/test_login.py
import pytest
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage

@pytest.mark.parametrize("username,password,should_pass", [
    ("admin", "admin123", True),
    ("wrong", "wrongpass", False),
])
def test_login_flow(driver, username, password, should_pass):
    base = "http://localhost:8000"
    login = LoginPage(driver, base)
    login.load()
    # Data-driven: inject test data directly
    login.login(username, password)

    if should_pass:
        dash = DashboardPage(driver, base)
        assert dash.is_loaded(), "Dashboard should be visible for valid credentials"
        dash.click_action()
    else:
        assert "Invalid credentials" in login.get_error_text(), "Should show invalid message"
