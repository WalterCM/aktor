
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit

class RecipientLayout(QVBoxLayout):

    infoChanged = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()
        self.info = {}

    def initUI(self):
        subtitle = QLabel("<b>Informacion del receptor</b>")
        self.addWidget(subtitle)

        self.nameEdit = QLineEdit()
        self.rankEdit = QLineEdit()
        self.cipEdit = QLineEdit()
        self.jobEdit = QLineEdit()

        self.addParameter("Nombre", self.nameEdit)
        self.addParameter("Grado", self.rankEdit)
        self.addParameter("CIP", self.cipEdit)
        self.addParameter("Cargo", self.jobEdit)

        self.nameEdit.textChanged.connect(self.updateInfo)
        self.rankEdit.textChanged.connect(self.updateInfo)
        self.cipEdit.textChanged.connect(self.updateInfo)
        self.jobEdit.textChanged.connect(self.updateInfo)

    def addParameter(self, text, lineEdit):
        layout = QHBoxLayout()
        label = QLabel(text)
        label.setFixedSize(50, 30)
        layout.addWidget(label)
        lineEdit.setFixedSize(200, 30)
        layout.addWidget(lineEdit)
        self.addLayout(layout)

    def updateInfo(self):
        self.info["recipient"] = self.nameEdit.text()
        self.info["rank"] = self.rankEdit.text()
        self.info["cip"] = self.cipEdit.text()
        self.info["job"] = self.jobEdit.text()
        self.infoChanged.emit()

    def getInfo(self):
        return self.info
        