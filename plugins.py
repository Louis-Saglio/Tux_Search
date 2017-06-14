#! /bin/python

from webbrowser import open_new_tab
from module import *


def search(args: list):
    search = ' '.join(args[3::])
    site = args[2]

    unsupported_sites = []
    if site in unsupported_sites:
        print(f"Désolé mais {site} ne supporte pas ce type de recherche")
    else:
        url = write_search_url(site, search)
    print("Veuillez patienter. Votre navigateur va s'ouvrir à :", url)
    open_new_tab(url)


commandes = {'search': search}
