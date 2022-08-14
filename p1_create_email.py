# Combine list of names with domain name. v2 - import file

#Ask user for the filename.
def name_file():
    filename= input("Enter filename: ")
    with open(filename, "r") as file:
        name_list = file.readlines()
    first_names =  []
    for name in name_list:
        name_split = name.split()
        for i, name in enumerate(name_split):
            if name[0]:
                first_names.append(name)
    return first_names

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