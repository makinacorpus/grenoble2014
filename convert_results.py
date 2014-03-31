#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import namedtuple
import json
import sys
import csv

"""
    Ce fichier convertit les données brutes de bureaux provenant de
    caen.fr/ResultatsAffichage/MenuScrutin.aspx en format lisible par le scrit Leaflet dans index.hmtl
"""
"""
candidates = ['l_orphelin','de_la_provote','duron','bruneau','casevitz','adam','chapron', 'NULS']

OfficeResults = namedtuple(
    'OfficeResult',
    ' ,'.join(candidates))
"""

if __name__ == '__main__':
    """
    if len(sys.argv) != 3:
        msg = 'Usage : {command} <input.json> <output.json>'.format(
            command=sys.argv[0])
        print(msg)
        exit()
    """
    offices = {}
    
    # Concert CSV to JSON
    #csvfile = open(sys.argv[1], 'r')
    #csvfile = open("grenoble_2eme_tour.csv")
    #jsonfile = open('tempo.json', 'w')
    candidates = ('piolle', 'safar', 'chamussy', 'dornando', 'nuls')
    fieldnames = ('nom_bureau', 'inscrits', 'emarges', 'procurations', 'votes', 'nuls', 'exprimes', 'piolle', 'safar', 'chamussy', 'dornando')

    #fieldnames = ('nom_bureau','sous_bureau','l_orphelin','de_la_provote','duron','bruneau','casevitz','adam','chapron','NULS')
    #reader.next() # skip header
    """
    jsonfile.write('{"version":"1", "data":[')
    virg = ''
    for row in reader:
        jsonfile.write('%s' % (virg))
        json.dump(row, jsonfile)
        virg = ',\n'
    jsonfile.write(']}')
    jsonfile.close()
    """
    # process data

    with open("grenoble_2eme_tour.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames, delimiter=";")

        #reader = json.load(json_file, encoding='utf8')
        reader.next()
        for row in reader:
            if row["nom_bureau"] != "":
                results = sorted(
                    [{candidate.lower(): float(row[candidate]) * 100/ float(row["votes"])}
                     for candidate in candidates],
                    key=lambda k: k.values(),
                    reverse=True)
                bureau = row['nom_bureau'].split()[0]
                offices[bureau] = results
                pass

    with open("bureaux_decoupage_2.json", 'w') as outfile:
        outfile.write('var results2=')
        response_json = json.dump(offices, outfile)