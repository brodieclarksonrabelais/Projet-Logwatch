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
Vérifié par : <personne>, sur <le cas éprouvé, différent de celui du
test>

## B2 - <le symptôme, en cinq mots>

Test en échec : test_d3_ignore_url_legitime
Attendu / reçu : [] / [{'ip': '10.0...': 'moyenne'}]
Fonction visée : d3_scan, ligne 151
Cause racine : Dans motif scan on trouve l'objet admin qui pose problème quand ona des url administratifs
Correction prévue : retirer /admin de motifs scan
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-09-30
Vérifié par : <personne>, sur <le cas éprouvé, différent de celui du
test>

## B3 - <le symptôme, en cinq mots>

Test en échec : pas de test pour cette fonction
Attendu / reçu : D6 rapports purges: 1 / D6 rapports purges: 0
Fonction visée : d6_purger_rapports, ligne 151
Cause racine :
Correction prévue :
(étape 6) Correctif : commit <hash>, <Brodie>, le 2026-09-30
Vérifié par : <personne>, sur <le cas éprouvé, différent de celui du
test>
