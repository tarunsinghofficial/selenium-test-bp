# tests/conftest.py
import os
import pytest
import sys

# Add the project root to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.utils.grid_driver_factory import GridDriverFactory

BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8000')

@pytest.fixture(scope='function')
def driver(request):
    headless = os.environ.get('HEADLESS', '1') == '1'
    use_grid = os.environ.get('USE_GRID', '0') == '1'
    grid_url = os.environ.get('GRID_URL', 'http://localhost:4444')

    # Default to Chrome for single-browser tests using this fixture
    browser = getattr(request, 'param', None) or os.environ.get('BROWSER', 'chrome')

    drv = GridDriverFactory.get_driver(
        browser=browser,
        use_grid=use_grid,
        grid_url=grid_url,
        headless=headless,
    )

    # maximize for non-headless debugging
    if not headless:
        try:
            drv.maximize_window()
        except Exception:
            pass

    yield drv
    try:
        drv.quit()
    except Exception:
        pass
