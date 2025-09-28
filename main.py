from Data import *
from books import *
from users import *

print(utilisateurs)
print(aime_livres)
print(livres)
print("-"*220)

print(SortingData(livres))
Ancien(livres)
Récent(livres)
CreationDict(aime_livres)
PaginationList(utilisateurs)

print(UsersMaj(utilisateurs))
print(NamesMAj(utilisateurs))
DictUsers(utilisateurs,aime_livres)
RésumeUsers(utilisateurs,aime_livres)