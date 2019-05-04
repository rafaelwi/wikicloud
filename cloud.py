# wiki word cloud generator
# github: rafaelwi

""" Libraries """
# For word cloud
import numpy
import pandas as pd 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#import mathplotlib.pyplit as plt

# For reading the page
import wcfuncts as wc 

# System Functions
from os import path
import urllib.request
import sys


""" Main Program """
url = 'https://en.wikipedia.org/wiki/Death_Grips'

wc.print_page_text(url)