import copy

dict_of_items_1 = {
    "env" : "dev",
    "server" : "linux2 AWS",
    "ram" : 8096,
    "CPU" : 4,
    "Active" : False
}
dict_of_items_2 = {
    "env" : "Azure",
    "server" : "linux2 Azure",
    "ram" : 10296,
    "CPU" : 8,
    "Active" : True
}
dict_of_items_3 = {
    "env" : "GCP",
    "server" : "linux2 GCP",
    "ram" : 102961,
    "CPU" : 12,
    "Active" : True
}
dict_of_items_4 = {
    "env" : "xyz",
    "server" : "linux2 xyz",
    "ram" : 1029612,
    "CPU" : 16,
    "Active" : False
}
dict_of_items_5 = {
    "env" : "xyz",
    "server" : "linux2 xyz",
    "ram" : 1029612,
    "CPU" : 16,
    "Active" : False
}
dict_of_items_6 = {
    "env" : "xyz",
    "server" : "linux2 xyz",
    "ram" : 1029612,
    "CPU" : 16,
    "Active" : False
}
dict_of_items_7 = {
    "env" : "xyz",
    "server" : "linux2 xyz",
    "ram" : 1029612,
    "CPU" : 16,
    "Active" : False
}


Env_items = [dict_of_items_1,dict_of_items_2]
Env_items_1 = [dict_of_items_3,dict_of_items_4,dict_of_items_5,dict_of_items_6,dict_of_items_7]

print("Created element item list :",Env_items_1)

#pop function work here for remove elements
Env_items_1.pop(3
)
print("pop function work here:",Env_items_1)


# how to insert function work only string
print("insert function work here")
Env_items_1.insert(1,dict_of_items_4)

# how to extend function work
Env_items_1.extend(Env_items) 
print("This is extend function works : ",Env_items_1)

# how index work to find element on which pocition
print("To find index value :",Env_items.index(dict_of_items_2))

# How copy function works with import copy
Env_items_copy = copy.copy(Env_items)
print("item copy : ", Env_items_copy)

# how count function work, its only work for string
Str_value = "hello python to python"
str_len = len(Str_value)
str_count = Str_value.count("python")
print("String count :",str_count)
print("string len:",str_len)

# how append fuction work
Env_items.append(dict_of_items_4)

for i in Env_items:
    for Key,Value in i.items():
        if Key == "Active" and Value == False:
            print(i.values())

print(dir(Env_items))


# list example

if dict_of_items_1.get("Active"):
    print(dict_of_items_1.get("env"))
else:
    print("Activation is not True")


