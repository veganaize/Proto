import argparse
import sys

import Browser


homepage = 'http://example.com/homepage'


def parse_arguments():
    argument_parser = argparse.ArgumentParser(
            prog='Proto',
            description='Web browser written in Python 3.4',
            epilog='https://github.com/veganaiZe/Proto'
    )
    
    argument_parser.add_argument(
            'address',
            default=homepage,
            help='A web address with an "http://" or "https://" prefix.',
            nargs='?'
    )
    
    arguments = argument_parser.parse_args()

    print('arguments.address:', arguments.address)
    return arguments.address


def display_page(address=homepage):
    page = Browser.request_url(address)
    page.render()


if __name__ == '__main__':
    address = parse_arguments()
    display_page(address)
