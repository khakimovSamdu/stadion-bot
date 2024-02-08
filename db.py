from tinydb import TinyDB, Query
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
    

def get_stadion_malumot(manzil: str):
    collection = tindb.table("Stadions")
    items = collection.search(q.manzil==manzil)
    return items

