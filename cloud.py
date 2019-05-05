# wiki word cloud generator
# github: rafaelwi

""" Libraries """
# For word cloud

#import mathplotlib.pyplit as plt

# For reading the page
import wcfuncts as wc 

# System Functions
from os import path
import urllib.request
import sys


""" Main Program """
url = 'https://en.wikipedia.org/wiki/Death_Grips'

page_text = wc.get_page_text(url)

wc.generate_word_cloud(page_text)