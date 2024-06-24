range(10)
iter=list(range(10))
print(iter)
print(list("chinchu"))
for i in "chinchu":
    print(i,end="")


def check(password):
    has_number=False
    for i in password:
        if i.isdigit():
            has_number=True
    return has_number

password=input("Password: ")
has_number=check(password)
print(has_number)
    
