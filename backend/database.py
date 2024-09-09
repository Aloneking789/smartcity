import pymongo

def connect_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["cctv_monitoring"]
    return db

# Use the database to store issues
db = connect_db()
issue_collection = db["issues"]

def report_issue(issue):
    issue_collection.insert_one(issue)

def get_all_issues():
    return list(issue_collection.find({}))
