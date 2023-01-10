import os
import string 
import random 

# password generator
def password_generator():

    #counter = 0
    while True:
        N = 15
        accepted_chars = ["&" "%" "@" "!" "#" "*" "^"]
        password = ''.join(random.choices(str(accepted_chars[:]) + string.ascii_lowercase + string.ascii_uppercase + string.digits, k = N))
        print(password)

        another_pass = input("\nDo you want another password?(y/n) ")

        if another_pass == 'y':
            #counter += 1
            continue
        elif another_pass == 'n':
            do_you_want_to_save(password)
            break
        else:
            print("\nError, try again.")
            continue


#save pass process
def save_pass_to_file(name,path,passw):

    save_to = os.path.join(path,name) + ".txt"

    while True:
        if not os.path.exists(save_to):
            print("\nCreating now...")

            with open(save_to, "x") as save_to:
                save_to.write(passw)
            verify = str(os.path.join(path,name) + ".txt")
            print(f"\nYour password has been saved. \n\nYou can view it here: {verify}")
            break
        else:
            overwrite_warning(save_to,name,passw,path)
            break



#overwrite file function
def overwrite_file(file,name,content,path):
    print("Overwriting file now...")
    os.remove(file)
    #print(file)
    save_pass_to_file(name,path,content)
    


#file overwrite warning message
def overwrite_warning(failed_file_path,pass_name,file_content,directory):
    overwrite_warning = input("A file already exists with this name. Overwrite?(y/n) ")
                
    if overwrite_warning == "y":
        #print("test pass for yes")
        overwrite_file(failed_file_path,pass_name,file_content,directory)

    elif overwrite_warning == "n":
        #print("test pass for no")
        restart = input("Change the file name or quit?(y/n) ")
        if restart == "y":
            new_name = input("Type a new file name here: ")
            # new_path = input("Please resubmit the path: ")
            save_pass_to_file(new_name,directory,file_content)

    else:
        print("Error, incorrect input. Try again...")
        overwrite_warning()


# do you want to save the password?
def do_you_want_to_save(passw): 

    while True:
        save_answer = input("\nDo you want to save this pass?(y/n) ")   
        
        if save_answer == "y":
            print("\nGot it.")
            pass_name = input("\nWhat do you want to name this password? " )
            filepath = input("\nWhere do you want to save this? ")
            save_pass_to_file(pass_name,filepath,passw)
            break
        elif save_answer == "n":
            print("\nSee ya later!")
            break
        else:
            print("\nError, incorrect input. Try again.")
        

#start script
password_generator()



