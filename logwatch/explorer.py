from logwatch import lire_log

sample_logs, ignorees = lire_log("sample-logs.log")
dix_echecs, ignorees2 = lire_log("dix-echecs.log")

print(f"Nombre de lignes lues : {len(sample_logs)}")
print(f"et nombre de lignes ignorees : {ignorees}")

print(f"Nombre de lignes lues parmi les dix échecs : {len(dix_echecs)}")
print(f"et nombre de lignes ignorees parmi les dix échecs : {ignorees2}")
#D2 réagit à partir de 11 échecs, c'est la comparaison entre le seuil et le nombre d'échecs par ip qui le décide


"""Compte le nombre de requetes par famille de code de réponse"""
compteur  = {}
for log in sample_logs:
  status = str(log["statut"])[0] + "xx"  # Regroupe les codes par famille (2xx, 3xx, 4xx, 5xx)
  compteur[status] = compteur.get(status, 0) + 1

print(compteur)
print(sum(compteur.values()))  # Devrait correspondre au nombre total de lignes lues

compteur2  = {}
for log in sample_logs:
  adresseIp = log["ip"]  
  compteur2[adresseIp] = compteur2.get(adresseIp, 0) + 1
print(compteur2)
print(sum(compteur2.values()))  # Devrait correspondre au nombre total de lignes lues

compteur3  = {}
for log in sample_logs:
  if log["methode"] == "POST" and log["url"] == "/login" and log["statut"] in (401, 403):  
    adresseIp = log["ip"]  # Regroupe les codes par famille (2xx, 3xx, 4xx, 5xx)
    compteur3[adresseIp] = compteur3.get(adresseIp, 0) + 1
print(compteur3)
print(sum(compteur3.values()))
print(sample_logs[0].keys())



par_minute = {}
for log in sample_logs:
    minute = log["date"][:17]
    par_minute[minute] = par_minute.get(minute, 0) + 1
minute_max = None
for minute, n in par_minute.items():
    if minute_max is None or n > par_minute[minute_max]:
        minute_max = minute
print(f"Minute la plus chargée : {minute_max} avec {par_minute[minute_max]} requêtes")
somme_totale = sum(par_minute.values())
print(f"Vérification : somme des minutes ({somme_totale}) = total des requêtes lues ({len(sample_logs)})")

fenetre_minutes = 5
par_fenetre = {}

for log in sample_logs:
    date_minute = log["date"][:17]
    m = int(date_minute[-2:])
    debut = m - (m % fenetre_minutes)
    cle_fenetre = f"{date_minute[:15]}{debut:02d}"
    par_fenetre[cle_fenetre] = par_fenetre.get(cle_fenetre, 0) + 1
    fenetre_max = None
for fenetre, n in par_fenetre.items():
    if fenetre_max is None or n > par_fenetre[fenetre_max]:
        fenetre_max = fenetre

print(f"Fenêtre la plus chargée : {fenetre_max} avec {par_fenetre[fenetre_max]} requêtes")

somme_requetes = sum(par_minute.values())
nombre_de_minutes = len(par_minute)

charge_calculee = somme_requetes / nombre_de_minutes

print(f"Charge calculée : {round(charge_calculee, 1)}")


def part_5xx(compteur):
  """Part des reponses 5xx sur l'ensemble des requetes lues (fraction entre 0 et 1)"""
  total = sum(compteur.values())
  return compteur.get("5xx", 0) / total if total else 0.0


SEUIL_README = 0.05  # README : seuil_5xx = 0.05 (5 %)
print(f"Part des 5xx : {part_5xx(compteur):.1%} (seuil README : {SEUIL_README:.1%})")