import sys

from PySide.QtGui import *
from src.CSVimport import *
from src.Model import *
from src import Model, CSVimport, View

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
        self.table = Model.Model(datalist=[], header=["T", "WV", "WK", "BZ", "SPR", "WBER", "ABG", "UNG", "SPOE", "FPOE", "OEVP", "GRUE",
                                   "NEOS",
                                   "WWW", "ANDAS", "GFW", "SLP", "WIFF", "M", "FREIE"], parent=self)

        self.Out.actionNew.activated.connect(self.new)
        self.Out.actionOpen.activated.connect(self.open)
        self.Out.actionSave.activated.connect(self.save)
        self.Out.actionSave_as.activated.connect(self.saveas)
        self.Out.actionKopieren_2.activated.connect(self.copy)
        self.Out.actionEinf_gen.activated.connect(self.paste)
        self.Out.actionDelZeile.activated.connect(self.delzeile)
        self.Out.actionAusschneiden_2.activated.connect(self.cut)
        self.Out.actionDuplZeile.activated.connect(self.duplicate)
        self.Out.actionAddZeile.activated.connect(self.addzeile)

    """
        Anlegen einer neuen Tabelle.
    """
    def new(self):
        self.filename = None
        self.table.set_list([], [])

    """
        Oeffnet eine CSV-Datei, und zeigt sie im Fenster an.
    """
    def open(self):

        datei = QFileDialog.getOpenFileName(self, caption="CSV-Datei öffnen...", filter="CSV-Datei (*.csv)")[0]

        if datei:
            self.datei = datei
            fields, header = CSVimport.CSVimport.readcsv(self.datei)
            self.refresh_table(fields, header)

    """
        Speichert die Tabelle als CSV-Datei ab, unter dem verwendeten Dateinamen.
    """
    def save(self):

        if self.datei:
            CSVimport.CSVimport.writecsv(self.datei, self.table.get_list())
        else:
            self.saveas()

    """
        Speichert die Tabelle als neue CSV-Datei mit unterschiedlichen Attributen ab.
    """
    def saveas(self):

        datei = QFileDialog.getSaveFileName(self, caption="Als CSV-Datei speichern ...", dir=self.datei, filter="CSV-File (*.csv)")[0]

        if datei:
            self.datei = datei
            self.save()

    """
        Kopiert eine Zelle in die Zwischenablage.
    """
    def copy(self):
        if self.Out.tableView.selectionModel().selectedIndexes():

            clipboard = QApplication.clipboard()
            index = self.Out.tableView.selectionModel().selectedIndexes()[0]
            value = str(self.table.data(index))
            clipboard.setText(value)

    """
        Fuegt den Inhalt der Zwischenablage ein.
    """
    def paste(self):
        if self.Out.tableView.selectionModel().selectedIndexes():

            clipboard = QApplication.clipboard()
            index = self.Out.tableView.selectionModel().selectedIndexes()[0]
            self.table.setData(index, str(clipboard.text()))
            self.Out.tableView.reset()

    """
        Schneidet den Wert einer Zelle aus und legt in in der Zwischenablage ab.
    """
    def cut(self):
        if self.Out.tableView.selectionModel().selectedIndexes():

            clipboard = QApplication.clipboard()
            index = self.Out.tableView.selectionModel().selectedIndexes()[0]
            value = str(self.table.data(index))
            clipboard.setText(value)
            self.table.setData(index, '')
            self.Out.tableView.reset()

    """
        Fuegt eine Zeile unterhalb der letzten Zelle zur Tabelle hinzu.
    """
    def addzeile(self):
        if len(self.table.get_header()) != 0:
            self.table.insertRows(self.table.rowCount(self), 1)

    """
        Loescht eine Zeile aus der Tabelle.
    """
    def delzeile(self):

        try:

            if len(self.table.get_header()) != 0:
                index = self.Out.tableView.selectionModel().selectedIndexes()[0]
                self.table.removeRows(index.row(), 1)

        except IndexError as e:
            return

    """
        Aktualisiert die Tabellenansicht.
    """
    def refresh_table(self, fields, header):
        self.table.set_list(fields, header)
        self.Out.tableView.reset()
        self.Out.tableView.setModel(self.table)

    """
        Dupliziert eine Zeil der Tabelle.
    """
    def duplicate(self):
        if self.Out.tableView.selectionModel().selectedIndexes():

            index = self.Out.tableView.selectionModel().selectedIndexes()[0]
            self.table.duplicateRow(index.row())
            self.Out.tableView.reset()

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
