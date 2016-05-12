#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from models import EquipmentModel
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton


class ComboBoxDelegate(QItemDelegate):
    def __init__(self, parent, items):
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(self.items)

        return editor

    def setEditorData(self, editor, index):
        value = str(index.model().data(index, Qt.EditRole))

        num = self.items.index(value)
        editor.setCurrentIndex(num)


    def setModelData(self, editor, model, index):
        value = editor.currentText()
        print(value)
        model.setData(index, value, Qt.DisplayRole)

    def upadteEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class EquipmentView(QTableView):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        equipment = EquipmentModel()
        self.setModel(equipment)
        items = []
        items.append("Disponible")
        items.append("Prestado")
        items.append("Perdido")
        delegate = ComboBoxDelegate(self, items)
        self.setItemDelegateForColumn(6, delegate)
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        hbox = QHBoxLayout()
        self.mainWidget.setLayout(hbox)

        view = EquipmentView()
        hbox.addWidget(view)

        self.resize(view.rect().width(),
                    view.rect().height())

        preview = QTextEdit()
        hbox.addWidget(preview)
        
        self.setWindowTitle('aktor')
        screenGeometry = QApplication.desktop().screenGeometry();
        x = (screenGeometry.width()- self.width()) / 2;
        y = (screenGeometry.height()- self.height()) / 2;
        #self.move(x, y)
        self.setGeometry(x, y, 1000, 500)
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
