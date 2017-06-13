#! /bin/python

from http.client import HTTPConnection, ResponseNotReady 


def write_search_url(site, search):
    return "https://" + site + ".com/search?q=" + '+'.join(search.split())


def is_404(url):
    connection = HTTPConnection(url)
    try:
        code = connection.request("GET", url)
        is_404 = False
    except:
        is_404 = True
    return is_404

if __name__ == "__main__":
    print(check_url_404("www.google.com"))

