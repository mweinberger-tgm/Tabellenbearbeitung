import sys

from PySide.QtGui import *

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

        self.Out.actionNew.activated.connect(self.new)
        self.Out.actionCopy_CS.activated.connect(self.copycs)
        self.Out.actionOpen.activated.connect(self.open)
        self.Out.actionSave.activated.connect(self.save)
        self.Out.actionSave_as.activated.connect(self.saveas)

    """
        New
    """
    def new(self):

        # Hier kommt der Methodeninhalt für New!
        print("New")

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

        if datei is not "":
            do = CSVimport(datei)
            out = do.readcsv()

            tmp = ""
            for row in out:
                tmp += str(row)
                tmp += "<br><br>"

            tmp += "Total rows: " + str(len(out))
            self.Out.textbox.setText(tmp)

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

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
