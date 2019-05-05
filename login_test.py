import pytest

@pytest.fixture(scope="module")
def setup(request):
    return "srinivas"

def test_login_page(setUp):
		browser = setUp
		browser.base_page().navigate_to_url("https://storyweaver.org.in")
		browser.login_page().login_with({"email": "abcd@abcd.com", "password": "qwerty"})



