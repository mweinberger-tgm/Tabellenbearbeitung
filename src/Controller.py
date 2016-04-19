import sys

from PySide.QtGui import *
from src.Model import Model
from src import View
from src.CSVimport import *

__author__ = 'Michael Weinberger'
__date__ = 20160211
__version__ = 1.0


class Controller(QMainWindow):

    """
        Anzeigen der GUI
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.Out = View.Ui_MainWindow()
        self.Out.setupUi(self)

        self.Out.tableView.setSortingEnabled(True)

        self.datei = None
        self.table = Model(datalist=[], header=[], parent=self)

        self.Out.actionNew.activated.connect(self.new)
        self.Out.actionOpen.activated.connect(self.open)
        self.Out.actionSave.activated.connect(self.save)
        self.Out.actionSave_as.activated.connect(self.saveas)

    """
        New
    """
    def new(self):
        self.filename = None
        self.table.set_list([], [])

    """
        Copy CS
    """
    def copycs(self):

        # Hier kommt der Methodeninhalt für Copy CS!
        print("Copy CS")

    """
        Oeffnet eine CSV-Datei, und zeigt sie im Fenster an.
    """
    def open(self):

        datei = QFileDialog.getOpenFileName(self, caption="CSV-Datei öffnen...", filter="CSV-Datei (*.csv)")[0]

        if datei is not '':
            self.datei = datei
            fields, header = CSVimport.readcsv(self.datei)
            self.refresh_table(fields, header)

    """
        Save
    """
    def save(self):

        # Hier kommt der Methodeninhalt für Save!
        print("Save")

    """
        Save As
    """
    def saveas(self):

        # Hier kommt der Methodeninhalt für Save as!
        print("Save as")

    def refresh_table(self, fields, header):
        self.table.set_list(fields, header)
        self.Out.tableView.reset()
        self.Out.tableView.setModel(self.table)

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
