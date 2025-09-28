from Data import *

print(utilisateurs)
print(aime_livres)
print(livres)
print("*"*220)

def UsersMaj(Mylist):
    ListMaj=list(filter(lambda x : x[3]>18, Mylist))
    return ListMaj
print(UsersMaj(utilisateurs))
print("-"*220)

def NamesMAj(Mylist):
    ListNames=list(map(lambda x: f"{x[1].upper()} {x[2].upper()}", Mylist))
    return ListNames
print(NamesMAj(utilisateurs))
print("-"*220)

def DictUsers(MylistUsers,MylistAime):
    DictUsers = {}
    for x in MylistAime:
        for y in MylistUsers:
            if x[0] == y[0]:
                if y[2] + " " + y[ 1] in DictUsers:
                    DictUsers[y[2] + " " + y[1]] = DictUsers[y[2] + " " + y[1]] + (x[1],)
                else:
                    DictUsers[y[2] + " " + y[1]] = (x[1],)
    print(DictUsers)
DictUsers(utilisateurs,aime_livres)
print("-"*220)


def RésumeUsers(MylistUsers,MylistAime):
    DictUsers = {}
    for x in MylistAime:
        for y in MylistUsers:
            if x[0] == y[0]:
                age = y[3]
                name = y[2] + " " + y[ 1]
                DictUsers["name"] = name
                DictUsers["age"] = age
                if DictUsers["name"] in DictUsers:
                    DictUsers["books"] = DictUsers["books"] + (x[1],)
                else:
                    DictUsers["books"] = (x[1],)
        print(DictUsers)

RésumeUsers(utilisateurs,aime_livres)
print("-"*220)



