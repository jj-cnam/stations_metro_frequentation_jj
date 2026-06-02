Stockage des données : <https://datalab.sspcloud.fr/s3/jacquemmoz/?profile=default>


# Matériels et méthodes

## Source de données

[https://prim.iledefrance-mobilites.fr/]
Validations sur le réseau ferré en 2025
"Ce jeu de données présente le nombre de validations des voyageurs par jour par arrêt et par titre de transport sur le réseau ferré."
Licence : Licence ODbL Version Française https://spdx.org/licenses/ODbL-1.0.html#licenseText (spécifique BDD)
Producteur : Île-de-France Mobilités
4 trimestres ==> 4 fichiers à concaténer

### 1er trim

[https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-1er-trimestre]
Dernier traitement (données) : 23 juillet 2025 9:44
Dernier traitement (métadonnées) : 29 décembre 2025 11:57

### 2e trim

[https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-2eme-trimestre]
Dernier traitement (données) : 28 août 2025 14:20
Dernier traitement (métadonnées) : 29 décembre 2025 11:57

### 3e trim

[https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-3eme-trimestre]
Dernier traitement (données) : 27 novembre 2025 11:12
Dernier traitement (métadonnées) : 29 décembre 2025 11:56

### 4e trim
[https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/validations-reseau-ferre-nombre-validations-par-jour-4eme-trimestre]
Dernier traitement (données) : 11 mars 2026 9:44
Dernier traitement (métadonnées) : 11 mars 2026 9:44


### Dictionnaire des données

> Voir Word.
> Générer depuis le json.

jour : date : date de la Validation


jour	code_stif_trns	code_stif_res	code_stif_arret	libelle_arret	id_zdc	categorie_titre	nb_vald
2025-04-12	100	110	861	TRINITE	71355	NON DEFINI	73
2025-04-12	100	110	862	TROCADERO	71285	Forfaits courts	12487

**Attention, lorsque NB_VALD est égal à 5 cela correspond à 5 validations ou moins (RGPD)**

### Description des données

725 arrêts ferrés (RER, métro, Transilien)

Dans le cas du réseau ferré, les validations sont rattachées à
une station (et non à une ligne). En effet, la validation se fait à
l’entrée de la station, indépendamment de la ligne précise
empruntée. De plus, une fois entré dans le réseau métro ou
RER, l’usager n’a en général pas besoin de revalider lorsqu’il
change de ligne.

ATTENTION : le T4 est ici considéré comme un mode ferré

### Traitements

- agréger titres "sociaux" ?
- forfaits spéciaux ? prévalence ? Par date.
- inconnu/anomalies ? prévalence ?

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

- 3 dimensions : stations (lignes), jours, titre
- géographie ?

- série temporelle :
	- par jour : effet w-e, + été
	- par semaine : été
	- forfaits courts vs Navigo/ImaginR
	
- titre spécial 21/6 (début année : titres papier ?)


# Discussion

- tickets cartonnées pas pris en compte (+ pas de portique, travaux, fraude)


# Biblio

[https://eu.ftp.opendatasoft.com/stif/Validations/Documentation/Donnees_de_validation.pdf]