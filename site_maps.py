# __author__ = "Lisa Ferrier"
__date__ = "8 Apr 2022"
# site_maps.py
# Requries Python 3.6 and ArcPro 2.8 or later

'''
This script automates the production of site level maps for SVMP sample prep. 
It assumes the input feature class contains a field named "site_code" and 
iterates through unique values in the attribute table, zooms to the extent of
each 'site' and exports a map named for each site.
'''

import os 
import arcpy
import time

def unique_values(fc, field):
    with arcpy.da.SearchCursor(fc, [field]) as cursor:
        return sorted({row[0] for row in cursor})
    
# set workspace 
basedir = 'C:/Users/lisabelle/Documents/work/projects/2022_site_prep/'
gdb = basedir + 'svmp_site_prep_2022.gdb'


arcpy.env.workspace = gdb

# set feature class and column with site code
fc = 'target_lines_2022_all'
site_list = unique_values(fc, 'site_code')

# initialize map
m = arcpy.mp.ArcGISProject("CURRENT") 

# name of Layout used to produce maps
m_obj = m.listMaps("Site Map")[0]

for site in site_list:
    lyr = m_obj.listLayers(fc)[0]
    
    def_query = "site_code = '{0}'".format(site)
    print(def_query)
    
    lyr.definitionQuery = def_query
    lyt = m.listLayouts()[0]
    
    # Layout has a text element called "Site".
    for elm in lyt.listElements("TEXT_ELEMENT"):
        if elm.name == 'Site':
            elm.text = site

    
    m_frame = lyt.listElements('MAPFRAME_ELEMENT', 'Site Map')[0]
    m_frame.camera.setExtent(m_frame.getLayerExtent(lyr1, False, True))
    m_frame.camera.scale *= 1.25
    
    # output file name.
    # note that the out_file path expects a subdirectory 'maps' is present. Modify as needed. 
    out_file = lyt.exportToPDF(basedir + 'maps/{0}_transect_map.pdf'.format(site))
    
    # to control execution of maps, it's assigned to a variable (out_file). 
    # You can comment the next line out if you want to test that the rest of the variables are valid.
    out_file
    
    # clear the def query and repeat, iterating through the feature class, site by site.
    lyr.definitionQuery = None
