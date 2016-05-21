
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout

class ButtonLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addStretch(1)

        self.previewButton = QPushButton("vista previa")
        self.addWidget(self.previewButton)
        self.nextButton = QPushButton("Siguiente")
        self.addWidget(self.nextButton)