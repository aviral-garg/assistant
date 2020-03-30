import time

from WebBrowser import WebBrowser
from constant import WAKING_UP_URL


class WakingUp(WebBrowser):
    def __init__(self):
        super().__init__()
        self.open(url=WAKING_UP_URL)

    def next_session(self):
        pass


if __name__ == '__main__':
    chrome = WakingUp()

    # @formatter:off
    # chrome.google_search('aviral garg')     # test google_search()
    # chrome.open()                           # test open()
    # @formatter:off

    time.sleep(5)
    chrome.driver.quit()
