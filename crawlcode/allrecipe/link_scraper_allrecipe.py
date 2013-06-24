from urllib2 import *
from BeautifulSoup import BeautifulSoup
import re


output_file1 = open('res_link1.txt', 'w')

link = 'http://allrecipes.com/recipes/ViewAll.aspx?Page='
for i in range(2400):
    url = link + str(i+1)
    soup = BeautifulSoup(urlopen(url).read())

    print i+1

    mainblock = soup.findAll("div", {"class": "rectitlediv"})
    for block in mainblock:
        new_soup = BeautifulSoup(str(block))
        links = new_soup("a")[0]
        pattern = re.compile('href=".*"')
        result = re.search(pattern,str(links))
        
        recipelink = str(result.group())

        print recipelink
        output_file1.write(recipelink+'\n')

