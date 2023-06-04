from pymongo import MongoClient

client=MongoClient("mongodb+srv://dev:dev123@cluster0.xv26xln.mongodb.net/");

db = client["automation_config"]
collection = db["config"]


collection_data=collection.insert_one({"unsername":"abhisim0098@gmail.com","password":"test@123"})