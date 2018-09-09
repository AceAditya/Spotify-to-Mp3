#from _future_ import unicode_literals
import youtube_dl
import webbrowser
import urllib.request
import urllib.parse
import re

x= input("Enter the link to the spotify playlist. The playlist must be thirty of less songs.")
url= x
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from lxml import html
import requests
songs=[]
page = requests.get(url)
soup=BeautifulSoup(urlopen(url),'html.parser')
song = soup.find_all("span", {'class': 'track-name'})
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out
length= len(song)
for i in range(length):
    song[i] = remove_html_markup(song[i])
#print(song)

for i in range(0,length):   
	search=song[i]
	#print(search)
	query_string = urllib.parse.urlencode({"search_query" : (search)})
	#print(query_string)

	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	print(html_content)

	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	print(search_results)

	url = "http://www.youtube.com/watch?v=" + search_results[0]
	print(url)
	ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
		