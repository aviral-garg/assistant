import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constant import GOOGLE_URL


class WebBrowser:
    # todo: ability to use current browser

    def __init__(self, browser=webdriver.Chrome()):
        # assumption: correct chromedriver in PATH env var
        self.driver = browser

    @staticmethod
    def clean_url(url: str) -> str:
        """
        :param url: [str] url to clean
        :return: [str] url with "https://www." or "https://" added as prefixes, if absent
        """
        if url is None:
            raise Exception('clean_url:', '`url` not present')

        url = url.strip("https://")
        url = url.strip("www.")
        url = "https://www." + url
        return url

    def open(self, url: str):
        if url is None:
            raise Exception('open:', '`url` not present')

        url = self.clean_url(url=url)
        self.driver.get(url=url)

    def google_search(self, search_words: str = None):
        if not search_words:
            raise Exception('g_search:', '`search_words` not present')

        self.open(url=GOOGLE_URL)
        time.sleep(1)
        search_box = chrome.driver.find_element_by_name('q')
        search_box.send_keys(search_words)
        search_box.submit()


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=selenium")
    chrome = WebBrowser(browser=webdriver.Chrome(options=chrome_options))

    # cookies = pickle.load(open("cookies.pkl", "rb"))
    # for cookie in cookies:
    #     chrome.driver.add_cookie(cookie)

    # @formatter:off
    chrome.open(url="https://www.linkedin.com/in/aviralgarg/detail/interests/companies/")           # test open()
    # chrome.google_search('aviral garg')     # test google_search()
    # @formatter:off

    # time.sleep(30)
    # pickle.dump(chrome.driver.get_cookies(), open("cookies.pkl", "wb"))

    # chrome.driver.quit()
