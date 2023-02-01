print("##########################################################################################################")
print("This is just for fun!, we are still encrypting the passwords!, Do not use for actual storing of passwords!")
print("##########################################################################################################")

# manual encrypt is possible, but here we are using module
# pip install cryptography using terminal/CLI
# Fernet module allow you to encrypt
from cryptography.fernet import Fernet
# master_pwd = input("What is the master password? ")


# key + password + text to encrypt = random text
# random text + key + password = text to encrypt
# mode wb - write in bytes
# commented to use only once

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
        
# write_key()

# mode rb - read in bytes
def load_key():
   file = open("key.key", "rb")
   key = file.read()
   file.close()
   return key

key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # rstrip is specif to remove, even strip works
            data = line.rstrip()
            # explanation for below spilt function
            # if we have data like "hello|tim|yes|2|7"
            # the data is split into list like ["hello","tim","yes","2","7"]
            # here we are adding name and pswd which will be assigned to user, passw. 
            # If you want to have extra input asdd new variable to assign same.
            # encode() turns the string into bytes or '.bytes' also should work
            # decode() is exactly opposite of encode()
            user, passw =  data.split("|")
            # print("User:", user, "| Password:", passw)
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pwd = input("Password: ")
    
    # using with the file closes automatically 
    # using file = open(.......) need to close manually
    # r - read mode
    # w - write mode
    # a - append mode, if file exists adds, otherwise creates new file
    with open('passwords.txt', 'a') as f:
        # f.write(name + "|" + pwd)
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    
while True:
    mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Type the correct mode to proceed! ")
        continue