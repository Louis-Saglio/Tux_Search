#! /bin/python

from webbrowser import open_new_tab
from module import write_search_url


def search(site: str, search: str):
    open_new_tab(write_search_url(site, search))


commandes = {'search': search}

