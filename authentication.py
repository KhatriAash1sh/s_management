from file_read_write import read

dict1=read()

def teacher_verification(Name,id):
    for i in dict1:
        if i.get("Name")==Name:
            if i.get("id")==id:
                return True #id match person as teacher
            else:
                a=False
        else:
            a=False #id unmatch
    return a

# print(teacher_verification("Hari",10))


def student_verification(Name,rollno):
    for i in dict1:
        if i.get("Name")==Name:
            if i.get("rollno")==rollno:
                return True #rollno match person as student
            else:
                a=False
        else:
            a=False #rollno unmatch
    return a




# def verification(Name,number):
    
#     if student_verification(Name,number)==True:
#         return True
#     elif teacher_verification(Name,number)==True:
#         return True
#     else:
#         return False

# def student_or_teacher_verification(Name,number):
#     if teacher_verification(Name,number)==True:
#         return "Teacher"
#     elif student_verification(Name,number):
#         return "Student"
#     else:
#         return None
    

        
            


