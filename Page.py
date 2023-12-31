from Parser import Parser


class Response:
    def __init__(self, response=None, bytes_string=b''):
        self.response = response
        self.bytes_string = bytes_string

    def read(self):
        try:
            return self.response.read()
        except:
            print('response.read() failed')
            return self.bytes_string

    def getheader(self, header):
        try:
            return self.response.getheader(header).lower().split()
        except:
            return ['', '']


class Page:
    def __init__(self, response):
        self.doctype = ''
        self.encoding = 'iso-8859-1'  # HTTP 1.1 Default
        self.html = b''
        self.lang = 'unknown'
        self.mime_type = ''
        self.response = response
        self.html = response.read()

    def as_source(self):
        return self.html.decode(self.determine_encoding().encoding)
    
    def determine_encoding(self):
        self.mime_type, encoding = self.response.getheader('Content-Type')
        if encoding.strip() == 'charset=utf-8':
            self.encoding = 'utf-8'
            print('Encoding set to:', self.encoding, 'in determine_encoding()')
            
        return self

    def render(self):
        Parser(self).feed(self.html.decode(self.determine_encoding().encoding))
        return self
