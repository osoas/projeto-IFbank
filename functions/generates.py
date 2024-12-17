import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from globalsVar import nums
import random
import string



def generateNum() -> str:
    num = str(random.randint(100000000, 999999999))
    while num in nums:
        num = str(random.randint(100000000, 999999999)) 
    return num


numspix = []
def generatePix() -> str:
    while True:
        pix = ''.join([str(random.choice(string.ascii_letters  + string.digits)) for _ in range(9)])

        if pix not in numspix:
            numspix.append(pix)
            return pix


    