# Combine list of names with domain name. v1 - import from list.

name_list= ["Jason", "Jeffrey", "Jennifer", "Debra", "Chelsea"]
email_domain= input("Enter the domain: ")

def create_email(names, domain):
    new_list = []
    for name in names:
        new_list.append(name + "@" + domain)
    print(new_list)
    return new_list

create_email(name_list, email_domain)