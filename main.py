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

template2 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>193</width>
    <height>238</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>30</y>
      <width>121</width>
      <height>21</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>190</y>
      <width>121</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Подтвердить</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>80</y>
      <width>121</width>
      <height>71</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>81</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Введите ID&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>121</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Введите заметку&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
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
        super().__init__()
        file = io.StringIO(template)
        uic.loadUi(file, self)
        connect = sqlite3.connect('coffee.sqlite')
        cursor = connect.cursor()
        all_info = cursor.execute('SELECT * FROM coffee_characteristic')
        all_info = [el for el in all_info]
        self.tableWidget.setRowCount(len(all_info))
        self.tableWidget.setColumnCount(8)
        for i in range(len(all_info)):
            for j in range(8):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(all_info[i][j])))


class Notes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        file2 = io.StringIO(template2)
        uic.loadUi(file2, self)
        self.pushButton.clicked.connect(self.note)

    def note(self):
        connect = sqlite3.connect('coffee.sqlite')
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