# Combine list of names with domain name. v3 - Choice between firstName@domain.com or firstInitial_LastName@domain.com

#Choice of naming convention
def email_naming_convention():
    naming_conv = input("Pick your naming convention. \n 1.john@acme.com \n 2.jsmith@acme.com. \n\n Select a number: ")
    if naming_conv == "1" or "2":
        return naming_conv
    else: 
        print("This is not a choice. Please try again.")
        email_naming_convention()

#Ask user for filename and create username naming convention from user input.
def name_file():
    filename= input("Enter filename: ")
    with open(filename, "r") as file:
        name_list = file.readlines()  

    naming_conv = email_naming_convention()

    first_names =  []
    firstInitial_lastname = []    

    if naming_conv == "1":        
        for fullname in name_list:
            name_split = fullname.split()
            for i, name in enumerate(name_split):
                if name[0]:
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

# Main function that combines names with domain.
def create_email(names, domain):    
    new_list = []
    for name in names:
        new_list.append(name + "@" + domain)
    print(new_list)
    return new_list

create_email(name_file(), email_domain)