#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("../data/aktor.db")
        if db.open():
            print("opened")
        else:
            print("not opened")

        query = QSqlQuery()
        query.exec_("SELECT code FROM Equipment")
        while (query.next()):
            print("something")
            print(query.value(0))

        self.btn = QPushButton('button', self)
        self.btn.move(100, 20)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('sql test')
        self.show()        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    