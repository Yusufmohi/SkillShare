def print_list(lst):
    for string in lst:
        print(string)

def print_gt3(lst):
    for numbers in lst:
        if numbers>3:
            print("True")
        else:
            print("False")

def print_c_name(names):
    for name in names:
        if name.startswith("C"):
            print(name)

def get_nme(names):#it only return the first name that starts with "C"
    for name in names:
        if name.startswith("C"):
            return name
    
