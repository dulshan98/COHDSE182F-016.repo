import pymongo
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["Mylogin"]
collection = db["login"]

user = input("Enter User Name : ")
password = input("Enter Your Password : ")
for y in collection.find({},{"userName":1,"password":1}):
    user = str(y["userName"])
    Password = str(y["password"])
if user == userName and password == Password:
    print("\nLogin Successful!!\n")
else:
    print("\nUser doesn't exist or wrong password!!\n")
