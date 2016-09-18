from lxml import html
import requests

while 1:
	name=raw_input()
	if name=='end':
		break

	page=requests.get('http://codeforces.com/profile/'+name)
	tree=html.fromstring(page.content)

	rating = tree.xpath('/html/body/div[2]/div[3]/div[2]/div[2]/div[5]/div[2]/ul/li[1]/span[1]/text()')
	for l in rating:
		print l