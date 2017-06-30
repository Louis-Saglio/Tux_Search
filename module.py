#! /bin/python

from http.client import HTTPConnection, ResponseNotReady 
from urllib.error import URLError
from urllib.request import urlopen

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
    
    return protocole + "://" + site + extension + '/' + slash + start_get + get_var + equal + join_char.join(search.split())


def check404(url):
    is_404 = False
    try:
        urlopen(url)
    except URLError:
        is_404 = True
    return is_404


if __name__ == '__main__':
    url = write_search_url("google", "rien")
    print(url)
    print(check404(url))

