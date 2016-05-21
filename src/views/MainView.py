#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlDatabase

from views.Equipment import EquipmentLayout
from views.Act import ActPreview
from views.Buttons import ButtonLayout

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initDB()
        self.initUI()

    def initDB(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        dir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(dir, "data/aktor.db")

        self.db.setDatabaseName(filename)
        
    def initUI(self):
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)

        self.preview = ActPreview(self.db)
        self.equipmentLayout = EquipmentLayout(self.db)
        buttonLayout = ButtonLayout()

        hbox = QHBoxLayout()
        hbox.addLayout(self.equipmentLayout)
        hbox.addWidget(self.preview)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(buttonLayout)
        self.mainWidget.setLayout(vbox)

        self.recipient = self.equipmentLayout.recipient
        self.recipient.infoChanged.connect(self.updateRecipient)

        selection = self.equipmentLayout.table.selectionModel()
        selection.selectionChanged.connect(self.updateEquipment)
        self.setWindowParameters()

        buttonLayout.previewButton.pressed.connect(self.preview.updateText)

        self.show()

    def updateRecipient(self):
        self.preview.model.updateRecipient(self.equipmentLayout)

    def updateEquipment(self):
        self.preview.model.updateEquipment(self.equipmentLayout)

    def setWindowParameters(self):
        #self.resize(self.table.rect().width(),
                    #self.table.rect().height())

        self.setWindowTitle('aktor')
        screenGeometry = QApplication.desktop().screenGeometry();
        x = (screenGeometry.width()- self.width()) / 2;
        y = (screenGeometry.height()- self.height()) / 2;

        self.setGeometry(x, y, 1000, 500)
