import firebase_admin
from firebase_admin import credentials, firestore
from typing import Any, Dict


CREDENTIALS_PATH = "./firebase/firebase.json"

cred = credentials.Certificate(CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()






def addUser(name: str, age: int, cpf: str) -> bool:
    existing_users = db.collection("users").where("cpf", "==", cpf).stream()
    if any(existing_users):
        return False

    doc_ref = db.collection("users").document(cpf)
    doc_ref.set({
        "cpf": cpf,
        "name": name,
        "age": age,
    })
    return True

def listUsers() -> None:
    docs = db.collection("users").stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
        
def listAccounts() -> None:
    docs = db.collection("accounts").stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def attUser(docId: str, newData: Dict[str, Any]) -> bool:
    doc_ref = db.collection("users").document(docId)
    
    if not doc_ref.get().exists:
        return False
    doc_ref.update(newData)
    return True

def deleteUser(docId: str):
    doc_ref = db.collection("users").document(docId)
    if not doc_ref.get().exists:
        return False
    db.collection("users").document(docId).delete()
    return True
    
if __name__ == "__main__":
    listUsers()
    input()
    listAccounts()
