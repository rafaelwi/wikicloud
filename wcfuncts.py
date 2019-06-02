# wcfuncts.py: Word Cloud Functions
# github: rafaelwi

"""
TODO NEXT:
- Fix README
- Make plots go to plots folder in Pictures folder
- Allow changing the attributes of the plot generated
"""

""" Imports """
import sys
import argparse

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


""" Parse arguements from command line

Args:
    args: A list of arguements from the command line

Returns: 
    Article URL if -a flag is used, version number or about otherwise
"""
def parse_cl_args(args, cloud_format):
    # Set up arguements parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action="store_true", 
        help='shows version number')
    parser.add_argument('-ab', '--about', action="store_true", 
        help='shows about the author')
    parser.add_argument('-a', '--article', help=('the name or URL of the art'
        'icle of which you want to generate a word cloud for'))
    parser.add_argument('-hi', '--height', help='the height of the word cloud',
        type=int)
    parser.add_argument('-wi', '--width', help='the width of the word cloud',
        type=int)
    parser.add_argument('-bg', '--background_color', help=('background color '
        'of the word plot'))
    parser.add_argument('-f', '--font', help='font used in the word cloud')

    args = parser.parse_args()

    # --version/-v arguement
    if args.version:
        log_message('wikicloud ver. 2019.05.30')
        sys.exit()
    # end if

    # --about/-ab arguement
    elif args.about:
        log_message(('wikicloud is a python script written by rafaelwi that '
            'generates word clouds from wikipedia articles. Use `python3 '
            ' cloud.py --help` to learn how to use the script.'))
        sys.exit()
    # end elif

    # Formatting for the word cloud
    # --height/-hi argument
    if (args.height):
        if (args.height > 0):
            cloud_format[0] = args.height
    
    # --width/-wi argument
    if (args.width):
        if (args.width > 0):
            cloud_format[1] = args.width

    # --background_color/-bg argument
    if (args.background_color):
        cloud_format[2] = args.background_color

    # --font/-f arguement
    if (args.font):
        cloud_format[3] = args.font

    # --article/-a arguement
    if args.article:
        raw_article = args.article
        print(raw_article)
        article_url = validate_article(raw_article)
        return(article_url)
    # end else
# end parse_cl_args(args)


"""Validate the input of the article input from command line

Args:
    article: URL or name of article

Returns:
    A URL of the article
"""
def validate_article(article):
    # Check if what has been passed in is a URL or just the name of an article
    # If URL is passed in
    if article.startswith('https://en.wikipedia.org/wiki'):
        if ((article.split('/')[0] == 'https:') & 
            (article.split('/')[2] == 'en.wikipedia.org') &
            (article.split('/')[3] == 'wiki')):
                return article

    # If an article name is passed in
    else:
        article_name = article.replace(' ', '_')
        return ('https://en.wikipedia.org/wiki/{}'.format(article_name))
# end validate_article(article)


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

    # Check if a valid page was fetched
    if raw_html == None:
        log_message(('Error: Ending execution due to no article named "{}" on '
        'Wikipedia. Please make sure you have typed in the page name '
        'correctly'.format(url.split('/')[4].replace('_', ' '))))
        sys.exit()
    # end if

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
def generate_word_cloud(text, filename, cloud_format):
    # Word cloud set up
    stopwords = STOPWORDS
    
    # Generate the word cloud
    log_message('Generating plot...')
    try:
        cloud = WordCloud(height = cloud_format[0], width = cloud_format[1],  
            background_color = cloud_format[2], font_path = cloud_format[3],
            stopwords = stopwords, min_font_size = 10).generate(text)
    except:
        log_message(('Could not generate word cloud due to bad font path, '
            'using fallback font DroidSansMono'))
        cloud = WordCloud(height = cloud_format[0], width = cloud_format[1],  
            background_color = cloud_format[2], stopwords = stopwords, 
            min_font_size = 10).generate(text)
    plt.figure(figsize = (8, 8), facecolor = cloud_format[2])
    plt.facecolor = (cloud_format[2])
    plt.imshow(cloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    # Save the word cloud
    cloud.to_file(filename)
    log_message('Saved plot as {}!'.format(filename))
# end generate_word_cloud(text, filename)
### end of file wcfuncts.py ###
