r'''
Briefing:
Write a function to download and save a sequence of files.
Input: URL for first item, output directory path

Example:
>>> download_files('http://699340.youcanlearnit.net/image001.jpg','\images' )

Successfully downloaded
http://699340.youcanlearnit.net/image001.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image002.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image003.jpg

.
.
.

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
from urllib.request import urlretrieve
from urllib.parse import urlparse
import re

def download_files(url):
    urlPath = urlparse(url).path
    print(urlPath)
    urlPathNum = re.findall('\d+', urlPath)
    if u

    
        
    
    

download_files('http://699340.youcanlearnit.net/image001.jpg')