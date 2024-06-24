def gt5(x):
    if(x>5):
        return "super da"
    else:
        return "kashtam"
def reaction(x):
    if(x=="among us"):
        return "correct bro"
def bojack(lst):
    if sum(lst)<21:
        return sum(lst)
    else:
        return "noo"
def can_cook(lst):
    if "lemon" in lst:
        return lst
    else:
        return []
def laugh(lst):
    if any(lst):# if True in lst:
        return "HeHe"
    else:
        return "Uhh"
def print_from_to(x,y):
    i=x
    while i<y:
        print(i)
        i += 1
        
