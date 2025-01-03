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
    <width>593</width>
    <height>510</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>571</width>
      <height>421</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="edit_btn">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>20</y>
      <width>201</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Изменить выделенную ячейку</string>
    </property>
   </widget>
   <widget class="QPushButton" name="add_btn">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>121</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Добавить запись</string>
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
    <width>585</width>
    <height>256</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>151</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;название сорта&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>10</y>
      <width>161</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;степень обжарки&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>20</y>
      <width>161</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;молотый/в зернах&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>100</y>
      <width>131</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;описание вкуса&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>100</y>
      <width>81</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;цена&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;объем упаковки&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_3">
    <property name="geometry">
     <rect>
      <x>170</x>
      <y>60</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_4">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>60</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_5">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>140</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_6">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>140</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_7">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>140</y>
      <width>113</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>360</x>
      <y>180</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Применить</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

template3 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>205</width>
    <height>124</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>161</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>171</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Введите значение&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>70</y>
      <width>161</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Применить</string>
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
        self.update_table()
        self.add_btn.clicked.connect(self.add_el)
        self.edit_btn.clicked.connect(self.edit_el)
        self.tableWidget.itemSelectionChanged.connect(self.curr_selection_cell)

    def curr_selection_cell(self):
        self.curr_cell = (self.tableWidget.currentRow(), self.tableWidget.currentColumn())

    def update_table(self):
        connect = sqlite3.connect('coffee.sqlite')
        cursor = connect.cursor()
        all_info = cursor.execute('SELECT * FROM coffee_characteristic')
        all_info = list(all_info)
        self.tableWidget.setRowCount(len(all_info))
        self.tableWidget.setColumnCount(7)
        for i in range(len(all_info)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(all_info[i][j])))

    def add_el(self):
        self.add_widget = QtWidgets.QMainWindow()
        file = io.StringIO(template2)
        uic.loadUi(file, self.add_widget)
        self.add_widget.show()
        self.add_widget.pushButton.clicked.connect(self.edit_db)

    def edit_db(self):
        connect = sqlite3.connect('coffee.sqlite')
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO coffee_characteristic (
                                      [название сорта],
                                      [степень обжарки],
                                      [молотый/в зернах],
                                      [описание вкуса],
                                      цена,
                                      [объем упаковки]
                                  )
                                  VALUES (
                                      ?,
                                      ?,
                                      ?,
                                      ?,
                                      ?,
                                      ?
                                  );
""", (self.add_widget.lineEdit_2.text(), self.add_widget.lineEdit_3.text(),
      self.add_widget.lineEdit_4.text(), self.add_widget.lineEdit_5.text(),
      self.add_widget.lineEdit_6.text(), self.add_widget.lineEdit_7.text()))
        connect.commit()
        self.update_table()

    def edit_el(self):
        self.edit_widget = QtWidgets.QMainWindow()
        file = io.StringIO(template3)
        uic.loadUi(file, self.edit_widget)
        self.edit_widget.show()
        self.edit_widget.pushButton.clicked.connect(self.changeCell)

    def changeCell(self):
        connect = sqlite3.connect('coffee.sqlite')
        cursor = connect.cursor()
        self.tableWidget.setItem(self.curr_cell[0], self.curr_cell[1],
                                 QtWidgets.QTableWidgetItem(self.edit_widget.lineEdit.text()))
        cursor.execute('DELETE FROM coffee_characteristic')
        for i in range(self.tableWidget.rowCount()):
            cursor.execute("""INSERT INTO coffee_characteristic (
                                      [название сорта],
                                      [степень обжарки],
                                      [молотый/в зернах],
                                      [описание вкуса],
                                      цена,
                                      [объем упаковки]
                                  )
                                  VALUES (
                                      ?,
                                      ?,
                                      ?,
                                      ?,
                                      ?,
                                      ?
                                  );
""", (self.tableWidget.item(i, 1).text(),
      self.tableWidget.item(i, 2).text(), self.tableWidget.item(i, 3).text(),
      self.tableWidget.item(i, 4).text(), self.tableWidget.item(i, 5).text(),
      self.tableWidget.item(i, 6).text()))
        connect.commit()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TableOfTypesCoffees()
    window.show()
    sys.exit(app.exec())   # q