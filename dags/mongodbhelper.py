from pymongo import MongoClient


def get_connection():
    db_name=None
    try:
      client=MongoClient("mongodb+srv://dev:dev123@cluster0.xv26xln.mongodb.net/");
      db_name = client["automation_config"]
      print(db_name)
    except Exception as exception:
      print(exception)
    return db_name
      
      
def insert_single_document(collection_name,query,projection=None):  
 collection_data=None
 try:
  db_name=get_connection()   
  collection = db_name[collection_name]
  print(collection)
  collection_data=collection.insert_one(query,projection)
  print(collection_data)
 except Exception as exception:
   print(exception)
  
 return collection_data

def get_single_document(collection_name,query,projection=None):  
 collection_data=None
 try:
  db_name=get_connection()   
  collection = db_name[collection_name]
  print(collection)
  collection_data=collection.find_one(query,projection)
  print(collection_data)
 except Exception as exception:
   print(exception)
  
 return collection_data
  
def update_single_document(collection_name,query,projection=None):  
 collection_data=None
 try:
  db_name=get_connection()   
  collection = db_name[collection_name]
  print(collection)
  collection_data=collection.update_one(query,projection)
  print(collection_data)
 except Exception as exception:
   print(exception)
  
 return collection_data
  

if __name__=="__main__":
  update_single_document("config",{"name":"abc"},{"_id":0})