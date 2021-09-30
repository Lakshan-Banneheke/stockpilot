import certifi
import pymongo

def create_collection(db,tName):
    coll = db[tName]

def insert_one_to_collection(db,data,cName): # data to be inserted as a dictionery
    coll = db[cName]
    return(coll.insert_one(data)) # returns the object id

def insert_many_to_collection(db,data,cName): # data is a list containing all the dictioneries
    coll = db[cName]
    return(coll.insert_many(data)) # returns object ids as a list

def read_one_from_collection(db,data,cName): # data should be the query as a dictionery
    coll = db[cName]
    return(coll.find_one(data)) # returns first occurence

def read_many_from_collection(db,data,cName): # data should be the query as a dictionery
    coll = db[cName]
    result = []
    for read in coll.find(data): # returns a cursor instance of the documents related
        result.append(read)
    return(result) 

def update_one_document(db,query,newValues,cName):
    coll = db[cName]
    return(coll.update_one(query,newValues))

def count_document(db,data,cName):
    coll = db[cName]
    return(coll.count_documents(data)) # returns the matching document count

def remove_one_from_collection(db,data,cName): # data contains the required query
    coll = db[cName]
    return(coll.delete_one(data))

def remove_many_from_collection(db,data,cName): # data contains the required query
    coll = db[cName]
    return(coll.delete_many(data))

def delete_collection(db,cName): # data contains the required query
    coll = db[cName]
    return(coll.drop())




def db_action(type,parameters,user_type):  # Can do all the db actions through this function

    admin_url = 'mongodb+srv://SEPU01:User123@sepcluster.yjn4m.mongodb.net/test_sep?retryWrites=true&w=majority'

    general_url = 'mongodb+srv://SEPU02:general123@sepcluster.yjn4m.mongodb.net/test_sep?retryWrites=true&w=majority'

    dbName = 'StockPilot'

    if (user_type=="admin"):
        url = admin_url
    elif(user_type=="general"):
        url = general_url
    else:
        return("Error")

    client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

    db = client[dbName]

    if(True):
        if (type=="create_collection"):
            result = create_collection(db,parameters)
        elif(type=="insert_one"):
            result = insert_one_to_collection(db,parameters[0],parameters[1])
        elif(type=="insert_many"):
            result = insert_many_to_collection(db,parameters[0],parameters[1])
        elif(type=="read_one"):
            result = read_one_from_collection(db,parameters[0],parameters[1])
        elif(type=="read_many"):
            result = read_many_from_collection(db,parameters[0],parameters[1])
        elif(type=="update_one"):
            result = update_one_document(db,parameters[0],parameters[1],parameters[2])
        elif(type=="count"):
            result = count_document(db,parameters[0],parameters[1])
        elif(type=="remove_one"):
            result = remove_one_from_collection(db,parameters[0],parameters[1])
        elif(type=="remove_many"):
            result =  remove_many_from_collection(db,parameters[0],parameters[1])
        elif (type == "delete_collection"):
            result = delete_collection(db, parameters[0])
        else:
            result = "DB Action not specified"

        return(result)
    # except ValueError:
    #     return("Unexpected Value Error")
    # except:
    #     return("Unexpected Error Has occured")

        

    
    

# create_collection("test02")

# insert_one_to_collection({"name_id":"nimal","age":23,"email":"nimal@skl.com"},"test02")

# insert_many_to_collection([{"name_id":"nimal","age":23,"email":"nimal@skl.com"},{"name_id":"kamal","age":33,"email":"nimal@skl.com"},{"name_id":"nimaal","age":233,"email":"nial@skl.com"}],"test02")

# read_one_from_collection({"name_id":"nimal"},"test01")

# read_many_from_collection({"name_id":"nimal"},"test01")

# print(count_document({"email":"nimal@skl.com"},"test01"))

# print(remove_one_from_collection({"name_id":"nimal"},"test01"))

# print(remove_many_from_collection({"email":"nimal@skl.com"},"test01"))

# print(db_action("insert_many",[[{"id":23,"val":1},{"id":34,"val":4},{"id":67,"val":3}],"test02"],"admin"))



