from csv import *

"""
Eine einfache Klasse, die ein beliebiges CSV-File ausliest
"""


class CSVimport(object):

    """
        Liest das gewuenschte CSV-File aus und liefert es als Liste inkl. Header zurueck.
    """
    @staticmethod
    def readcsv(filename):

        with open(filename, newline='') as f:

            sniffer = Sniffer()
            sample = f.read(4096)
            dialect = sniffer.sniff(sample, delimiters=[';', ','])

            f.seek(0)

            lines_reader = DictReader(f, dialect=dialect)

            lines = []
            for line in lines_reader:
                lines.append(line)

            return lines, lines_reader.fieldnames

    """
        Speichert die Tabelle als CSV-Datei unter dem mitgelieferten Namen ab.
    """
    @staticmethod
    def writecsv(filename, lines, delimiter=';'):

        with open(filename, 'w') as f:

            if len(lines) == 0:
                return

            fieldnames = list(lines[0].keys())
            writer = DictWriter(f, delimiter=delimiter, fieldnames=fieldnames)
            writer.writerow(dict((fn, fn) for fn in fieldnames))

            for line in lines:
                writer.writerow(line)
