import pymongo

if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create or switch to a database
    db = client["mydatabase"]
    
    # Create or switch to a collection
    collection = db["mycollection"]
    
    
    # # Find One document in the collection
    # one_doc = collection.find_one({"_id": 4})
    # if one_doc:
    #     print("Found document:", one_doc)
    # else:
    #     print("No document found with the specified criteria.")
    
        
    # Find All documents in the collection
    all_docs = collection.find({"name": "Alice"}, {"_id": 1, "name": 1, "age": 1}).limit(2)
    
    # Count the number of documents matching the criteria
    count = collection.count_documents({"name": "Alice"})
    print(f"Total matching documents: {count}")
    
    # Print all found documents
    if all_docs:
        print("Found documents:")
        for doc in all_docs:
            print(doc)
    else:
        print("No documents found with the specified criteria.")