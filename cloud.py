# wiki word cloud generator
# github: rafaelwi

""" Libraries """
# For reading the page
import wcfuncts as wc 

""" Main Program """
url = 'https://en.wikipedia.org/wiki/Death_Grips'

page_text = wc.get_page_text(url)

wc.generate_word_cloud(page_text)