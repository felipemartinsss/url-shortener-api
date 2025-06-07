import hashlib
from repository import insert_url_mapping, recover_url_mapping

class URLShortener:
    def __init__(self):
        self.md5 = hashlib.md5()

    def shorten(self, original_url):
        encoded_original_url = original_url.encode('utf-8')
        self.md5.update(encoded_original_url)
        shortened_url = self.md5.hexdigest()
        insert_url_mapping(original_url, shortened_url)
        return shortened_url

    def recover(self, shortened_url):
        original_url = recover_url_mapping(shortened_url)
        return original_url

    def print_urls(self, original_url, shortened_url):
        print(f'Original URL: {original_url}, Shortened URL: {shortened_url}')
