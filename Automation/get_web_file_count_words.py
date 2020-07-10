"""
Retrieve web page and count the words
"""

import urllib

def get_web_page_count_words(url):
    count_map = {}
    urlh = urllib.urlopen(url)
    for line in urlh:
        words = line.split()
        for word in words:
            count_map[word] = count_map.get(word, 0) + 1

    print(count_map)


def search_hyperlinks():
    url = raw_input("Enter the URL:")
    html = urllib.urlopen(url).read()
    # html is a string with all the lines
    links = re.findall('href="http://.+?"', html)
    #findall returns the list that matches the regular expression
    for link in links:
        print link
