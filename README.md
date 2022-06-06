L Ferrier
6 June 2022

The site_map.py script automates the production of site level maps for SVMP sample prep. 
It assumes the input feature class contains a field named "site_code" and 
iterates through unique values in the attribute table, zooms to the extent of
each 'site' and exports a map named for each site.
