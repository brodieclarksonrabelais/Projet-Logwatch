from logwatch import lire_log, d1_requetes_par_ip

entrees, ignorees = lire_log("sample-logs.log")
print(f"{len(entrees)} entrees lues, {ignorees} ignorees")

compteur = {}
for log in entrees:
    statut = str(log["statut"])[0] + "xx"
    compteur[statut] = compteur.get(statut, 0) + 1

compteur2 = {}
for log in entrees:
    ip = log["ip"]
    compteur2[ip] = compteur2.get(ip, 0) + 1


print(sum(compteur.values()))

print(compteur2)
print(sum(compteur2.values()))
print(f"L'écart est de {sum(compteur2.values()) - d1_requetes_par_ip(entrees, 1)['somme'] -ignorees} -"
       f" D1: {d1_requetes_par_ip(entrees, 1)['somme']}/ somme IP: {sum(compteur2.values())} / ignorees: {ignorees}")





