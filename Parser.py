import shutil
from html.parser import HTMLParser


class LangParser:
    def __init__(self, page):
        ...
        
    def handle_starttag(self, tag, attrs):
        ...
        #print('html tag:', tag, ', attrs:', attrs)


class Parser(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.parser = BodyParser
        self.parsers = {
            'html': LangParser,
            'head': HeadParser,
            'body': BodyParser
        }

    def handle_decl(self, data):
        """Handle doctype declaration."""
        data = data.split(' ', 1)[1].strip()
        self.page.doctype = data
        #print('DOCTYPE:', self.page.doctype)

    def handle_starttag(self, tag, attrs):
        print('starttag:', tag, ', attrs:', attrs)
        self.parser = self.parsers.get(tag, self.parser)
        return self.parser(self.page).handle_starttag(tag, attrs)

    def handle_data(self, data):
        """Handle textual data in between opening/closing tags."""
        #print('data:', data)
        #return self.parser.handle_data(data)

    def handle_endtag(self, tag):
        ...
        #print('endtag:', tag)
        #return self.parser.handle_endtag(tag)


class HeadParser:
    def __init__(self, page):
        self.page = page
        self.tags = {
            'head': self.handle_head_tag,
            'meta': self.handle_meta_tag
        }

    def handle_starttag(self, tag, attrs):
        self.tags.get(tag, self.handle_unknown_tag)(tag, attrs)
##        if tag == 'a' and attrs[0][1][-3:] == 'pdf':
##            filename = attrs[0][1].split("/")[1]
##            print('Downloading: {0}...'.format(filename))
##            with open(filename, 'wb') as file:
##                with urllib.request.urlopen(
##                        'https://scripture4all.org/OnlineInterlinear/'
##                        + attrs[0][1]
##                        ) as response:
##                    shutil.copyfileobj(response, file)

    def handle_head_tag(self, tag, attrs):
        ...

    def handle_meta_tag(self, tag, attrs):
        attrs = dict(attrs)
        if 'charset' in attrs:
            self.page.encoding = attrs['charset'].strip().lower()
            print('Encoding set to:', self.page.encoding, 'in handle_meta_tag()')
        
    def handle_unknown_tag(self, tag, attrs):
        print('No handler for', tag, 'tag.')

    def handle_endtag(self, tag):
        ...

    def handle_data(self, data):
        ...


class BodyParser:
    def __init__(self, page):
        ...
        
    def handle_starttag(self, tag, attrs):
        ...

    def handle_endtag(self, tag):
        ...

    def handle_data(self, data):
        ...
