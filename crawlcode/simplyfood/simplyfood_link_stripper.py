from urllib2 import *
from BeautifulSoup import BeautifulSoup

def first_stage():
	file = open('res_link1.txt')
	output_file = open('res_link2.txt', 'w')
	for line in file:
		newline = line.split('"')
		nn = newline[2].split("<")
		print "tags", nn[0][1:]
		print "links", newline[1]
	
		output_file.write('tags~')
		output_file.write(nn[0][1:])
		output_file.write('\n')
	
		output_file.write('links~')	
		output_file.write(newline[1])
		output_file.write('\n')

def second_stage():
	file2 = open('res_link2.txt')
	output_file2 = open('res_link3.txt', 'w')
	count = 0;

	for line in file2:
		newl = line.split('~')	
		if newl[0] == "links":
			url = str(newl[1])
			soup = BeautifulSoup(urlopen(url).read())

			mainblock = soup.findAll("div", {"class": "archive-entry"})
			for block in mainblock:
				blockS = str(block)
				soupB = BeautifulSoup(blockS)

				try:
					imgtag = soupB('img')	
					imglink = '\t<img_link_1>' +  str(imgtag).split('"')[1] + '</img_link_1>'+'\n'
					linktag = soupB('a')[1]
					link_to_page = '\t<page_link>' + str(linktag).split('"')[1] + '</page_link>'+'\n'
					title = '\t<title>' + str(linktag).split('"')[1].split('/')[-2] + '</title>'+'\n'
					id_ = '\t<idx>' + str(count) + '</idx>'+'\n'
					recipe_headstart = '<recipe id=' + str(count) + '>'+'\n'

					print recipe_headstart
					print title
					print id_
					print link_to_page
					print cat_string
					print imglink
	
					output_file2.write(recipe_headstart)
					output_file2.write(title)
					output_file2.write(id_)
					output_file2.write(link_to_page)
					output_file2.write(cat_string)
					output_file2.write(imglink)
					count= count + 1
		
	
				except:
					recipe_headstart = '<recipe id=' + str(count) + '>'+'\n'
					linktag = soupB('a')[0]
					link_to_page = '\t<page_link>' + str(linktag).split('"')[1] + '</page_link>'+'\n'
					title = '\t<title>'+ str(linktag).split('"')[1].split('/')[-2] +'</title>'+'\n'
					id_ = '\t<idx>' + str(count) + '</idx>'+'\n'
					imglink = '\t<img_link_1>none</img_link_1>'+'\n'

					print recipe_headstart				
					print title
					print id_
					print link_to_page
					print cat_string
					print imglink
	
					output_file2.write(recipe_headstart)
					output_file2.write(title)
					output_file2.write(id_)
					output_file2.write(link_to_page)
					output_file2.write(cat_string)
					output_file2.write(imglink)
					count= count + 1
		
	
					continue
				recipe_headclose = '</recipe>\n'
				print recipe_headclose
				output_file2.write(recipe_headclose)
		else:
			cat_string = '\t'+'<category_tags>' + line.split('~')[1][:-1] + '</category_tags>'+'\n'


def third_stage():
	file3 = open('res_link3.txt').read()
	output_file4 = open('res_link4.txt', 'w')
	output_file5 = open('res_link5.txt', 'w')

	soup = BeautifulSoup(file3)


	recipe = soup('recipe')
	empty_dict = {}
	for sec in recipe:
		smallsec = BeautifulSoup(str(sec))
	
		smallsec = BeautifulSoup(str(sec))
		titles = smallsec('title')
		pattern = re.compile('>.*<')
		result = re.search(pattern,str(titles))
		result = str(result.group()[1:-1])
		ids = smallsec('idx')
		pattern = re.compile('>.*<')
		idxx = re.search(pattern,str(ids))
		idxx = str(idxx.group()[1:-1])
	
		#if idxx[-1] == '>' or idxx[-1] == '>':
		#	print idxx
		#	print result + '\n'

		if result not in empty_dict:
			empty_dict[result] = []
			empty_dict[result].append(idxx)
		else:
			empty_dict[result].append(idxx)

	for em in empty_dict:
		output_file4.write(str(em) + '\n')
		output_file4.write(str(empty_dict[em]) + '\n')

	new_count = 0
	new_dict = {}
	for titles in empty_dict:
	
		# merging tags from different indecies 
		new_tag_list = []
		for index in empty_dict[titles]:
			tmp = soup('recipe', {"id": str(index)})
			rec = BeautifulSoup(str(tmp))
			cat_tags = rec('category_tags')
			new_tag_list.append(cat_tags)  # Important 1
		
		tmp = soup('recipe', {"id": str(index)})
		rec = BeautifulSoup(str(tmp))
		title = rec('title') # Important 2
		link_to_page = rec('page_link') # Important 3
		imglink = rec('img_link_1') # Important 4
		# Important 5  & 6, id and header
	 	
	
		# Start printing out all information
	 	rec_start =  '<recipe id="' + str(new_count) + '">' + '\n'
		print rec_start
		output_file5.write(rec_start)
	
		rec_title =  '\t' + str(title)[1:-1] + '\n'
		print rec_title
		output_file5.write(rec_title)
	
		rec_idx =  '\t' + '<idx>' + str(new_count) + '</idx>' + '\n'
		print rec_idx
		output_file5.write(rec_idx)
	
		for instance in new_tag_list:
			rec_tag = '\t' + str(instance)[1:-1] + '\n'
			print rec_tag
			output_file5.write(rec_tag)
		
		rec_page_link =  '\t' + str(link_to_page)[1:-1] + '\n'
		print rec_page_link
		output_file5.write(rec_page_link)
	
		rec_img_link =  '\t' + str(imglink)[1:-1] + '\n'
		print rec_img_link
		output_file5.write(rec_img_link)

	 	rec_close =  '</recipe>' + '\n'
		print rec_close
		output_file5.write(rec_close)
	
		# increment count
		new_count = new_count + 1


file5 = open('res_link5.txt').read()
output_file6 = open('res_link6.txt', 'w')

soupR = BeautifulSoup(file5)

recipe = soupR('recipe')
for sec in recipe:
	smallsec = BeautifulSoup(str(sec))
	title = str(smallsec('title'))[1:-1]
	page_link = str(smallsec('page_link'))[1:-1]
	idxx = str(smallsec('idx'))[1:-1]
	
	pattern = re.compile('>.*<')
	idx2 = re.search(pattern,str(idxx))
	idx2 = str(idx2.group()[1:-1])
	
	cattags = str(smallsec('category_tags'))[1:-1]
	imgglink = str(smallsec('img_link_1'))[1:-1]
	recipe_start = '<recipe id="' + idx2 + '">'
	
	print recipe_start + '\n'
	print '\t' + title + '\n'
	print '\t' + page_link + '\n'
	print '\t' + idxx + '\n'
	print '\t' + cattags + '\n'
	print '\t' + imgglink + '\n'

	output_file6.write('\t' + recipe_start + '\n')
	output_file6.write('\t' + title + '\n')
	output_file6.write('\t' + page_link + '\n')
	output_file6.write('\t' + idxx + '\n')
	output_file6.write('\t' + cattags + '\n')
	output_file6.write('\t' + imgglink + '\n')

	pattern = re.compile('>.*<')
	page_link = re.search(pattern,str(page_link))
	page_link = str(page_link.group()[1:-1])
			
	c =urlopen(str(page_link))
	content = c.read()
	soup = BeautifulSoup(content)


	# Tags
	tags = soup('div', {'class': 'entry-meta'})
	tagP = BeautifulSoup(str(tags))
	soupP = tagP('p')
	
	tags_open = '\t' + '<category_tags_2>' + '\n'
	print tags_open
	output_file6.write(tags_open)

	for p in soupP:
		printed_tags = '\t\t' + str(p) + '\n'
		print printed_tags
		output_file6.write(printed_tags)
		
	tags_close = '\t' + '</category_tags_2>' + '\n'
	print tags_close
	output_file6.write(tags_close)

	#print '********************************************\n'

	# Introduction
	intro = soup('div', {'id': 'recipe-intro'})
	introFocus = BeautifulSoup(str(intro))
	soupP = introFocus('p')
	
	intro_open = '\t' + '<intro_text>' + '\n'
	print intro_open
	output_file6.write(intro_open)
	
	for p in soupP:
		intro_print =  '\t\t' + str(p) + '\n'
		print intro_print
		output_file6.write(intro_print)

	# Introduction notes
	intronotes = soup('div', {'id': 'recipe-intronote'})
	introFocus = BeautifulSoup(str(intronotes))
	soupP = introFocus('p')
	for p in soupP:
		intro_print2 = '\t\t' + str(p) + '\n'
		print intro_print2
		output_file6.write(intro_print2)
		
	intro_close = '\t' + '</intro_text>' + '\n'
	print intro_close
	output_file6.write(intro_close)

	#print '********************************************\n'

	# Ingredients
	ingredients = soup('div', {'id': 'recipe-ingredients'})
	ingredients_div = BeautifulSoup(str(ingredients))
	ingredients_li = BeautifulSoup(str(ingredients_div))
	soupli = ingredients_li('li')
	
	ingre_open = '\t' + '<ingre_text>' + '\n'
	print ingre_open
	output_file6.write(ingre_open)
	
	for li in soupli:
		ingre_list =  '\t\t' + str(li) + '\n'
		print ingre_list
		output_file6.write(ingre_list)

	ingre_close = '\t' + '</ingre_text>' + '\n'
	print ingre_close
	output_file6.write(ingre_close)

	#print '********************************************\n'

	# Method 
	method = soup('div', {'id': 'recipe-method'})
	method_div = BeautifulSoup(str(method))
	method_p = BeautifulSoup(str(method_div))
	soupP = method_p('p')

	method_open = '\t' + '<method_text>' + '\n'
	print method_open
	output_file6.write(method_open)
	
	for p in soupP:
		method_print = '\t\t' + str(p) + '\n'
		print method_print
		output_file6.write(method_print)

	method_img = BeautifulSoup(str(method_div))
	soupImg = method_img('img')
	for imglink in soupImg:
		method_img = '\t\t' + str(imglink) + '\n'
		print method_img
		output_file6.write(method_img)
		
	method_close = '\t' + '</method_text>' + '\n'
	print method_close
	output_file6.write(method_close)

	recipe_close = '</recipe>' + '\n'
	print recipe_close
	output_file6.write(recipe_close)






				