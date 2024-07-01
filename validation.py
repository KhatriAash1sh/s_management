from file_read_write import read

def email_validation(email):
    for i in email:
        if i=="@":
           if i==".":
               return True
           else: 
               a=False
        else:
            a=False
    return a

def phone_validation(phone):
    phone=str(phone)
    if len(phone)==10:
        return True
    else:
        return False
    
# def check_validation_email(email):
#     if email_validation(email)==True:
#          print("valid email.",email)
#     else:
#         print("invalide email.",email)

# check_validation_email("aashis5657@gmail.com")

# def check_validation_phone(phone):
#     if phone_validation(phone)==True:
#         print("valid phone no.",phone)
#     else:
#         print("invalide phone no.",phone)

def roll_or_id_unique_validation(number,status):
    dict1=read()
    if status=="Teacher":
        for i in dict1:
            if i.get("status")=="Teacher":
                if i.get("id")==number:
                    return False
                else:
                    pass
        return True

    elif status=="Student":
        for i in dict1:
            if i.get("status")=="Student":
                if i.get("rollno")==number:
                    return False
                else: 
                    pass
        return True
    else:
        pass


# if roll_or_id_unique_validation(10,"Teacher")==True:
#     print("You can take")
# else:
#     print("Already taken")