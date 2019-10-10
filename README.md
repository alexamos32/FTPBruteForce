# FTPBruteForce
FTP Brute Force Application.
Done as a class assignment.

This application brute forces all permutations of the groups:
(2 Uppercase) + (3 Lowercase) + (2 Numbers)
i.e. AAbbb11
     bbbAA11
     11bbbAA
     etc
     
USAGE: ./ftp_brute_force.py [options]
OPTIONS:  -t, --target  <hostname/ip>
          -u, --user    <username>
          -p, --port    <port>
  
EXAMPLE: ./ftp_brute_force.py -t 192.168.1.2 -u admin -p 21
     
