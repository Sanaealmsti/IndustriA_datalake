# Architecture du Data Lake — IndustriA

Les données des 5 lignes ont des schémas hétérogènes (casse des colonnes différente,
champ elapsed_time absent sur certaines lignes). Sans une architecture en couches,
un data scientist qui travaille sur ces données obtiendrait des erreurs ou des
résultats inexplicables. Les couches de données résouent ce problème en harmonisant
tous les schémas avant toute analyse.

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
