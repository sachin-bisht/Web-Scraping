import requests
import sys
from lxml import html

#user input
handle = input("Enter handle : ")

#valid username url
url = 'https://www.codechef.com/users/' + handle

page = requests.get(url)

tree = html.fromstring(page.content)

data = tree.xpath("//script[contains(text(), 'jQuery(document).foundation();')]/text()")

if len(data) == 0:
	print("Handle is invalid")
	sys.exit()

i = 0
cb = 0

while(1):
	cb = 0
	if i != 0:
		if(data[0][i-1] == ']' and data[0][i] == ';'):
			break
	if data[0][i] == '{':
		while(1):
			str = ""
			if(data[0][i] == ':'):
				cb += 1
			if(cb == 1):
				i += 2
				while(data[0][i] != '"'):
					str += data[0][i]
					i += 1
				print(str)
				break
			i += 1
		i += 1
	i += 1

# P.S. ---> I prefer avoiding regex
