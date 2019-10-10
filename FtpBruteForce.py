import sys
import argparse
import ftplib
from WordListGenerator import checkFile
from WordListGenerator import Generate



parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-p", "--port")

args = parser.parse_args()



fileExists = checkFile()
if not fileExists:
    Generate()




