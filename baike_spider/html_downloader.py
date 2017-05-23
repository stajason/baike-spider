from urllib import request
from urllib.parse import quote
import string

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        url = quote(url, safe=string.printable)  # safe表示可以忽略的字符
        # 打开网页
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        else:
            return response.read().decode('utf-8')
