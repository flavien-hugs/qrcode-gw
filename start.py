# start script

from main.make_qrcode import make_qrcode


if __name__ == '__main__':
    website_url = input('Enter your website link: ')
    make_qrcode(website_url)