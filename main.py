from PyQt6 import QtWidgets, uic
import io
import sys
import sqlite3
from release.mainForm import Ui_MainWindow as MainForm
from release.newNote import Ui_MainWindow as AddNewNote
import os


class TableOfTypesCoffees(QtWidgets.QMainWindow, MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        connect = sqlite3.connect('\\'.join(os.getcwd().split('\\')[:-1]) + '\\data\\coffee.sqlite')
        cursor = connect.cursor()
        all_info = cursor.execute('SELECT * FROM coffee_characteristic')
        all_info = [el for el in all_info]
        self.tableWidget.setRowCount(len(all_info))
        self.tableWidget.setColumnCount(8)
        for i in range(len(all_info)):
            for j in range(8):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(all_info[i][j])))


class Notes(QtWidgets.QMainWindow, AddNewNote):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.note)

    def note(self):
        connect = sqlite3.connect('\\'.join(os.getcwd().split('\\')[:-1]) + '\\data\\coffee.sqlite')
        cursor = connect.cursor()
        all_info = cursor.execute('SELECT * FROM coffee_characteristic')
        all_info = [el for el in all_info]
        try:
            if self.lineEdit.text() is not None and self.textEdit.toPlainText() is not None:
                if int(self.lineEdit.text()) in [el[0] for el in all_info]:
                    cursor.execute("UPDATE coffee_characteristic SET notes = ? WHERE ID = ?", (self.textEdit.toPlainText(), int(self.lineEdit.text())))
                    connect.commit()
                    self.statusBar().showMessage('')
        except ValueError:
            self.statusBar().showMessage('ValueError')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TableOfTypesCoffees()
    window.show()
    window2 = Notes()
    window2.show()
    sys.exit(app.exec())