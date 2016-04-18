import csv

"""
Eine einfache Klasse, die ein beliebiges CSV-File ausliest
"""


class CSVimport(object):

    """
    Der Filename wird hier uebergeben
    """
    def __init__(self, filename):
        self.filename = filename

    """
    Liest das gewuenschte CSV-File aus und liefert es als Liste zurueck.
    """
    def readcsv(self):

        out = []

        with open(self.filename, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                out.append(row)

        return out
