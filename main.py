from PyQt6 import QtWidgets, uic
import io
import sys
import sqlite3


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>773</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>90</y>
      <width>571</width>
      <height>421</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class TableOfTypesCoffees(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()   # q
        file = io.StringIO(template)
        uic.loadUi(file, self)
        connect = sqlite3.connect('coffee.sqlite')
        cursor = connect.cursor()
        all_info = cursor.execute('SELECT * FROM coffee_characteristic')
        all_info = [el for el in all_info]
        self.tableWidget.setRowCount(len(all_info))
        self.tableWidget.setColumnCount(7)
        for i in range(len(all_info)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(all_info[i][j])))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TableOfTypesCoffees()
    window.show()   # q q j
    sys.exit(app.exec())