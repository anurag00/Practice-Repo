#!/usr/bin/python3

import urllib.request
import re

def spanThrough(site_url,count):
	count += 1
	print("==",count,"==> ",site_url);
	try:
		req = urllib.request.Request(site_url)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		paragraph = re.findall(r'href="(h.*?)"',str(respData))
		for line in paragraph:
			if line not in urlList and line not in urlDoneList:
				print(line)
				urlList.append(line)
		if (count <= 30):
			temp = urlList.pop(0)
			spanThrough(temp,count)
	except:
		print("________",site_url,"is not complaint________")
		if count == 1:
			exit(0)
		if (count <= 30):
			temp = urlList.pop(0)
			spanThrough(temp,count)
				

if __name__ == "__main__":
	print("Select a website for scraping: ",end='')
	beg_site_url = input()
	print(beg_site_url + " is selected")

	count = 0
	urlList = [beg_site_url]
	urlDoneList=[]
	beg_site_url = urlList.pop()
	urlDoneList.append(beg_site_url)
	spanThrough(beg_site_url,count)
	print("Ending...")
