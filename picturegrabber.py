#!/usr/bin/env python3
import urllib.request
import urllib.parse
import requests
from PIL import Image

requrl = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"


def download_image(OID: str, outputfolder: str):
    global requrl
    r = requests.get(url=requrl + OID)
    print(str(r))
    if str(r) != "<Response [200]>":
        return None
    data = r.json()

    picurl = data["primaryImage"]
    picurl = picurl.replace(' ', '%20')
    
    # check res and aspect ratio
    image = Image.open(urllib.request.urlopen(picurl))
    width, height = image.size

    print(f"w: {width} and h: {height}")
    if width > height and width >= 1920 and height >= 1080:
        urllib.request.urlretrieve(picurl, outputfolder + '/' + OID + ".jpg")
