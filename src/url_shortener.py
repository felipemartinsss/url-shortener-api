import hashlib

class URLShortener:
    def __init__(self):
        self.md5 = hashlib.md5()

    def shorten(self, original_url):
        encoded_original_url = original_url.encode('utf-8')
        self.md5.update(encoded_original_url)
        hex_digest = self.md5.hexdigest()
        # TODO: still need to record in database
        return hex_digest

    def recover(self, shortened_url):
        # TODO: query from database and return it if found
        return None

    def print_urls(self, original_url, shortened_url):
        print(f'Original URL: {original_url}, Shortened URL: {shortened_url}')
