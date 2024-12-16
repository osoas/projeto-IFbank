from globalsVar import nums
import random

def generateNum() -> str:
    num = str(random.randint(100000000, 999999999))
    while num in nums:
        num = str(random.randint(100000000, 999999999)) 
    return num