import http.client
import urllib.request

from Page import Page, Response


user_agents = {
    'proto': 'Mozilla/5.0 Proto/0.1',
    'firefox2win32': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
    'firefox115win64': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'firefox115lin64': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0',
    'firefox115lin32': 'Mozilla/5.0 (X11; Linux i686; rv:115.0) Gecko/20100101 Firefox/115.0',
    'firefox109win64': 'Mozilla/5.0 (Windows NT 10.0; Win64; rv:109.0) Gecko/20100101 Firefox/109.0)',
    'firefox108win64': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    'firefox35lin64': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
    'chrome79win64': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'win7win64': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
}


def request_url(address):
    try:
        return Page(Response(urllib.request.urlopen(address)))
    except:
        print('Exception! Opening URL.')
        return Page(Response())
