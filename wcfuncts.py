# wcfuncts.py: Word Cloud Functions

""" Libraries """
from requests.exceptions import RequrstException
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
            log_message('Error during requests to {0} : {1}'.format(url, str(e)))
            return None
# end get_page(url)


"""Checks if the response from the URL is good

Args:
    resp: Respond from website of connection status

Returns: 
    true if a successful connection has been made and false otherwise
"""
def is_good_response(resp):
    return (resp.status_code == 200 and resp.headers['Content-Type'].lower() is not None and resp.headers['Content-Type'].lower().find('html') > -1)
# end is_good_response(resp)


def print_page_text(url):
    raw_html = get_page(url)
    bs4_html = BeautifulSoup(raw_html, 'html.parser')

