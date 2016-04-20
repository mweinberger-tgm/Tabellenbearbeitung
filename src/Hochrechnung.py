from PySide import QtGui
from PySide.QtGui import QDialog, QVBoxLayout
from src.Model import *

"""
    Erzeugt das Fenster, dass die zusammengestellte Hochrechnung ausgibt.
"""
class Hochrechnung(QDialog):

    def __init__(self, data, header, title, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        table_model = Model(datalist=[], header=[], parent=self)
        table_model.set_list(data, header)

        self.view = QtGui.QTableView(self)
        self.view.setModel(table_model)
        self.view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.view.resizeColumnsToContents()
        layout.addWidget(self.view)

        self.setWindowTitle(title)
        self.resize(500, 100)
        self.setModal(True)
        self.exec_()
