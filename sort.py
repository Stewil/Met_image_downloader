#!/usr/bin/env python3

import csv
import sys


csv.field_size_limit(sys.maxsize)
infile = "MetObjects.csv"
outfile = "sorted.csv"
lines_to_read = 1000

params = [
        [8,"Painting","Drawing","Print"], # object name
        [3,"True"], #is public doamin
        ]

outlist = []

def readline():
    global infile, outlist, lines_to_read
    i = lines_to_read
    try:
        with open(infile, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in linereader:
                #print(f"Line{i}: {len(row)}")
                if i <= 0:
                    break
                else:
                    i -= 1
                    if compare(row):
                        outlist.append(row)
    except IndexError as e:
        print(f"Index error in line {lines_to_read - i}")
                



def compare(row):
    global params
    param = params[0]
    
    for arg in param[1:]:
        if len(row) < 9:
            raise IndexError("Row too short!")
        #print(f"is {arg} in {row[param[0]]}")
        if arg in row[param[0]] and params[1][1] in row[params[1][0]]:
            return True


def run():
    global lines_to_read, outlist, infile
    if len(sys.argv) < 2:
        print(f"too few arguments ({len(sys.argv)})")
        return None
    if sys.argv[1] == "--help":
        print("Usage example: python3 sort.py MetFile.csv 5000")
        print(f"This script takes a file name of the Met Museum CSV file, and an amount of lines.")
        print("Big files can take a while. Default is 1000 lines")
        print("Output is a file called sorted.csv")
        return None
    else:
        infile = sys.argv[1]
        if not os.isfile(infile):
            print(f"Wrong filename supplied: {infile}")
    if isinstance(sys.argv[2], int):
        lines_to_read = sys.argv[2]
    elif sys.argv[2] is not None:
        try:
            lines_to_read = int(sys.argv[2])
        except ValueError:
            print("ERROR: value supplied is NaN")
            return None
    if lines_to_read < 1:
        print("No lines to read (did you give a positive integer?")
        return None
    readline()
    #for item in outlist:
        #print(item[0])
    with open(outfile, 'w', newline='') as csvfile:
        linewriter = csv.writer(
                csvfile, 
                )
        for item in outlist:
            linewriter.writerow([item[4]])    
    print(f" Generated list of {len(outlist)} entries")



if __name__ == '__main__':
    run()
