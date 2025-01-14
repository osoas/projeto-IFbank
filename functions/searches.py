from firebase_admin import firestore
from classes.accountClass import Account
import firebase_admin
from firebase.config import db

def searchAccountByCpf(cpf: str) -> Account | None:
    usersRef = db.collection("users")
    query = usersRef.where("cpf", "==", cpf).get()

    if query:
        userDoc = query[0]
        userId = userDoc.id
        accountsRef = db.collection("accounts")
        accountQuery = accountsRef.where("holderId", "==", userId).get()

        if accountQuery:
            accountData = accountQuery[0].to_dict()
            return Account(
                password=accountData['password'],
                num=accountData['num'],
                holderId=accountData['holderId'],
                keys=accountData['keys'],
                RealValue=accountData.get('realValue', 0),
                contacts=accountData.get("contacts", [])
            )   
    return None


def searchAccountByNum(num: str) -> Account | None:
    accountsRef = db.collection("accounts")
    query = accountsRef.where("num", "==", num).get()

    if query:
        accountData = query[0].to_dict()
        return Account(
            password=accountData['password'],
            num=accountData['num'],
            holderId=accountData['holderId'],
            keys=accountData['keys'],
            RealValue=accountData.get('realValue', 0),
            contacts=accountData.get("contacts", [])

        )
    return None


def searchAccountByKey(key: str) -> Account | None:
    accountsRef = db.collection("accounts")
    query = accountsRef.where("keys", "array_contains", key).get()
    if query:
        accountData = query[0].to_dict()
        return Account(
            password=accountData["password"],
            holderId=accountData["holderId"],
            num=accountData["num"],
            RealValue=accountData.get("realValue", 0),
            keys=accountData.get("keys", [])
        )   
    return None