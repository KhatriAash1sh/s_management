import json

"""
Here is the functon that access the datas of json file which directly affect the database
function like readfunction,writefunction,data_deletion functions
"""

def read():
    list1=[]
    try:
        with open("data.json","r") as file:
            list1 = json.load(file)
    except:
        print("No file")

    return list1
    
def write(listdata):
    name = listdata[0]

    if listdata[5]=="Teacher":
        id=listdata[1]
    else:
        rollno=listdata[1]

    email=listdata[2]
    phone_no=listdata[3]
    address=listdata[4]
    status=listdata[5]

    if status=="Teacher":
        subject=listdata[6]
    else:
        marks=listdata[6]

    list1 = []
    try:
        with open("data.json","r") as file:
            list1 = json.load(file)
    except:
        print("No file")

    if status=="Teacher":
        dict1 = {
            "Name" : name,
            "id" : id,
            "email": email,
            "phone_no":phone_no,
            "address":address,
            "status":status,
            "subject":subject,
        }
    elif status=="Student":
        dict1 = {
            "Name" : name,
            "rollno" : rollno,
            "email": email,
            "phone_no":phone_no,
            "address":address,
            "status":status,
            "marks":marks
        }

    list1.append(dict1)

    with open("data.json", "w") as file:
        json.dump(list1, file)


def data_deletion_student(name,rollno):
    list1=[]
    list2=[]
    try:
        with open("data.json","r") as file:
            list1 = json.load(file)
    except:
        print("No file")
    
    for i in list1:
        if i.get("rollno")==rollno:
            pass
        else:
            list2.append(i)
        
    with open("data.json", "w") as file:
        json.dump(list2, file)
        
    print(f"Student Name::{name} and Roll no: {rollno} was deleted")

def data_deletion_teacher(name,id):
    list1=[]
    list2=[]
    try:
        with open("data.json","r") as file:
            list1 = json.load(file)
    except:
        print("No file")
    
    for i in list1:
        if i.get("id")==id:
            pass
        else:
            list2.append(i)
        
    with open("data.json", "w") as file:
        json.dump(list2, file)
        
    print(f"Teacher Name::{name} and ID no.: {id} was deleted")
            
    

# list0=["Hari",10,"hari@gmail.com",000000000,"Kathmandu","Teacher","maths"]
# list1=["sita",12,"sita@gmail.com",000000000,"Pokhara","Student",[20,30,40,50]]
# list2=["rita",13,"rita@gamil.com",000000000,"Nepaljung","Student",[100,97,99,98]]

# write(list0)
# write(list1)
# write(list2)

# data=read()
# print(data)

# data_deletion_teacher("Hari",10)





    