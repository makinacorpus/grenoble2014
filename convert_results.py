#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import csv

"""
    Ce fichier convertit les données brutes de bureaux provenant de
    http://www.grenoble.fr/125-elections.htm en format lisible par le scrit Leaflet dans index.hmtl
"""

if __name__ == '__main__':
    offices = {}
    participation = {}

    candidates = ('piolle', 'safar', 'chamussy', 'dornando', 'nuls')
    
    #keys
    fieldnames = ('nom_bureau', 'inscrits', 'emarges', 'procurations', 'votes', 'nuls', 'exprimes', 'piolle', 'safar', 'chamussy', 'dornando')
    
    # Concert CSV to JSON
    with open("grenoble_2eme_tour.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames, delimiter=";")
        #Skip first line
        reader.next()
        for row in reader:
            #Skip line without name
            if row["nom_bureau"] != "":
                results = sorted(
                    [{candidate.lower(): float(row[candidate]) * 100 / float(row["votes"])}
                     for candidate in candidates],
                    key=lambda k: k.values(),
                    reverse=True)
                bureau = row['nom_bureau'].split()[0]
                participation[bureau] = float(row["votes"]) * 100 / float(row["inscrits"])
                offices[bureau] = results
                pass

    # generate json
    with open("bureaux_decoupage_2.json", 'w') as outfile:
        outfile.write('var results2=')
        response_json = json.dump(offices, outfile)

    #generate json
    with open("participation_2.json", 'w') as outfile:
        outfile.write('var participation2=')
        response_json = json.dump(participation, outfile)
