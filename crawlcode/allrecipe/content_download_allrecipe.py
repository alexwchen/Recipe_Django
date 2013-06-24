from urllib2 import *
from BeautifulSoup import BeautifulSoup
import re

input_urls = open('res_link1.txt')
output_file = open('res_link2.txt', 'w')

count = 0
for url in input_urls:
    url = url.split('"')[1]
    
    soup = BeautifulSoup(urlopen(url).read())

    time_list = []
    time_type_list = []
    Timeblock = soup.findAll("div", {"class": "times"})
    for block in Timeblock: 
        new_soup = BeautifulSoup(str(block))
        Time = new_soup("span")
        for time in Time:
            pattern = re.compile('<span>.*</span>')
            result = re.search(pattern,str(time)) 
            if result!=None:
                result_time= str(result.group()).split('<')[1].split('>')[1]
                time_list.append(result_time)

        Time_types = new_soup("h5")
        for time_type in Time_types:
            mytype = str(time_type).replace('<','@').replace('>','@').replace('\n','@').replace('\r','@').split('@')[4]
            time_type_list.append(mytype.replace(' ', '')[:-1])
    
    ingre_list = []
    Ingreblock = soup.findAll("div", {"class": "ingredients"})
    for block in Ingreblock: 
        new_soup = BeautifulSoup(str(block))
        ingre_list = []
        Ingredients = new_soup("li")
        for ingre in Ingredients:
            result_ingre= str(ingre).replace('\n','@').replace('\r','@').split('@')[-1].split('<')[-2]
            ingre_list.append(result_ingre)

    dir_list = []
    Dirblock = soup.findAll("div", {"class": "directions"})
    for block in Dirblock: 
        new_soup = BeautifulSoup(str(block))
        dir_list = []
        directions = new_soup("li")
        for direc in directions:
            result_dir= str(direc).replace('\n','@').replace('\r','@').split('@')[2]
            dir_list.append(result_dir)
    title = url.split('/')[-2]
    
    title = '<title>' +  title + '</title>' + '\n'
    idx = '<idx>' + str(count) + '</idx>' + '\n'
    recipe_open = '<recipe>'+'\n'
    recipe_close = '</recipe>'+'\n'

    print recipe_open
    output_file.write(recipe_open)
    print title
    output_file.write(title)
    print idx
    output_file.write(idx)

    for i in range(len(time_type_list)):
        type_open =  '<' + time_type_list[i] +'>' +'\n'
        time_content = '\t' + time_list[i] +'\n'
        type_close = '</' + time_type_list[i] +'>' +'\n'
        print type_open
        print time_content
        print type_close
        
        output_file.write(type_open)
        output_file.write(time_content)
        output_file.write(type_close)
    
    ingre_open = '<ingredient>' + '\n'
    print ingre_open 
    output_file.write(ingre_open)

    for i in ingre_list:
        print i
        output_file.write(i+'\n')

    ingre_close = '</ingredient>' + '\n'
    print ingre_close
    output_file.write(ingre_close)

    dir_open = '<directions>' + '\n'
    print dir_open
    output_file.write(dir_open)
    for i in dir_list:
        print i 
        output_file.write(i+'\n')
    dir_close = '</directions>' + '\n'
    print dir_close
    output_file.write(dir_close)

    print recipe_close
    output_file.write(recipe_close)
    count = count + 1
