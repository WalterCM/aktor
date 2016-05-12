#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

class EquipmentModel(QSqlQueryModel):
    def __init__(self):
        super().__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        dir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(dir, "data/aktor.db")

        self.db.setDatabaseName(filename)
        if not self.db.open():
            return -1

        self.refresh()

    def flags(self, index):
        flags = QSqlQueryModel.flags(self, index)
        if index.column() == 6:
            flags |= Qt.ItemIsEditable
        return flags

    def setData(self, index, value, role):
        if index.column() != 6:
            return False

        primaryKeyIndex = QSqlQueryModel.index(self, index.row(), 1)
        id = self.data(primaryKeyIndex)

        self.clear()
        ok = self.setState(id, str(value))
        self.refresh()
        return ok

    def setState(self, item_id, state):
        query = QSqlQuery()
        query.prepare("UPDATE Items SET state = ? WHERE id = ?")
        query.addBindValue(state)
        query.addBindValue(item_id)
        return query.exec_()

    def refresh(self):
        self.setQuery("SELECT  d.description,\
                               i.serie,\
                               i.state\
                       FROM Items as i\
                       INNER JOIN Devices as d\
                       ON i.device_id = d.id")
        self.setHeaderData(0, Qt.Horizontal, "Descripcion")
        self.setHeaderData(1, Qt.Horizontal, "Serie")
        self.setHeaderData(2, Qt.Horizontal, "Estado")
