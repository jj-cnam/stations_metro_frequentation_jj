#!/usr/bin/env -S uv run --script

"""Script d'entrée/sortie.
Recopie la première feuille du classeur d'entrée dans la première feuille ('DATA') du classeur de sortie."""

import argparse
from io import BytesIO
import requests
from datetime import datetime
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet

from metro.feuilles import feuilles
from metro.graphes1 import graphes1
from metro.graphes2 import graphes2


# URL par défaut du fichier d'entrée
URL = "https://minio.lab.sspcloud.fr/jacquemmoz/partage/data_traitee.xlsx"


def dataset(source: Worksheet, cible: Workbook):
    """
    Copie les données sources dans une feuille "DATA" du classeur cible
    :param source: classeur des données sources
    :param cible: classeur cible
    """
    # feuille 'DATA'
    data = cible.create_sheet("DATA")
    for ligne in source:
        for cellule in ligne:
            data[cellule.coordinate].value = cellule.value


def orchestre(entree: BytesIO, sortie: str):
    """
    Orchestre la création du classeur, depuis la lecture du classeur source.
    :param entree: classeur d'entrée sous forme d'un buffer binaire
    par défaut correspond au contenu présent à l'url définie par la constante URL
    :param sortie: chemin du fichier de sortie du classeur
    """
    cible = Workbook()
    cible.remove(
        cible.worksheets[0]
    )  # efface la feuille créée par défaut avec le classeur

    # Feuille 'DATA' (import des données)
    print(str(datetime.now()), "Import des données...")
    source = load_workbook(entree, read_only=True)
    dataset(source.worksheets[0], cible)
    source.close()  # openpyxl.load_workbook() n'a pas de gestionnaire de contexte
    cible.save(sortie)

    # Feuilles de calcul
    print(str(datetime.now()), "Calcul des feuilles...")
    feuilles(cible)
    cible.save(sortie)

    # Graphes1
    print(str(datetime.now()), "Feuille Graphes1...")
    graphes1(cible)
    cible.active = cible["Graphes1"]
    cible.save(sortie)

    # Graphes2
    print(str(datetime.now()), "Feuille Graphes2...")
    graphes2(cible)
    cible.save(sortie)

    cible.close()
    print(str(datetime.now()), "Fin du traitement.")


def main():
    parser = argparse.ArgumentParser(
        description="Génère le tableau de bord de la fréquentation des stations de métro parisien",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    entree_args = parser.add_mutually_exclusive_group()
    entree_args.add_argument(
        "-i", "--input", type=str, help="chemin du fichier d'entrée"
    )
    entree_args.add_argument(
        "-u", "--url", type=str, help="url du fichier d'entrée", default=URL
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="chemin du fichier de sortie",
        default="sortie.xlsx",
    )
    args = parser.parse_args()
    if args.input:
        with open(args.input, "rb") as fichier:
            entree_bin = BytesIO(fichier.read())
    else:
        entree_bin = BytesIO(requests.get(args.url).content)
    orchestre(entree_bin, args.output)


if __name__ == "__main__":
    main()
