from Parser import Parser


class Response:
    def __init__(self, response):
        self.response = response

    def read(self):
        try:
            return self.response.read()
        except:
            print('response.read() failed')
            return b''

    def getheader(self, header):
        try:
            return self.response.getheader(header).lower().split()
        except:
            return ['', '']


class Page:
    def __init__(self, response):
        self.doctype = ''
        self.encoding = 'iso-8859-1'  # HTTP 1.1 Default
        self.html = ''
        self.lang = 'unknown'
        self.mime_type = ''
        self.response = response
        self.html = response.read().decode(self.determine_encoding().encoding)

    def determine_encoding(self):
        self.mime_type, encoding = self.response.getheader('Content-Type')
        if encoding.strip() == 'charset=utf-8':
            self.encoding = 'utf-8'

        print('Encoding:', self.encoding)
        return self

    def render(self):
        Parser(self).feed(self.html)
        print(self.html)
        return self
