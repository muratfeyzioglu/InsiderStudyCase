import pytest
import sys
from selenium import webdriver
from datetime import datetime, date
from pytest_html_reporter import attach
print(sys.path)

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome()

    yield driver
    file_name = f'_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    driver.save_screenshot(".\\screenshots\\" + file_name)
    attach(data=driver.get_screenshot_as_png())

@pytest.fixture()
def log_on_failure(request, setup):
    yield
    item = request.node
    if item.rep_call.failed:
        driver = setup
        driver.save_screenshot(".\\screenshots\\deneme.png")
        attach(data=driver.get_screenshot_as_png())


# check if a test has failed
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# hooks, terminal info,
# get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# return the Browser value to setupp method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")