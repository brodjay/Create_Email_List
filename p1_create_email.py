# Combine list of names with domain name. 
# v5 - Check if output file exists. If so, append "_x" where x is a number. 
# Fixed - Added output message to console displaying new list. 
# Fixed - First option to create email list created seperate emails with first and last names instead of just first.

from os.path import exists

#Choice of naming convention
def email_naming_convention():
    naming_conv = input("Pick your naming convention. \n 1.john@acme.com \n 2.jsmith@acme.com. \n\n Select a number: ")
    print()
    if naming_conv == "1" or "2":
        return naming_conv
    else: 
        print("This is not a choice. Please try again.")
        email_naming_convention()

#Ask user for filename and create username based on naming convention from user input.
def name_file():
    success = False
    while not success:        
        try:
            filename= input("Enter filename: ")
            with open(filename, "r") as file:
                name_list = file.readlines()
                success = True
        except: 
            print("File not found! Try again.")

    naming_conv = email_naming_convention()

    first_names =  []
    firstInitial_lastname = []    

    if naming_conv == "1":        
        for fullname in name_list:
            name_split = fullname.split()
            for i, name in enumerate(name_split):
                if name == name_split[0]:
                    first_names.append(name.lower())
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

# Ask user for the domain.
email_domain= input("Enter the domain: ")

# Create new email list and convert to string for file export .
def create_list(names, domain):
    new_list = []
    for name in names:
        new_list.append(name + "@" + domain) 
    new_list_str = "\n".join(new_list)
    print("Your new email list: \n\n{}".format(new_list_str).strip())
    return new_list_str

# Export to file. Creates a file_x file where "x" is a number not in the folder starting at 1 if original file created.
def export_file(list):
    if not exists("new_email_list.txt"):
        with open("new_email_list.txt", "w") as file:
            file.writelines(list)
    elif exists("new_email_list.txt"):
        count = 1
        isRunning = 0
        while isRunning == 0:
            if not exists("new_email_list" + "_" + str(count) + ".txt"):                
                with open("new_email_list" + "_" + str(count) + ".txt", "w") as file:
                  file.writelines(list)
                isRunning = 1
            elif exists("new_email_list" + "_" + str(count) + ".txt"):
                count += 1
    return        

# Main function that combines names with domain and exports to a new file.
def create_email(names, domain):    
    new_list_str = create_list(names, domain)
    export_file(new_list_str)

# Function Call
create_email(name_file(), email_domain)