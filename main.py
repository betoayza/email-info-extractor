import re

email = input("Enter some email: ")
email = re.sub("\.|\_|-", " ", email)
name = email[0: email.find("@")].split(" ")
list_name = list(name) 

for x in range(0, len(name)):
    list_name[x] = list_name[x].capitalize()

name = " ".join(list_name)
domain = email[email.find("@")+1:]
domain = domain[0: domain.find(" ")].capitalize()
domain_dict = {"Gmail": "Google", "Yahoo": "Yahoo", "Outlook": "Microsoft"}

if domain in domain_dict.keys():
    print("Hey,", name,"! I can see domain registered by", domain_dict[domain])
else:
    print("Hey,", name,"! I can see custom domain is", domain)



