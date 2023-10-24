import sys

import Browser


def display_page(address='http://example.com'):
    argv = sys.argv
    if len(argv) > 1: address = argv[1]
    page = Browser.request_url(address)
    page.render()


display_page()
