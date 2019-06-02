# wiki word cloud generator
# github: rafaelwi

""" Imports """
import sys
import wcfuncts as wc 

""" Main Program """
# Data order: Height (-hi), Width (-wi), Background Color (-bg), Font (-f)
# The colors that can be used for -bg can be found here:
#   https://drafts.csswg.org/css-color-4/#named-colors
cloud_fmt = CloudFormat(height = 800, width = 800, background_color = 'white',
    font = 'font', scale = 1)

# Parse command line arguements
url = wc.parse_cl_args(sys.argv, cloud_format)

# Get filename
filename = wc.get_filename(url)

# Get page text
page_text = wc.get_page_text(url)

# Generate and save word cloud
wc.generate_word_cloud(page_text, filename, cloud_format)

### end of script cloud.py ###
