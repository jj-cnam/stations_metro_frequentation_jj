#!/usr/bin/env -S uv run --script

"""Script d'entrée/sortie.
Recopie la première feuille du classeur d'entrée dans la première feuille ('DATA') du classeur de sortie
et orchestre la génération du classeur de sortie."""

from datetime import datetime
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.worksheet import Worksheet

from metro.feuilles import feuilles
from metro.graphes1 import graphes1
from metro.graphes2 import graphes2


def dataset(source:Worksheet, cible:Workbook):
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


def main():
    """
    Orchestre la création du classeur, depuis la lecture du classeur source.
    """
    # prévoir argparse
    fichier_cible = "sortie.xlsx"
    cible = Workbook()
    cible.remove(cible.worksheets[0])  # efface la feuille créée par défaut avec le classeur

    # Feuille 'DATA' (import des données)
    print(str(datetime.now()), "Import des données...")
    source = load_workbook("data_traitee.xlsx")
    dataset(source.worksheets[0], cible)
    source.close()  # openpyxl.load_workbook() n'a pas de gestionnaire de contexte
    cible.save(fichier_cible)

    # Feuilles de calcul
    print(str(datetime.now()), "Calcul des feuilles...")
    feuilles(cible)
    cible.save(fichier_cible)

    # Graphes1
    print(str(datetime.now()), "Feuille Graphes1...")
    graphes1(cible)
    cible.active = cible["Graphes1"]
    cible.save(fichier_cible)

    # Graphes2
    print(str(datetime.now()), "Feuille Graphes2...")
    graphes2(cible)
    cible.save(fichier_cible)

    cible.close()
    print(str(datetime.now()), "Fin du traitement.")


if __name__ == "__main__":
    main()
