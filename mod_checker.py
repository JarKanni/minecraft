### mod checker: see if mods are up to date
import pandas as pd


# load mod dictionary, links   {name:link}
mods = pd.read_csv(mod_list.csv, index_col=0, skiprows=2)


# ask for $version to check
version = input('Current Version: ')


# check all links for $latest_version
### use beautiful soup??; scrape into json??


# compare versions
    for m in mods:
      if $version > $latest_version
      then add to [not_updated] list
      else add to [updated] list

# print results
    print('Total updated: ' + len(updated) + ' / ' + (len(updated) + len(not_updated)))
    print('Mods needing updates: \n' + not_updated)
