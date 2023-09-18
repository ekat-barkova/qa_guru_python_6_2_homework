import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.config.window_width = 1280
    browser.config.window_height = 720


@pytest.fixture
def open_url():
    browser.open('https://google.com')


def test_search(browser_size, open_url):
     browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
     browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_search_no_result(browser_size, open_url):
    browser.element('[name="q"]').should(be.blank).type('fdfdfdfdfdh141cnjmmmmmm').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))