from tinydb import TinyDB, Query
from typing import Union
q = Query()

tindb = TinyDB("db.json", indent = 4)

def get_stadions():
    items = tindb.tables()
    return items

def get_stadion_by_item(stadion: str):
    if stadion in get_stadions():
        collection = tindb.table(stadion)
        return collection.all()
    else:
        return [] 
    
def get_stadion_by_id(stadion: str, doc_id: Union[int, str]):
    if stadion in get_stadions():
        collection = tindb.table(stadion)
        item = collection.get(doc_id=doc_id)
        return item
