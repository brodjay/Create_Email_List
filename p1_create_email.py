# Combine list of names with domain name. 
# v6 - Update Existing email list with new domain
# Feature - Added option to update an existing email list to a new domain. External module - feat_new_domain.py
# Refactored some variables and create_email().

from os.path import exists
from feat_new_domain import new_domain

#Choice to create new email from username list (1) or update domain from existing email list.
def option():
    choice = input("Select your option: \n\n1. Create a new email from an existing username list.\n2. Update the domain of an existing email list.\n\nSelect a number: ")
    
    if choice == "1" or choice == "2":
        return choice
    else: 
        print("Sorry that is not a choice. Please select 1 or 2.")
        option()

#Choice of naming convention
def email_naming_convention():
    naming_conv = input("\nPick your naming convention. \n 1.john@acme.com \n 2.jsmith@acme.com \n\n Select a number: ")
    if naming_conv == "1" or "2":
        return naming_conv
    else: 
        print("This is not a valid option. Please try again.")
        email_naming_convention()

#Ask user for filename.
def filename():
    success = False
    while not success:        
        try:
            filename= input("Enter filename: ")
            with open(filename, "r") as file:
                open_file = file.readlines()
                success = True
            return open_file
        except: 
            print("File not found! Try again.")

# Ask user for the domain.
def email_domain():
    email_domain= input("Enter the domain: ")
    return email_domain

# Create username list based on naming convention selection.

def naming_convention(name_list):
    naming_conv = email_naming_convention()

    first_names =  []
    firstInitial_lastname = []    

    if naming_conv == "1":        
        for fullname in name_list:            
            name_split = fullname.split()            
            for i, name in enumerate(name_split):
                if name == name_split[0]:
                    first_names.append(name.lower())
                    print(first_names)
        return first_names
    else:        
        for fullname in name_list:
            new_name = ""
            name_split = fullname.split()
            for i, name in enumerate(name_split):                
                if name == name_split[0]:
                    new_name += name[0].lower()
                else: 
                   new_name += name.lower()    
            firstInitial_lastname.append(new_name)            
        return firstInitial_lastname

# Create new email list and convert to string for file export .
def create_list(names, domain):
    new_list = []
    for name in names:
        new_list.append(name + "@" + domain) 
    new_list_str = "\n".join(new_list)
    print("Your new email list: \n\n{}".format(new_list_str).strip())
    return new_list_str

# Ask for new filename.
def name_file():
    name_of_file = input("What do you want to name your new list? This will be exported as a .txt file: ")
    if " " in name_of_file:
        name_of_file = name_of_file.replace(" ", "_")
    return name_of_file

# Export to file. Creates a file_x file where "x" is a number not in the folder starting at 1 if original file created.
def export_file(list, new_file_name):
    if not exists(new_file_name + ".txt"):
        with open(new_file_name + ".txt", "w") as file:
            file.writelines(list)
    elif exists(new_file_name + ".txt"):
        count = 1
        isRunning = 0
        while isRunning == 0:
            if not exists(new_file_name + "_" + str(count) + ".txt"):                
                with open(new_file_name + "_" + str(count) + ".txt", "w") as file:
                  file.writelines(list)
                isRunning = 1
            elif exists(new_file_name + "_" + str(count) + ".txt"):
                count += 1
    return        

# Main function.
def create_email(option):
    file = filename()
    domain = email_domain()
    export_name = name_file()
    if option == "1":
        name_list = naming_convention(file)
        new_list_str = create_list(name_list, domain)
    else:
        new_list_str = new_domain(file, domain)

    export_file(new_list_str, export_name)

#Function Call
create_email(option())