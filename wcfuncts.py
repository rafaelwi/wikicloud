# wcfuncts.py: Word Cloud Functions
# github: rafaelwi

"""
TODO NEXT:
- Allow plots to be generated from just the article name
- Allow changing the attributes of the plot generated
"""

""" Imports """
import sys

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from requests.exceptions import RequestException
from requests import get
from contextlib import closing
from bs4 import BeautifulSoup
import lxml


"""Prints out the message passed in. Used for debugging

Args:
    m: A message

Returns: 
    the message
"""
def log_message(m):
    print (m)
# end log_message(m)


"""Gets the URL and verifies that it is valid
Args:
    args: List of arguments from the command line
Returns:
    the URL entered
"""
def get_url(args):
    # Check if the correct number of args was passed in
    if len(args) != 2:
        log_message('Usage: python3 cloud.py <wikipedia URL>')
        sys.exit()
    # end if

    # Get the URL and check that it is valid
    raw_url = args[1]
    split_url = raw_url.split('/')

    # Validate and return URL
    if (len(split_url) == 5) & (split_url[3] == 'wiki'):
        return raw_url
    # end if
    
    # If the URL is not valid
    else:
        log_message((
            'Error: Ending execution due to invalid URL passed in: <{}>'
            ' URL should be in the form of \x1b[1mhttps://en.wikipedia.org/wik'
            'i/Article_Name \x1b[0m'.format(raw_url)
            ))
        sys.exit()
    # end else
# end get_url(args)


"""Gets the filename of the plot
Args:
    url: Wikipedia URL of the page
Returns:
    A filename for the plot
"""
def get_filename(url):
    return url.split('/')[4] + '.png'
# end get_filename(ur;)



"""Gets the page source of a requested website
Args:
    url: The URL of the page that the source will be taken from
Returns: 
    the source code of the URL passed in
"""
def get_page(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
            log_message('Error during requests to {0} : {1}'
                .format(url, str(e)))
            return None
# end get_page(url)


"""Checks if the response from the URL is good
Args:
    resp: Respond from website of connection status
Returns: 
    true if a successful connection has been made and false otherwise
"""
def is_good_response(resp):
    return (resp.status_code == 200 and resp.headers['Content-Type'].lower() 
    is not None and resp.headers['Content-Type'].lower().find('html') > -1)
# end is_good_response(resp)


"""Gets the text from a webpage found inbetween <p> tags
Args:
    url: URL of the webpage that is being scraped
Returns:
    a string containing all of the text on the page
"""
def get_page_text(url):
    bs4_para_text = ''
    raw_html = get_page(url)
    bs4_html = BeautifulSoup(raw_html, 'lxml')
    log_message('Got raw HTML of <{}>'.format(url))

    # Get all instances of text on the page
    bs4_find_all = bs4_html.find_all('p')

    for i in bs4_find_all:
        bs4_para_text += i.get_text()
    # end for
    
    bs4_para_text = bs4_para_text.lower()
    log_message('Got raw text of <{}>'.format(url))

    return bs4_para_text
# end print_page_text(url)


""" Generates a word cloud from a block of text
Args:
    text: A string containing a block of text
Returns:
    no value. Creates a word cloud as an image and saves it
"""
def generate_word_cloud(text, filename):
    # Word cloud set up
    stopwords = STOPWORDS
    
    # Generate the word cloud
    log_message ('Generating plot...')
    cloud = WordCloud(width = 800, height = 800, background_color = 'white', 
        stopwords = stopwords, min_font_size = 10).generate(text)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    # Save the word cloud
    plt.savefig(filename, bbox_inches='tight')
    log_message('Saved plot as {}!'.format(filename))
# end generate_word_cloud(text, filename)

### end of file wcfuncts.py ###
