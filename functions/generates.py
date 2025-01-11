import random
import string
from firebase.config import db



def generateNum() -> str:
    while True:
        num = str(random.randint(100000000, 999999999))
        
        accountsRef = db.collection("accounts").document(num)
        if not accountsRef.get().exists: 
            return num



def generatePix() -> str:
    while True:
        pix = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
        
        accountsRef = db.collection("accounts")
        query = accountsRef.where("keys", "array_contains", pix).get()
        
        if not query:
            return pix