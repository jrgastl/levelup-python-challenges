'''
Briefing:
Write a function to download and save a sequence of files.
Input: URL for first item, output directory path

Example:
>>> download_files('http://699340.youcanlearnit.net/image001.jpg','./images' )

Successfully downloaded
http://699340.youcanlearnit.net/image001.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image002.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image003.jpg

...

Successfully downloaded
http://699340.youcanlearnit.net/image049.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image050.jpg

Could not retrive
http://699340.youcanlearnit.net/image051.jpg

Documentation:
https://realpython.com/python-download-file-from-url/
https://docs.python.org/3/library/re.html#frie09
https://docs.python.org/3/howto/regex.html#regex-howto
https://docs.python.org/3/library/re.html
'''
from urllib.request import urlopen,urlretrieve
from urllib.parse import urlparse, urlunparse
import re
import requests

def check_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    print(requests.get(url,headers=headers).status_code)
    if requests.get(url,headers=headers).status_code in range(200,300):
        return True
    return False

def download_files(url,output_path):
    urlScheme, urlNetloc, urlPath, urlParams, urlQuery, urlFragment  = urlparse(url)
    pathNumPos = re.finditer(r'[0-9]+', urlPath) # Parse the part of the url that has the file path (in the example "/image001.jpg") and get all the numbers positions
    iteratorsSpan = [num.span() for num in pathNumPos if int(num.group()) == 1 ] # Separate the position for numbers that are equal to 1 in value
    # urlretrieve(url,''.join([output_path,urlPath])) # Download the first file
    # print(f'Successfully downloaded!\n{url}') # Download the first file
    for span in iteratorsSpan:
        iterator = int(urlPath[span[0]:span[1]])
        iterator += 1
        iteratorStr = str(iterator).zfill(len(urlPath[span[0]:span[1]]))
        urlPath = ''.join([urlPath[:span[0]],iteratorStr,urlPath[span[1]:]])
        downloadUrl = urlunparse([urlScheme, urlNetloc, urlPath, urlParams, urlQuery, urlFragment])
        if check_url(downloadUrl):
            downloadUrl = url
            urlretrieve(downloadUrl,''.join([output_path,urlPath])) # Download the first file
            print(f'Successfully downloaded!\n{downloadUrl}') # Download the first file
            while True:
                iterator = int(urlPath[span[0]:span[1]])
                iterator += 1
                iteratorStr = str(iterator).zfill(len(urlPath[span[0]:span[1]]))
                urlPath = ''.join([urlPath[:span[0]],iteratorStr,urlPath[span[1]:]])
                downloadUrl = urlunparse([urlScheme, urlNetloc, urlPath, urlParams, urlQuery, urlFragment])
                if check_url(downloadUrl):
                    urlretrieve(downloadUrl,''.join([output_path,urlPath])) # Download the first file
                    print(f'Successfully downloaded!\n{downloadUrl}') # Download the first file
                else:
                    break
            print(f'Could not retrieve!\n{downloadUrl}') # Download the first file

# download_files('http://699340.youcanlearnit.net/image001.jpg','./downloads')
print(check_url('http://699340.youcanlearnit.net/image060.jpg'))