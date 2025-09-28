from Data import *

print(utilisateurs)
print(aime_livres)
print(livres)
print("-"*220)

def SortingData(Mylist):
    Mylist.sort(key=lambda x: x["année"])
    return Mylist
    print("-" * 220)



def Ancien(Mylist):
    SotoringList = SortingData(Mylist)
    AncienLiver = SotoringList[0]
    print("-" * 220)


def Récent(Mylist):
    SotoringList = SortingData(Mylist)
    RécentLiver = SotoringList[-1]
    print(RécentLiver)
    print("-" * 220)



def CreationDict(Mylist):
    dictionnaire = {}
    for item in Mylist:
        if item[1] not in dictionnaire:
            dictionnaire[item[1]] = 1
        else:
            dictionnaire[item[1]] += 1
    print(dictionnaire)
    print("-" * 220)


def PaginationList(Mylist):
    x=0
    while x < len(Mylist):
        print(f"Pagination {(x+2)//2}")
        print(Mylist[x])
        if x+1 < len(Mylist):
            print(Mylist[x+1])
        x += 2
    print("-" * 220)


