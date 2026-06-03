# Analyse des schémas — 5 lignes de production

## Diffèrences de colonnes

LineA : Temperature, pressure, elapsed_time (10 000 lignes)
LineB : temperature, pressure, Elapsed_time (5 000 lignes)
LineC : Temperature, pressure, pas de elapsed_time (5 000 lignes)
LineD : temperature, Pressure, pas de elapsed_time (5 000 lignes)
LineE : Temperature, pressure, pas de elapsed_time (5 000 lignes)

## Problèmes identifiés

La casse des colonnes est inconsistante entre les fichiers.
elapsed_time est absent sur LineC, LineD et LineE.
Si on concatene les fichiers sans nettoyage on obtient des erreurs.

## Ce qu'on va faire en Staging

Renommer toutes les colonnes en minuscules.
Ajouter elapsed_time a null quand il est absent.
Convertir timestamp en format datetime standard.
