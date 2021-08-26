import re

#file_load
def file_read():
    f = open("credentials.txt", "r")
    credentials=f.read().split("\n")
    f.close()
    return credentials

#file write
def file_write(username,password):
    f = open("credentials.txt", "a")
    f.write("\n"+username+"\n")
    f.write(password)
    f.close()
    
#registration
def registration():
    username=input("Enter the username\n")
    r=re.compile("^[a-z]{1}[a-zA-Z0-9_+-]{0,}@{1}[a-zA-Z0-9]{1,}.{1}[a-z]{1,}$")
    t1=re.match(r, username)
    if t1:
        if not chech_username(username):
            password=input("Enter the password\n")
            password_reg=re.compile(r'''((?=.* [A-Z])(?=.* [0-9])(?=.* [a-z])(?=.* [+-/\*$#@!]).{5,16})''',re.VERBOSE)
            t2=re.match(password_reg, password)
            if t2:
                file_write(username,password)
                print("Registered Successfully")
            else:
                print("Please strong password")
        else:
            print("username already exists")
    else:
        print("invalid email format")
    main_func()
    
#forgot password
def forgot_password():
    username=input("Enter the username\n")
    credentials=file_read()
    for i in range(0,len(credentials),2):
        if credentials[i]==username:
            print("Your password: "+credentials[i+1])
            main_func()
    print("Your username does not exists")
    main_func()
    
#check wheather use already exists or not
def chech_username(username):
    credentials=file_read()
    for i in range(0,len(credentials),2):
        if credentials[i]==username:
            return 1
    return 0
def check_user(username,password):
    credentials=file_read()
    for i in range(0,len(credentials),2):
        if credentials[i]==username and credentials[i+1]==password:
            return 1
    return 0

#login
def login():
    username=input("Enter the username\n")
    password=input("Enter the password\n")
    if check_user(username,password):
            print("login success")
    else:
        print("Invalid username and password please register")
        main_func()

def main_func():
    n=int(input("Choose any one option to proceed\nPress 1 for Login\nPress 2 for Registration\nPress 3 for Forgot password"))
    if n==1:
        login()
    elif n==2:
        registration()
    elif n==3:
        forgot_password()
    else:
        print("exit, thank you")
main_func()