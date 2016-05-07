#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QTableView, QApplication
from models import EquipmentModel

class EquipmentView(QTableView):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        equipment = EquipmentModel()
        self.setModel(equipment)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('sql test')
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    view = EquipmentView()
    sys.exit(app.exec_())
