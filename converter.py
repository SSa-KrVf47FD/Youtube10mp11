import urllib, json, re

#List of Youtube Video IDs to download
ListofURL = open("list.txt","r")
Ids = [url.strip().replace('https://www.youtube.com/watch?v=','') for url in ListofURL.readlines()]

#Base url
url = "http://www.youtubeinmp3.com/fetch/?format=JSON&video=https://www.youtube.com/watch?v="

for id in Ids:
	
    #Getting the API's download link as json response
    response = urllib.urlopen(url+id)
    data = json.loads("{" + re.findall('\{(.*?)\}', response.read())[0] + "}")

    #Creating a file to download the song to
    target = open(data["title"]+".mp3", 'wb')

    #Downloading the mp3
    mresponse = urllib.urlopen(data["link"])
    mdata = mresponse.read()

    #saving Data to the created file
    target.write(mdata)

    #closing the created file
    target.close()
