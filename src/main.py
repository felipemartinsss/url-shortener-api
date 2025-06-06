import hashlib
from url_shortener import URLShortener

def receive_input_url():
    return input("Digite uma url: ")

if __name__ == '__main__':
    original_url = receive_input_url()
    url_shortener = URLShortener()
    shortened_url = url_shortener.shorten(original_url)
    url_shortener.print_urls(original_url, shortened_url)
