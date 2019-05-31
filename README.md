# wikicloud
wikipedia word cloud generator in python3

# Features
- Can generate word clouds from a Wikipedia article


# Running
1. Clone the repo using `git clone https://github.com/rafaelwi/wikicloud.git`
2. Ensure that you have `requests`, `matplotlib`, `BeautifulSoup`, and `lxml` are installed
3. Run the script
4. Find the image of the plot in the `plots` folder

## Using the script
To get a specific article:
`python3 cloud.py -a https://en.wikipedia.org/wiki/GitHub` or 
`python3 cloud.py -a GitHub` or
`python3 cloud.py -a 'New York City'`

To specify the height and width, use the `-hi` and `-wi` options respectively. The defaults
are `-hi 800 -wi 800`
`python3 cloud.py -a Github -hi 1000 -wi 4000`

To specify the background color, use the `-bg` option. A list of possible arguements can be
found [here](https://drafts.csswg.org/css-color-4/#named-colors)
`python3 cloud.py -a GitHub -bg 'darkviolet'`

# To add
- Resize plots
- Set fonts
- Set font sizes
- Set colours


