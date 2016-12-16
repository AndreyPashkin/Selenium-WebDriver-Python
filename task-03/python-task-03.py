import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test(driver):
    driver.get("http://litecart.local/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("1221")
    driver.find_element_by_name("login").click()






