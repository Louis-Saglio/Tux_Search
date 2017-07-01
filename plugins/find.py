from urllib.request import urlopen
from bs4 import BeautifulSoup
from plugins.search import write_search_url


def get_voyage(depart, arrivee, try_again=0):

    if try_again == -1:
        return f"Aucun résultat trouvé pour le trajet {depart} {arrivee}\n"

    depart = get_gare_name(depart)
    arrivee = get_gare_name(arrivee)

    # noinspection PyShadowingNames
    url = write_search_url("horairetrain", f"{get_url_gare_name(depart)} {get_url_gare_name(arrivee)}")
    content = urlopen(url)
    content = content.read()
    # sleep(2)

    soup = BeautifulSoup(content, "html5lib")
    divs = soup.find_all(class_="t-s-c")
    durations = soup.find_all(class_="duree-c duree-empty")
    durations = [duration.text for duration in durations if duration.text != "\xa0"]

    rep = ''
    i = 0
    # Pour une raison encore indéterminée, il semble impossible d'utiliser zip
    for div in divs:
        texte = div.text.replace("\n", "")
        horaire = texte[:5:]
        gare = get_gare_name(texte[5::])
        if gare == depart:
            rep += f"{gare}\t{horaire}\t\t"
        if gare == arrivee:
            rep += f"{gare}\t{horaire}\t\t{durations[i]}\n"
            i += 1
    if not rep:
        # rep = "Aucun résultat n'a été trouvé"
        rep = get_voyage(depart, arrivee, try_again=try_again-1)
    return rep


def get_url_gare_name(name: str):
    name = name.replace("-St-", "saint")
    name = name.replace("-Saint-", "st")
    name = name.replace('-', '')
    name = name.replace(' ', '')
    for lettre in "éêèë":
        name = name.replace(lettre, "e")
    for lettre in "àâä":
        name = name.replace(lettre, "a")
    for lettre in "ùûü":
        name = name.replace(lettre, "u")
    name = name.lower()
    return name


def get_gare_name(name: str):
    return name.replace("Saint", "St")


if __name__ == '__main__':
    print(get_voyage("Bordeaux-Saint-Jean", "Cérons"))
    print(get_voyage("Paris-Montparnasse", "La Réole"))
    print(get_voyage("Perpignan", "Dunkerque"))
