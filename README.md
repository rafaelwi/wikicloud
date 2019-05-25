# wikicloud
wikipedia word cloud generator in python3

# Features
- Can generate word clouds from a Wikipedia article


# Running
1. Clone the repo using `git clone https://github.com/rafaelwi/wikicloud.git`
2. Ensure that you have `requests`, `matplotlib`, `BeautifulSoup`, and `lxml` are installed
3. Run the script
4. FInd the image of the plot in the `plots` folder

## Using the script
To get a specific article:
`python3 cloud.py https://en.wikipedia.org/wiki/GitHub` or 
`python3 cloud.py page='GitHub'`

For articles with spaces in its name, both `python3 cloud.py page='New_York_City'` and 
`python3 cloud.py page='New York City'` work.

# To add
- Resize plots
- Set fonts
- Set font sizes
- Set colours


