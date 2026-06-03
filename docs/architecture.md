# Architecture du Data Lake — IndustriA

valeurs manquantes traitees. Pret pour lanalyse exploratoire.



**Curated**

Donnees agregees et enrichies, directement utilisables par les data scientists

pour entrainer un modele de maintenance predictive.



**Archive**

Donnees de plus de 180 jours, conservees pour audit et conformite.

Suppression automatique apres 2 ans via les regles ILM de MinIO.



## Justification



Les donnees des 5 lignes ont des schemas heterogenes (casse des colonnes differente,

champ elapsed_time absent sur certaines lignes). Sans une architecture en couches,

un data scientist qui travaille sur ces donnees obtiendrait des erreurs ou des

resultats inexplicables. La couche staging resout ce probleme en harmonisant

tous les schemas avant toute analyse.

## Structure des buckets MinIO

raw/
    production_lines/
        lineA/year=2025/month=05/
        lineB/year=2025/month=04/
        lineC/year=2025/month=03/
        lineD/year=2025/month=02/
        lineE/year=2025/month=01/

staging/
    production_lines/

curated/
    production_lines/

archive/
    production_lines/
