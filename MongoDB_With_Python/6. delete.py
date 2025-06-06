import pymongo
if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create or switch to a database
    db = client["mydatabase"]
    
    # Create or switch to a collection
    collection = db["mycollection"]
    
    # Delete one document in the collection
    result = collection.delete_one({"_id": 3})
    print(f"Deleted {result.deleted_count} document(s).")
    
    # Delete multiple documents in the collection
    # result = collection.delete_many({"age": {"$lt": 40}})
    
    # result = collection.delete_many({"_id": {"$eq": 2}})
    # # Print the number of deleted documents
    # print(f"Deleted {result.deleted_count} document(s) with age less than 20.")
    
    
    # Delete all documents in the collection
    # result = collection.delete_many({})
    
    # Delete database
    client.drop_database("sicky")
    
    
    # Examples of MongoDB comparison operators
    print("\nMongoDB Comparison Operators Examples:")
    
    # $eq - Equal to
    collection.find({"age": {"$eq": 25}})
    
    # $gt - Greater than
    collection.find({"age": {"$gt": 25}})
    
    # $gte - Greater than or equal to
    collection.find({"age": {"$gte": 25}})
    
    # $lt - Less than
    collection.find({"age": {"$lt": 25}})
    
    # $lte - Less than or equal to
    collection.find({"age": {"$lte": 25}})
    
    # $ne - Not equal to
    collection.find({"age": {"$ne": 25}})
    
    # $in - Matches any value in array
    collection.find({"age": {"$in": [25, 30, 35]}})
    
    # $nin - Matches none of the values in array
    collection.find({"age": {"$nin": [25, 30, 35]}})
    
    # $exists - Matches documents that have the specified field
    collection.find({"age": {"$exists": True}})
    
    # $regex - Matches pattern
    collection.find({"name": {"$regex": "^J"}})
    