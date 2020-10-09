#!/usr/bin/env python3
import picturegrabber
import sys

if len(sys.argv) == 2:
    if sys.argv[1] == "--help":
        print(f"Usage example: python3 download.py sorted.csv pics")
        print(f"This script takes following arguments:")
        print(f"\tOIDlist \t= the plaintext file with Object IDs seperated by lines.")
        print(f"\toutputfolder \t= the name of the folder in which you want the pictures to be placed")
        print("this currently only downloads pictures that are at or over 1920x1080 resolution")
        print("and where the width is larger than the height. This can be changed in the picturegrabber.py")
        print("script. Maybe i will add it as arguments later.")
        exit()
elif len(sys.argv) < 3:
    print(f"Too few arguments ({len(sys.argv)}). Did you supply the list of object IDs and the output folder?")
    exit()
else:
    OIDlist = sys.argv[1]
    outputfolder = sys.argv[2]

with open(OIDlist) as id_list:
    lines = id_list.readlines()
    for line in lines:
        line = str(line).strip()
        picturegrabber.download_image(line, outputfolder)
