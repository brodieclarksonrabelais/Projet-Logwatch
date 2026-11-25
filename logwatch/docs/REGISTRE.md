# docs/REGISTRE.md -- ouvert à l'étape 2, complété aux étapes 3 et 4,

arrêté à l'étape 5, fermé ligne à ligne à l'étape 6

# Registre des défauts LogWatch - N défaut(s) ouvert(s) au AAAA-MM-JJ

| n° | date | symptôme observé
| fonction suspectée | état |
|----|------------|---------------------------------------------------------
--|--------------------|--------|
| B1 | 2026-09-30 | test_d1_somme_egale_total_lines rouge : attendu 6, reçu
3 | d1_requetes_par_ip | fermé 2026-09-30 |
| B2 | 2026-09-30 | test_d3_ignore_url_legitime rouge : attendu [], reçu [{'ip': '10.0...': 'moyenne'}]
| d3_scan | fermé 2026-09-30 |
| B3 | 2026-11-18 | D6 ne prend pas en compte les logs vieillis manuellement | d6_purger_rapports |--------|

## B1 - <le symptôme, en cinq mots>

Test en échec : test_d1_somme_egale_total_lines
Attendu / reçu : 6 / 3
Fonction visée : d1_requetes_par_ip, ligne 120
Cause racine : On ne doit pas vérifier le statut des requêtes en entrées
Correction prévue : commenter la ligne
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-09-30
Vérifié par : <Brodie>, sur <le cas éprouvé, différent de celui du
test>

## B2 - <le symptôme, en cinq mots>

Test en échec : test_d3_ignore_url_legitime
Attendu / reçu : [] / [{'ip': '10.0...': 'moyenne'}]
Fonction visée : d3_scan, ligne 151
Cause racine : Dans motif scan on trouve l'objet admin qui pose problème quand ona des url administratifs
Correction prévue : retirer /admin de motifs scan
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-09-30
Vérifié par : <Brodie>, sur <le cas éprouvé, différent de celui du
test>

## B3 - <Pic de trafic non détecté et paramètre de fenêtre ignoré>

Test en échec : aucun
Attendu / reçu : alerte=True / alerte=False
Fonction visée : d4*pic_trafic, ligne de retour
Cause racine : Le paramètre `fenetre_minutes` de la signature n'est pas utilisé dans la fonction (le découpage est fait fixement minute par minute). De plus, pour déclencher l'alerte, la fonction compare la \_moyenne* globale de toutes les minutes au seuil (`charge = statistics.mean(...)`), au lieu de comparer la valeur de la fenêtre la plus chargée.
Correction prévue : Découper les requêtes par tranches en appliquant un modulo avec `fenetre_minutes`, et corriger la condition d'alerte pour vérifier si la fenêtre maximale dépasse le `seuil_pic` (`maxi > seuil_pic`).
(étape 6) Correctif : commit <hash>, <auteur>, le 19/10/2026
Vérifié par : <Brodie>

## B4 - Valeur incohérente du seuil d'erreurs 5xx (D5)

Test en échec : N/A (constaté manuellement via explorer.py)
Attendu / reçu : pas d'alerte | alerte
Fonction visée : DEFAUTS ligne 28
Cause racine : seuil_5xx à 0.5 au lieu de 0.05
Correction prévue : 0.5 à la place de 0.05 .
(étape 6) Correctif : commit <hash>, <auteur>, le 04/11/2026
Vérifié par : <Brodie>

## B5 - Le seuil brute-force (D2) ne réagit pas à la valeur exacte

Test en échec : aucun
Attendu / reçu : Au passage de dix-echecs.log (10 échecs), la ligne D2 affiche 0 IP(s). L'alerte ne se déclenche qu'à partir de 11 échecs.
Fonction visée : d2_brute_force[cite: 5] Cause racine : La comparaison dans le code utilise un opérateur strictement supérieur (if n > seuil:)[cite: 5] au lieu d'un opérateur supérieur ou égal.
Correction prévue : if n >= seuil: à la place de if n > seuil:.
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-18-11
Vérifié par : <Brodie>, sur <le cas éprouvé, différent de celui du
test>

## B6 - <le symptôme, en cinq mots>

Test en échec : pas de test pour cette fonction
Attendu / reçu : D6 rapports purges: 1 / D6 rapports purges: 0
Fonction visée : d6_purger_rapports, ligne 188
Cause racine : limite_jours = retention_jours x 30 => limite_jours = 210 jours au lieu de 7 jours
Correction prévue : limite_jours = retention_jours
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-11-25
Vérifié par : <Brodie>, sur <le cas éprouvé, différent de celui du
test>
