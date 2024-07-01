from file_read_write import*
from authentication import*
from validation import*

# set0=["Hari",10,"hari@gmail.com",000000000,"Kathmandu","Teacher","Maths"]
# set1=["sita",12,"sita@gmail.com",000000000,"Pokhara","Student",[10,20,30,40,50,60,70]]
# set2=["rita",13,"rita@gamil.com",000000000,"Nepaljung","Teacher","Science"]

# write(set0)
# write(set1)
# write(set2)

# data=read()
# print(data)
def marks_search(rollNo):
        dict1=read()
        marks=[]
        for i in dict1:
            if i.get("rollno")==rollNo:
                marks=i.get("marks")
                break
        
        return marks


class Student:
    
    def __init__(self,status="Student"):
        self.Name=""
        self.Rollno=int
        self.email=""
        self.phone=int
        self.address=""
        self.status=status
        self.marks=[]

    def s_accept(self):
        self.Name=input("name: ")
        while email_validation(self.email)!=True:
            self.email=input("email: ")
            print(email_validation(self.email))
            if email_validation(self.email)==True:
                print("valide email\n")
            else:
                print("invalide email renter in: _____@___.__ form\n")
        
        while phone_validation(self.phone)!=True:
            self.phone=int(input("phone no: "))
            print(phone_validation(self.phone))
            if phone_validation(self.email)==True:
                print("valide phone no")
            else:
                print("invalide phone no renter in: length of 10 digit number form\n")
        
        self.address=input("address: ")

        while roll_or_id_unique_validation(self.Rollno,self.status)!=True:
            self.Rollno=input("rollno: ")
            if roll_or_id_unique_validation(self.Rollno,self.status)==True:
                print("valide rollno no\n")
            else:
                print("invalide rollno renter:\n ")
        
        for i in range(1,5):
            mark=int(input("Enter the marks:",i," subject: "))
            self.marks.append(mark)
        list1=[self.Name,self.Rollno,self.email,self.phone,self.address,self.status,self.marks]
        write(list1)
    
    def s_display_all(self):
        dict1=read()
        list_data=[]
        for i in dict1:
            if i.get("status")=="Student":
                self.Name=i.get("Name")
                list_data=list_data.append(self.Name)
                return list_data
            else:
                pass
               
        return list_data
    
    def s_search(self,name,roll):
        dict=read()
        print("Detail of student:",name,"\n")
        for i in dict:
            if self.Rollno==roll:
                self.Name=i.get("Name")
                self.Rollno=i.get("roll")
                self.email=i.get("email")
                self.phone=i.get("phone_no")
                self.address=i.get("address")
                break
            else:
                pass 
    from file_read_write import read
        
    def pass_fail(self,rollNo):
        marks=marks_search(rollNo)
        for i in marks:
            if i>=32:
                x="pass"
            else:
                x="Fail"
                break
        return x


    def highes_lowest_score(self,rollNo):
        marks=marks_search(rollNo)
        highest_marks=0
        lowest_marks=0
        list_highest_lowest=[]
        for i in marks:
            if i>=highest_marks:
                highest_marks=i
            elif i<=lowest_marks:
                lowest_marks=i
        list_highest_lowest.append[highest_marks]
        list_highest_lowest.append[lowest_marks]
            
        return list_highest_lowest

    def percentage(self,rollNo):
        marks=marks_search(rollNo)
        
        total_marks=0
        x=0
        for i in marks:
            total_marks=total_marks+i
            x=x+1
        percentage=(total_marks)*100/x
        return percentage

    def rank(self,rollNo):
        marks=marks_search(rollNo)
        total_marks=0
        x=0
        for i in marks:
            total_marks=total_marks+i
            x=x+1
        my_percentage=(total_marks)*100/x
        rank=1
        
        student_percentage=0.0
        dict1=read()
        n=1
        for i in dict1:
            if i.get("status")=="Student":
                marks=i.get("marks")
                for i in marks:
                    rank=rank+1
                    total_marks=total_marks+i
                    n=n+1       
                student_percentage=((total_marks)*100/n)
                if my_percentage>student_percentage:
                    rank=rank-1
                else:
                    pass

        return rank
# s1=Student()
# s1.search("Hari")
class Teacher(Student):

    def __init__(self):
        Student.Name=""
        self.id=int
        Student.email=""
        Student.phone=int
        Student.address=""
        self.status="Teacher"
        self.subject=""

    def t_accept(self):
        self.Name=input("name: ")

        while email_validation(self.email)!=True:
            self.email=input("email: ")
            print(email_validation(self.email))
            if email_validation(self.email)==True:
                print("valide email\n")
            else:
                print("invalide email renter in: _____@___.__ form\n")

        while phone_validation(self.phone)!=True:
            self.phone=int(input("phone no: "))
            print(phone_validation(self.phone))
            if phone_validation(self.email)==True:
                print("valide phone no")
            else:
                print("invalide phone no renter in: length of 10 digit number form\n")

        self.address=input("address: ")

        while roll_or_id_unique_validation(self.id,self.status)!=True:
            self.id=input("rollno: ")
            if roll_or_id_unique_validation(self.id,self.status)==True:
                print("valide rollno no\n")
            else:
                print("invalide rollno renter:\n ")
        list1=[self.Name,self.Rollno,self.email,self.phone,self.address,self.status,self.subject]
        write(list1)


    def t_display_all(self):
        dict1=read()
        list_data=[]
        for i in dict1:
            if i.get("status")=="Teacher":
                self.Name=i.get("Name")
                list_data=list_data.append(self.Name)
                return list_data
            else:
                pass
               
        return list_data
        
    def t_search(self,name):
        dict=read()
        for i in dict:
            if self.Name==name:
                self.Name=i.get("Name")
                self.id=i.get("id")
                self.email=i.get("email")
                self.phone=i.get("phone_no")
                self.address=i.get("address")
                # print(i)
                break
            else:
                pass
    def delection_record_data(self,name,number_id,selection):
        if selection=="Teacher":
            data_deletion_teacher(name,number_id)
        elif selection=="Student":
            data_deletion_student(name,number_id)
        else:
            print("No deletion")

# s1=student()
# # master_key=teacher("Teacher",Name="Aashish",email="aashis5657@gmail.com",phone=9841907142,address="Dolpa",id=10,subjectstatus="All")
# # list1=master_key.list_return()
# # print(list1)
# # print(master_key.Name)
# # print(master_key.email)
# # count=1
# # while count==1:
# #     count=int(input("Enter 1 for re"))

