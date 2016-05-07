#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

class EquipmentModel(QSqlQueryModel):
    def __init__(self):
        super().__init__()
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("../data/aktor.db")
        if db.open():
            print("opened")
        else:
            print("not opened")

        self.setQuery("SELECT * FROM Equipment")
        self.setHeaderData(0, Qt.Horizontal, "Codigo")