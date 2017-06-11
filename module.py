def write_search_url(site, search):
    return "https://" + site + ".com/search?q=" + '+'.join(search.split())
