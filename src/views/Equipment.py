
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSortFilterProxyModel

from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout

from models.EquipmentModel import EquipmentModel
from views.Recipient import RecipientLayout

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
        model.setData(index, value, Qt.DisplayRole)

    def upadteEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class EquipmentView(QTableView):
    def __init__(self, db):
        super().__init__()
        self.initUI(db)

    def initUI(self, db):
        equipment = EquipmentModel(db)
        self.setModel(equipment)
        
        self.setStates()
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSizes()

        proxy = QSortFilterProxyModel()
        self.setModel(proxy)
        proxy.setSourceModel(equipment)

    def setStates(self):
        items = []
        items.append("Disponible")
        items.append("Prestado")
        items.append("Perdido")

        delegate = ComboBoxDelegate(self, items)
        self.setItemDelegateForColumn(2, delegate)

    def setSizes(self):
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        width = self.verticalHeader().width()
        width += self.horizontalHeader().length()
        width += self.frameWidth() * 2
        self.setFixedWidth(width + 20);
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

class EquipmentLayout(QVBoxLayout):
    def __init__(self, db):
        super().__init__()
        self.recipient = RecipientLayout()
        self.addLayout(self.recipient)

        self.table = EquipmentView(db)
        self.addWidget(self.table)

        #recipient.setFixedWidth(self.table.width)

    def getSelectedSeries(self):
        series = []
        selection = self.table.selectionModel()
        for index in selection.selectedIndexes():
            if index.column() % 3 == 1:
                series.append(index.data())

        return series

    def getRecipientInfo(self):
        return self.recipient.getInfo()
