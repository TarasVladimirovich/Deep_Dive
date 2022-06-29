from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        # if radius value is set we invalidate our cached _area value
        # we could make this more intelligent and see if the radius has actually changed
        # but keeping it simple
        self._area = None
        # we could even add validation here, like value has to be numeric, non-negative, etc
        self._radius = value

    @property
    def area(self):
        if self._area is None:
            # value not cached - calculate it
            print('Calculating area...')
            self._area = pi * (self.radius ** 2)
        return self._area


c = Circle(1)
print(c.area)
c.radius = 2
c.area
c.area
c.area

import requests
from time import perf_counter


class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # we'll lazy load the page - i.e. we wait until some property is requested

    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if self._page is None:
            # need to first download the page
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        resp =  requests.get(self.url)
        self._page = resp.text
        end_time = perf_counter()

        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time


urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')
