
import os.path

def check_file():
    res = os.path.exists('BruteForceList.txt')
    if res:
        return True
    else:
        return False


def generate():
   
    f = open("BruteForceList.txt", "a")
    
    for i in range(65, 91):


        for j in range(65, 91):


            for k in range(97, 123):



                for l in range(97, 123):


                    for m in range(97, 123):


                        for n in range(48, 58):


                            for o in range(48, 58):
                                f.write(chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n) + chr(o)  + '\n')

    f.close()
    return

    
  

    








