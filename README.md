# Tux_Search

Cortana for Linux

## Install
### For noobs

    Clone the repository in /opt with : "sudo cd /opt && git clone git@github.com:Louis-Saglio/Tux_Search.git"

    Then move the file /opt/Tux_Search/tux_run to /usr/local/bin/ with "sudo mv /opt/Tux_Search/tux_run /opt/Tux_Search/tux"

    Then allow everybody to use Tux-Search with : "sudo chmod -R a+x /opt/Tux_Search/ && chmod a+x /usr/local/bin/tux"

### For normal users

    Download the repository where you want

    Then add tux_run to your path for easy launching and rename it by tux, it's shorter  than tux_run

    Edit this file if you didn't install Tux_Search in /opt

## Commands available
### tux search

    tux search <site-name> query

    open a navigator searching the query in the site (only for sites supporting searching)

    examples :
        tux search google my query
        tux search github Louis-Saglio tux search

### tux find train

    tux search train <departure station-name> <arrival station-name>

    list next trains wich travel from deaparture station to arrival station

    Warning : You must provide a valid station name eg: Paris-Montparnasse is valid while Paris is not.

    examples :
        -   tux find train Bordeaux-Saint-Jean Langon

        -   tux find train Dunkerque Perpignan

        -   tux find Londres ManchesterAiroport

