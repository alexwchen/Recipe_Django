from urllib2 import *
from BeautifulSoup import BeautifulSoup
import re

input_urls = open('res_link1.txt')
output_file = open('res_link3.txt', 'w')

count = 0
for url in input_urls:
    url = url.split('"')[1]
    
    soup = BeautifulSoup(urlopen(url).read())

    img_list = []
    imgblock = soup.findAll("img", {"class": "rec-image photo"})
    for block in imgblock: 
        pattern = re.compile('src=".*"')
        result = re.search(pattern,str(block)) 
        if result!=None:
            result_img= str(result.group()).split('"')[1]
            img_list.append(result_img)
    
    title = url.split('/')[-2]
    title = '<title>' +  title + '</title>' + '\n'
    idx = '<idx>' + str(count) + '</idx>' + '\n'
    recipe_open = '<recipe>'+'\n'
    recipe_close = '</recipe>'+'\n'

    print recipe_open
    output_file.write(recipe_open)

    print title
    output_file.write(title)
    
    if len(img_list)==1:
        image_link = img_list[0] 
    else:
        image_link = 'none'
    image_link = '<img_link>' + image_link + '</img_link>' + '\n'
    print image_link
    output_file.write(image_link)

    print idx
    output_file.write(idx)

    print recipe_close
    output_file.write(recipe_close)

    count = count + 1
