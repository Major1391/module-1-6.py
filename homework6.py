my_dict = {"Mormozhev": 1991, "Smirnov": 2000, "Ivanov": 2002}
print(my_dict)
print(my_dict["Smirnov"])
print(my_dict.get("Kalina"))
my_dict.update({"Kiril": 2001,
                "Anton": 1987})
del my_dict["Mormozhev"]
print(my_dict.get("Mormozhev"))
print(my_dict)


#                                   Множества
my_set = {1,1,2,2,3,3}
print(my_set)
my_set.add(7)
my_set.add(8)
print(my_set)
my_set.discard(7)
print(my_set)