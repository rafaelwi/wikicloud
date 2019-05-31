# wiki word cloud generator
# github: rafaelwi

""" Imports """
import sys
import wcfuncts as wc 

""" Main Program """
# Data order: Height (-hi), Width (-wi), Background Color (-bg)
cloud_format = [800, 800, 'white']

# Parse command line arguements
url = wc.parse_cl_args(sys.argv, cloud_format)

# Get filename
filename = wc.get_filename(url)

# Get page text
page_text = wc.get_page_text(url)

# Generate and save word cloud
wc.generate_word_cloud(page_text, filename, cloud_format)

### end of script cloud.py ###
