import hashlib
from url_shortener import URLShortener

def receive_input_url():
    return input("Digite uma url: ")

# TODO: Can be turned to an API
if __name__ == '__main__':
    url_shortener = URLShortener()
    option = input("Digite 1 para obter uma url encurtada e 2 para recuperar uma url original: ")
    if option == '1':
        original_url = receive_input_url()
        shortened_url = url_shortener.shorten(original_url)
        url_shortener.print_urls(original_url, shortened_url)
    elif option == '2':
        shortened_url = input("Digite uma url encurtada: ")
        original_url = url_shortener.recover(shortened_url)
        url_shortener.print_urls(original_url, shortened_url)
    else:
        print("Opção inválida")
