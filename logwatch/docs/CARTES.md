# docs/CARTE.md -- gabarit de départ, amendé à l'étape 4

# Carte LogWatch v0 - v1 du AAAA-MM-JJ (étape 1)

## Entrées et sorties

lit : ... (et qui décide du chemin : l'option, .env, ou la valeur par
défaut)
écrit : ...
supprime : ...

## Les fonctions, dans l'ordre du fichier

Les quatorze lignes se generent, depuis logwatch/ :
Select-String -Path logwatch.py -Pattern '^def ' |
ForEach-Object { "| " + $\_.Line.Substring(4).TrimEnd(':') + " | |" }
Coller le resultat sous l'en-tete, puis remplir la seule colonne rend.
| fonction | rend
|
|-----------------------------------|---------------------------------------
--------|
| charger_env(chemin=".env") | Lit un fichier .env (CLE=valeur) et pose les variables absentes de l'environnement.|
|
| parser_ligne(ligne) | un dictionnaire à onze clés, ou None
si la ligne n'a pas la forme attendue |
|
| charger_config(chemin) | Rend les seuils : les defauts, ecrases par le contenu de config.json s'il existe. |
|
|lire_log(chemin, encodage="utf-8") | Lit le fichier et rend (entrees parsees, nombre de lignes ignorees).|
|
|anonymiser_ip(ip) | Masque le dernier octet d'une IPv4 : 203.0.113.7 -> 203.0.113.x (RGPD).|
|
|analyser(entrees, config) | Applique toutes les detections et rend le corps du rapport.|
|
|ecrire_rapport(rapport, dossier) | Ecrit le rapport JSON date dans le dossier et rend son chemin.|
|
|main(argv=None) | Programme principal|
|

## Les détections annoncées par le README (question 7)

| détection | fonction | ce que le README lui demande (seuil, unité, « dès
que » / « au moins » / « au-delà ») |
|-----------|----------|----------------------------------------------------
--------------------------------|
| D1 | d1_requetes_par_ip(entrees, top_ips) | nombre de requetes par IP, les top_ips plus actives en tete, et la somme de toutes. |
|
| D2 | d2_brute_force(entrees, url_login, seuil) | IPs qui enchainent les echecs de connexion (POST url_login en 401/403). |
|
| D3 | d3_scan(entrees, seuil) | IPs qui sondent des URLs typiques d'un scan de vulnerabilites |
|
| D4 | d4_pic_trafic(entrees, seuil_pic, fenetre_minutes) | pic de trafic : plus de seuil_pic requetes dans une fenetre de fenetre_minutes minutes. |
|
| D5 | d5_erreurs_5xx(entrees, seuil) | part des reponses en erreur serveur (5xx) sur l'ensemble des requetes. |
|
| D6 | d6_purger_rapports(dossier, retention_jours) | supprime les rapports plus vieux que la retention (RGPD : les rapports contiennent des IP). |
|

## Points opaques (question 8)

- ligne NN : que vaut ... quand ... ?
- ligne 81, 82, 83 : syntaxe inconnue : e["statut"] = int(e["statut"])
- ligne 69 : utilisation du with -> incoonnue
