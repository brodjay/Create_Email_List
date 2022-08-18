def new_domain(email_list, new_domain):
    new_list = []
    count = 0
    for name in email_list:
        try:
            index = name.index("@") + 1
            new_list.append(name[:index] + new_domain)
        except ValueError:
            count += 1 # Counts if any emails caused an error because "@" was missing.
    
    print("\nEmails missing '@' skipped: {}.\n".format(count))

    new_domain_list = "\n".join(new_list)    
    return new_domain_list


