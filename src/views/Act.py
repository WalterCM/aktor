
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from models.ActModel import ActModel

class ActPreview(QWebEngineView):
    def __init__(self, db):
        super().__init__()
        act = ActModel(db)
        self.setModel(act)
        #self.updateText()

    def setModel(self, model):
        self.model = model

    def updateText(self):
        dir = self.model.getTemplateDir()
        url = QUrl.fromLocalFile(dir)
        self.setHtml(self.model.toPlainText(), url)
