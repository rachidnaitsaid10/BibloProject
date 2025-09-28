from Data import *

print(utilisateurs)
print(aime_livres)
print(livres)
print("-"*220)

def SortingData(Mylist):
    Mylist.sort(key=lambda x: x["année"])
    return Mylist
    print("-" * 220)
print(SortingData(livres))


def Ancien(Mylist):
    SotoringList = SortingData(Mylist)
    AncienLiver = SotoringList[0]
    print(AncienLiver)
    print("-" * 220)
Ancien(livres)

def Récent(Mylist):
    SotoringList = SortingData(Mylist)
    RécentLiver = SotoringList[-1]
    print(RécentLiver)
    print("-" * 220)
Récent(livres)

