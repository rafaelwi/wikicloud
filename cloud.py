# wiki word cloud generator
# github: rafaelwi

""" Imports """
import sys
import wcfuncts as wc 

""" Main Program """
# Get URL
url = wc.get_url(sys.argv)

page_text = wc.get_page_text(url)

wc.generate_word_cloud(page_text)