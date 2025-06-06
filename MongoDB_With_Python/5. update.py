import pymongo
if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create or switch to a database
    db = client["mydatabase"]
    
    # Create or switch to a collection
    collection = db["mycollection"]
    
    # Update a document in the collection
    result = collection.update_one({"_id": 4}, {"$set": {"age": 22, "name": "Sicky"}})
    
    if result.modified_count > 0:
        print(f"Document updated successfully. Modified count: {result.modified_count}")
    else:
        print("No documents were updated.")
    # Find the updated document
    updated_doc = collection.find_one({"_id": 4},{"_id": 1, "name": 1, "age": 1})
    if updated_doc:
        print("Updated document:", updated_doc)
    else:
        print("No document found with the specified criteria.")