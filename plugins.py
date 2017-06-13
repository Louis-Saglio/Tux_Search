#! /bin/python

from webbrowser import open_new_tab
from module import *


def search(site: str, search: str):
    url = write_search_url(site, search)
    if is_404(url):
        print(f"Désolé, {site} n'accèpte pas ce type de recherche.")
        return
    open_new_tab(url)


commandes = {'search': search}
