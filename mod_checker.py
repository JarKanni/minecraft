### mod checker: see if mods are up to date

# load mod dictionary, links
mods = {name:link}


# ask input for $version to check
version = input('Version?')


# check all links for $latest_version



# compare versions
    for m in mods:
      if $version > $latest_version
      then add to [not_updated] list
      else add to [updated] list

# print results
    print('Total updated: ' + len(updated) + ' / ' + (len(updated) + len(not_updated)))
    print('Mods needing updates: \n' + not_updated)
