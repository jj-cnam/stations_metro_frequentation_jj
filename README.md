---
title: Tableau de bord de la fréquentation des stations du métro parisien en 2025
author: Julien Jacquemmoz
---

> Requirement : openpyxl==3.1.3

> tree

L'objectif est d'étudier la fréquentation des stations de métro du métro parisien, à partir de données fournies par Île-de-France Mobilités [https://prim.iledefrance-mobilites.fr/fr], en les représentant sur un tableau de bord.

- Quelle est l'évolution selon le temps ?
- Quelles sont les différences de fréquentation entre les stations ?

On va s'appuyer sur les **données de validation sur le réseau ferré** : elles comptent pour chaque *station* (appelée *arrêt*) le nombre de valiations par jour, correspondant donc aux **entrées dans la station**, catégorisées par *type de titre de transport*.
Limites :
- pas de données sur les tickets sur support papier (support en extinction),
- évidemment pas de données sur les voyageurs n'ayant pas pu valider ou fraudeurs,
- pour les stations ayant eu entre 1 et 5 validations journalières pour un type de titre donnée, les données indiquent "MOINS DE 5".

# Données sources
## Jeu de données

[https://prim.iledefrance-mobilites.fr/]
Validations sur le réseau ferré en 2025
"Ce jeu de données présente le nombre de validations des voyageurs par jour par arrêt et par titre de transport sur le réseau ferré."
Licence : Licence ODbL Version Française [https://spdx.org/licenses/ODbL-1.0.html#licenseText] (spécifique aux bases de données)
Producteur : Île-de-France Mobilités
Documentation : [https://eu.ftp.opendatasoft.com/stif/Validations/Documentation/Donnees_de_validation.pdf]
La masse fait qu'elles sont séparées en quatre fichiers de données trimestrielles :

- 1er trimestre [https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-1er-trimestre]
	- Dernier traitement (données) : 23 juillet 2025 9:44
	- Dernier traitement (métadonnées) : 29 décembre 2025 11:57
- 2e trimestre [https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre]
	- Dernier traitement (données) : 28 août 2025 14:20
	- Dernier traitement (métadonnées) : 29 décembre 2025 11:57
- 3e trimestre [https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-3eme-trimestre]	
	- Dernier traitement (données) : 27 novembre 2025 11:12
	- Dernier traitement (métadonnées) : 29 décembre 2025 11:56
 -4e trimestre [https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-4eme-trimestre]
	- Dernier traitement (données) : 11 mars 2026 9:44
	- Dernier traitement (métadonnées) : 11 mars 2026 9:44

## Dictionnaire des données

| VARIABLE        | FORMAT            | DEFINITION                                          |
| --------------- | ----------------- | --------------------------------------------------- |
| JOUR 	          | Date (01/01/2015) | Jour d’exploitation (de 04:00 à 03:59 le lendemain) |
| COD_STIF_TRNS   | Numérique         | Code Stif du transporteur							|
| COD_STIF_RES    | Numérique 		  | Code Stif du réseau									|
| COD_STIF_ARRET  | Numérique 		  | Code Stif de l’arrêt/station						|
| LIBELLE_ARRET   | Caractère 		  | Libellé de l’arrêt/station							|
| ID_REFA_LDA     | Caractère         | Identifiant arrêt référentiel STIF					|
| CATEGORIE_TITRE | Caractère         | Titre de transport									|
| NB_VALD         | Numérique         | Nombre de validations (en entrée sur le réseau)		|

On s'intéresse à la *RATP*, COD_STIF_TRNS 100, réseau métro, COD_STIF_RES 110.

## Nettoyage mise en forme et exploration des données

Ces opérations sont décrites et exécutables dans le notebook `exploration.ipynb` (dossier `notebooks`).

>Le jeu de données mise en forme est stocké dans le dépôt [https://minio.lab.sspcloud.fr/jacquemmoz/partage/data_traitee.xlsx].

# Traitements envisagés et maquette

>Dossier 'maquettes' : évolution des maquettes durant l'avacement du projet, au format *excalidraw* et *png*.




### Traitements

- concaténation 110 (==> transporteur 100)
- 365j : OK, continuité ok
- 319 arrêts différents
- code_stif_arret, ida : "doublons"
	- valeurs aberrantes Mairie de St-Ouen, Maison-Blanche
- catégorie_titre : 
	- Forfaits courts
	- Autres titres
	- Contrat Solidarité Transport
	- Forfait Navigo
	- Imagine R
	- Amethyste
	- NON DEFINI
	- Contrat Solidarite Transport
- contrat SolidartiE SolidaritÉ
- ANTONY ?

# Indicateurs

- agréger titres "sociaux" ?
- forfaits spéciaux ? prévalence ? Par date.
- inconnu/anomalies ? prévalence ?

- 3 dimensions : stations (lignes), jours, titre
- géographie ?

- série temporelle :
	- par jour : effet w-e, + été
	- par semaine : été
	- forfaits courts vs Navigo/ImaginR
	
- titre spécial 21/6 (début année : titres papier ?)
