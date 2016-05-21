#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel

class EquipmentModel(QSqlQueryModel):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.refresh()

    def flags(self, index):
        flags = QSqlQueryModel.flags(self, index)
        if index.column() == 2:
            flags |= Qt.ItemIsEditable
        return flags

    def setData(self, index, value, role):
        if index.column() != 2:
            return False

        primaryKeyIndex = QSqlQueryModel.index(self, index.row(), 1)
        id = self.data(primaryKeyIndex)

        self.clear()
        ok = self.setState(id, str(value))
        self.refresh()
        return ok

    def setState(self, item_id, state):
        if not self.db.open():
            return -1
        query = QSqlQuery()
        query.prepare("UPDATE Items SET state = ? WHERE id = ?")
        query.addBindValue(state)
        query.addBindValue(item_id)
        self.db.close
        return query.exec_()

    def refresh(self):
        if not self.db.open():
            return -1

        self.setQuery("SELECT  d.description, " +
                      "i.serie, " +
                      "i.state " +
                      "FROM Items as i " +
                      "INNER JOIN Devices as d " +
                      "ON i.device_id = d.id")
        self.setHeaderData(0, Qt.Horizontal, "Descripcion")
        self.setHeaderData(1, Qt.Horizontal, "Serie")
        self.setHeaderData(2, Qt.Horizontal, "Estado")

        self.db.close
