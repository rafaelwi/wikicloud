# wiki word cloud generator
# github: rafaelwi

""" Libraries """
# For word cloud
import numpy
import pandas as pd 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplit as plt

# For reading the page
from requests.exceptions import RequrstException
from requests import get
from contextlib import closing
from bs4 import BeautifulSoup
import lxml

# System Functions
from os import path
import urllib.request
import sys


""" Main Program """