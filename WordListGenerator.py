
import os.path

def checkFile():
    res = os.path.exists('BruteForceList.txt')
    if res:
        return True
    else:
        return False


def Generate():
    import datetime
    start = datetime.datetime.now()
    print 'script execution started at:', start

    

    
    f = open("BruteForceList.txt", "a")
    #arr = ['C', 'C', 'L', 'L', 'L', 'N', 'N']
    ##printArr = [0,0,0,0,0,0,0]
    #asciiRange = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    #for i in range(0, 7):
    #    if arr[i] == 'C':
    #        asciiRange[i][0] = 65
    #        asciiRange[i][1] = 91
    #    
    ##    elif arr[i] == 'L':
     #       asciiRange[i][0] = 97
    #        asciiRange[i][1] = 123

#        else:
 #           asciiRange[i][0] = 48
 #           asciiRange[i][1] = 58
 #       
 #   #TESTING IF RANGE SETUP WORKED, WORKS   
 #   #for i in range(0, 7):
    #    print asciiRange[i][0]
    #    print asciiRange[i][1]

    for i in range(65, 91):


        for j in range(65, 91):


            for k in range(97, 123):



                for l in range(97, 123):


                    for m in range(97, 123):


                        for n in range(48, 58):


                            for o in range(48, 58):
                                f.write(chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n) + chr(o)  + '\n')

    f.close()

    end = datetime.datetime.now()
    print 'Script execution ended at:', end
    totaltime = end - start
    print 'Script totally ran for :', totaltime
    return

    
  

    








