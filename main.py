from class_s_t import*
from authentication import*
# from file_read_write import*
    

def main():
    select=input("Enter 'Teacher' or 'student' sign in: ")
    if select=="Teacher":

        print("Fill sign in data:\n")

        Name=input("Name: ")
        id=int(input("ID: "))

        if teacher_verification(Name,id)==True:
            t1=Teacher()
            print("Login Successfully!\n")
            select=0
            while select<6:
                select=int(input("Enter the selection for: \n1)Add new student \t2)Add new Teacher \t 3)Detail of all Students \n4)Detail of all teacher \t5)Detail of a student \t6)Detail of teacher\n7)Deletion \t exit"))
                if select==1:
                    t1.s_accept()

                elif select==2:
                    t1.t_accept()

                elif select==3:
                    list1=t1.s_display_all()
                    print("Name of all Students:\n ")
                    for i in list1:
                        print(i)

                elif select==4:
                    list1=t1.t_display_all()
                    print("Name of all Teachers: \n")
                    for i in list1:
                        print(i)

                elif select==5:
                    print("Detail of Student: \n")
                    name=input("Name: ")
                    rollno=int(input("Roll No: "))
                    t1.s_search(name,rollno)

                elif select==6:
                    print("Detail of Teaacher: \n")
                    name=input("Name: ")
                    id=int(input("Id: "))
                    t1.t_search(name,id)
                elif select==7:
                    print("Enter the deletion name roll or id")
                    name=input("Name: ")
                    no_id=input("Roll or id: ")
                    s=input("Enter 'Teacher' for deletion of teacher and 'Student' for deletion of Student.:")
                    t1.delection_record_data(name,no_id,s)
                else:
                    break
                    
        else:
            print("login unsuccessful!\n")

    elif select=="Student":
        print("Fill sign in data:\n")

        Name=input("Name: ")
        rollno=int(input("Roll No: "))

        if student_verification(Name,rollno)==True:
            print("Login Successfully!")

            s1=Student()
    
            while select!=6:
                    select=int(input("Enter the selection for: \n1)my detail \t2)pass_fail \t 3)highest and lowest score \n4)percentage \t5)rank \t6)close"))
                    if select==1:
                        print("Detail of Student: \n")
                        s1.s_search(Name,rollno)

                    elif select==2:
                        print(s1.pass_fail())
                    elif select==3:
                        list1=s1.highes_lowest_score(int(rollno))
                        print("Highest marks: ",list1[0])
                        print("Lowest marks: ",list1[1])
                    elif select==4:
                        print("percentage: ",s1.percentage(rollno))
                    elif select==5:
                        print("Your rank: ",s1.rank(rollno))
                    else: 
                        break
            print("login Unsuccessful!")


            
if __name__=="__main__":
    main()