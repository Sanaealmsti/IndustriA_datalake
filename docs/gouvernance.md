
# Politique de gouvernance — IndustriA

## Contexte

Ce document définit les règles d'accès, de responsabilité et de cycle de vie des données du data lake IndustriA, conçu pour alimenter un futur modèle de maintenance prédictive sur 5 lignes de production instrumentées de capteurs

## Organisation des équipes métier

Excellence Industrielle est responsable des lignes de production stables
Qualité et Continuité de Production est responsable des lignes turbulentes et à pics
Ingénierie des Procédés est responsable de la ligne variable
Gouvernance des Données assure la supervision transversale du data lake et la validation avant passage en curated

## Propriétaires des données dans OpenMetadata

Le service minio-industriA ainsi que les buckets raw, staging, curated et archive sont sous la responsabilité du data-steward rattaché à l'équipe Gouvernance des Données
LineA est gérée par chef-ligne-a de l'équipe Excellence Industrielle
LineB, LineC et LineD sont gérées par chef-ligne-bcd de l'équipe Qualité et Continuité de Production
LineE est gérée par ingenieur-process de l'équipe Ingénierie des Procédés

## Comptes de service MinIO

Les comptes de service MinIO sont des comptes techniques d'accès au stockage objet, distincts des utilisateurs métier OpenMetadata
dataanalyst dispose d'un accès en lecture seule sur curated et est utilisé par les data scientists en consultation
Le dataengineer dispose d'un accès en lecture et écriture sur raw, staging et curated et est utilisé par les pipelines d'ingestion et de transformation
L'admin dispose de tous les droits sur tous les buckets et est réservé à l'administration technique

## Conditions d'accès

Le data analyst ne peut accéder à curated qu'après validation du data-steward
Le data engineer ne peut écrire sur raw et staging que dans le cadre des pipelines automatisés
Le rôle admin est réservé à l'équipe Gouvernance des Données
Tout accès aux données de production doit être tracé via les logs MinIO

## Niveaux de criticité

raw est classé Tier 1 car il constitue la source initiale et contient des données brutes irremplaçables
curated est classé Tier 1 car il contient les données d'entraînement pour le modèle de maintenance prédictive
staging est classé Tier 2 car les données transformées sont reconstructibles depuis raw
archive est classé Tier 3 car il contient des données expirées conservées pour audit

## Cycle de vie des données

Les buckets raw, staging et curated sont soumis à une suppression automatique après 730 jours via règle ILM MinIO
Le bucket archive est conservé indéfiniment pour audit et conformité réglementaire
Le déplacement vers archive se fait manuellement ou via un pipeline Airflow dédié
