#! /bin/python

from webbrowser import open_new_tab
import plugins.search
import plugins.find


# noinspection PyShadowingNames
def search(args: list):
    query = ' '.join(args[3::])
    site = args[2]

    unsupported_sites = ()

    if site in unsupported_sites:
        print(f"Désolé mais {site} n'est pas supporté par Tux search")
    else:
        url = plugins.search.write_search_url(site, query)
        print("Veuillez patienter. Votre navigateur va s'ouvrir à :", url)
        open_new_tab(url)


def find(args: list):
    if args[2] == "train":
        depart = args[3]
        arrivee = args[4]
        print(plugins.find.get_voyage(depart, arrivee, 3))
    else:
        raise NotImplementedError


commandes = {'search': search, 'find': find}
