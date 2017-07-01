#! /bin/python
import datetime
from copy import copy
from pprint import pprint
from urllib.request import urlopen

from bs4 import BeautifulSoup


def write_search_url(site, search):
    extension = '.com'
    if '.' in site:
        extension = ''

    join_char = '+'
    slash = "search"
    get_var = 'q'
    protocole = 'https'
    start_get = '?'
    equal = '='
    file_extension = ''

    if site == "qwant":
        join_char = ' '
        slash = ''

    if site == "yahoo":
        site = "search." + site

    if site == "saint-remi.fr":
        slash = 'recherche'
        get_var = 'search_query'

    if site == "google+":
        site = "plus.google"
        slash = "u/0/s/"
        get_var, start_get, equal = '', '', ''
        join_char = ' '

    if site == "openclassrooms":
        slash = "courses"

    if site == "twitter":
        join_char = " "

    if site == "slant":
        extension = ".co"
        get_var = "query"
        join_char = ' '

    if site == "horairetrain":
        extension = ".net"
        slash = "horaires-"
        start_get, get_var, equal = '', '', ''
        join_char = "-"
        file_extension = f'-{write_hour()}.html'

    return protocole + "://" + site + extension + '/' + slash + start_get + get_var + equal + join_char.join(
        search.split()) + file_extension


# noinspection PyShadowingNames
def check404(url):
    pass
    # is_404 = False
    # try:
    #     urlopen(url)
    # except URLError:
    #     is_404 = True
    # return is_404


def write_hour():
    today = datetime.datetime.now()
    month = str(today.month).rjust(2, '0')
    day = str(today.day).rjust(2, '0')
    # if today.minute > 29:
    #     today = today.replace(hour=today.hour+1, minute=0)
    # else:
    #     today = today.replace(minute=30)
    hour = str(today.hour).rjust(2, '0')
    minute = str(today.minute).rjust(2, '0')
    return f"{today.year}{month}{day}-{hour}{minute}"


if __name__ == '__main__':
    url = write_search_url("google", "rien")
    print(url)
    # print(check404(url))
    print(write_hour())
