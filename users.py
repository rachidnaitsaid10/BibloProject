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
    users_dict = {user[0]: (f"{user[2]} {user[1]}".upper(), user[3]) for user in utilisateurs}
    print(users_dict)

    livres_par_utilisateur = {}
    for user_id, livre in aime_livres:
        if user_id in users_dict:
            nom_complet, age = users_dict[user_id]
            if nom_complet not in livres_par_utilisateur:
                livres_par_utilisateur[nom_complet] = []
            livres_par_utilisateur[nom_complet].append(livre)
    print(livres_par_utilisateur)

    for nom_complet, age in users_dict.values():
        if nom_complet in livres_par_utilisateur:
            livres_str = "', '".join(livres_par_utilisateur[nom_complet])
            print(f"{nom_complet} ({age} ans) aime : '{livres_str}'")
        else:
            print(f"{nom_complet} ({age} ans) n'aime aucun livre")

RésumeUsers(utilisateurs,aime_livres)
print("-"*220)



