L Ferrier
6 June 2022

The site_map.py script automates the production of site level maps for SVMP sampling. 

It assumes the input feature class contains a field named "site_code". 

The script loops through unique "site_code" values in the attribute table, zooms to the site extent (via defition query) and exports a map for each site. Expects there is a text element in the map layout named 'Site' which is updated for each map to include the site code. Refer to the screenshot image for reference.



