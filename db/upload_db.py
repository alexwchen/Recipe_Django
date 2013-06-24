import sys,os
from datetime import *
sys.path.append('/Users/alexwchen/Desktop/')
os.environ['DJANGO_SETTINGS_MODULE'] ='recipe.settings'

from django.core.management import setup_environ
from recipe import settings

setup_environ(settings)

sys.path.append('/Users/alexwchen/Desktop/recipe')
from recipe.clusterEngine.models import Recipe


import re
from urllib2 import *
from BeautifulSoup import BeautifulSoup

allRec = Recipe.objects.all()

f_store = open('allrec_new.xml').read()
#f_store = open('test.xml').read()

soup = BeautifulSoup(f_store)
recipes = soup('recipe')

for rec in recipes:
	
	eachrec = BeautifulSoup(str(rec))
	pattern = re.compile('>.*<')

	try:
		r_title = str(eachrec('title'))[1:-1] +'\n'
		search = re.search(pattern,r_title)
		r_title = str(search.group()[1:-1])
	
		r_idx = str(eachrec('idx'))[1:-1] +'\n'
		search = re.search(pattern,r_idx)
		r_idx = str(search.group()[1:-1])

		r_url = str(eachrec('url'))[1:-1] +'\n'
		search = re.search(pattern,r_url)
		r_url = str(search.group()[1:-1])

		r_imgurl = str(eachrec('imgurl'))[1:-1] +'\n'
		search = re.search(pattern,r_imgurl)
		r_imgurl = str(search.group()[1:-1])
	
		direcs = str(eachrec('direcs'))[1:-1] +'\n'	
		direcs = direcs.replace("\r","@")
		direcs = direcs.replace("\t","@")
		direcs = direcs.split("\n")
		direcs_list = []
	
		for i in direcs:
			if i!="@":
				direcs_list.append(i.replace("@", ""))
		direcs_list = direcs_list[1:-2]

		ingr = str(eachrec('ingr'))[1:-1] +'\n'	
		ingr = ingr.replace("\r","@")
		ingr = ingr.replace("\t","@")
		ingr = ingr.split("\n")
		ingr_list = []
	
		for i in ingr:
			if i!="@":
				ingr_list.append(i.replace("@", ""))
		ingr_list = ingr_list[1:-2]
		
		if r_title=='':
			r_title = url.split('/')[-2]
		
		
		print '[ '+ r_idx + ' ]', r_title
		#print r_url
		#print r_imgurl
		#print direcs_list
		#print ingr_list
		
		newrec = Recipe(title=r_title)
		newrec.idx = r_idx
		newrec.url = r_url
		newrec.img_url = r_imgurl
		
		tmpMethod = ''
		for i in direcs_list:
			tmpMethod = tmpMethod + i + '\n'
		newrec.method = tmpMethod

		tmpIngr = ''
		for i in ingr_list:
			tmpIngr = tmpIngr + i + '\n'
		newrec.ingredient = tmpIngr
		
		newrec.save()
	except:
		continue