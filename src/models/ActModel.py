
import os
from PyQt5.QtCore import QDateTime
from PyQt5.QtSql import QSqlQuery

class ActModel():
    def __init__(self, db):
        self.recipientInfo = {}
        self.devicesInfo = []
        self.db = db

        dir = os.path.dirname(os.path.realpath('__file__'))
        self.templatedir = os.path.join(dir, "src/templates/")
        actFile = os.path.join(self.templatedir, "act.html")
        detailsFile = os.path.join(self.templatedir, "details.html")

        act = open(actFile, "r")
        details = open(detailsFile, "r")

        self.setTemplates(act.read(), details.read())
        self.startDatetime = QDateTime.currentDateTime()

    def setTemplates(self, act, details):
        self.act = act
        self.details = details

    def updateRecipient(self, equipmentLayout):
        self.recipientInfo = equipmentLayout.getRecipientInfo()

    def updateEquipment(self, equipmentLayout):
        if not self.db.open():
            return -1

        self.devicesInfo = []
        for serie in equipmentLayout.getSelectedSeries():
            query = QSqlQuery()
            query.prepare("SELECT d.description, " +
                                 "d.brand, " +
                                 "d.model, " +
                                 "i.serie, " +
                                 "i.id " +
                           "FROM Devices AS d " +
                           "INNER JOIN Items AS i " +
                           "ON d.id = i.device_id " +
                           "WHERE i.serie = ?")
            query.addBindValue(serie)
            query.exec_()
            while query.next():
                device = {}
                self.devicesInfo.append(device)
                device["name"] = str(query.value(0))
                device["brand"] = str(query.value(1))
                device["model"] = str(query.value(2))
                device["serie"] = str(query.value(3))
                device["id"] = str(query.value(4))

        self.db.close()

    def replaceTemplate(self):
        if len(self.recipientInfo) == 0 or len(self.devicesInfo) == 0:
            return ""

        text = (self.act + '.')[:-1]
        text = self.updateElement(text, "time",
                                  self.startDatetime.time().toString("hh:mm"))
        text = self.updateElement(text, "date",
                                  self.startDatetime.date().toString("ddMMMyyyy"))
        for var in self.recipientInfo:
            text = self.updateElement(text, var, self.recipientInfo[var])
        
        amount = len(self.devicesInfo)
        text = self.updateElement(text, "amount", str(amount))
        text = self.updateElement(text, "amount_text", self.getAmountText(amount))
        deviceText = ""
        for i in range(amount):
            newDevice = (self.details + '.')[:-1]
            for var in self.devicesInfo[i]:
                newDevice = self.updateElement(newDevice, "index", str(i + 1))
                newDevice = self.updateElement(newDevice, var,
                                               self.devicesInfo[i][var])

            deviceText += newDevice
        text = self.updateElement(text, "details", deviceText)
        endDatetime = QDateTime.currentDateTime()
        text = self.updateElement(text, "endtime",
                                  endDatetime.time().toString("hh:mm"))
        return text

    def toPlainText(self):
        return self.replaceTemplate()

    def updateElement(Self, text, element, value):
        tag = "[% " + element + " %]"
        while tag in text:
            text = text.replace(tag, value)

        return text

    def getTemplateDir(self):
        return self.templatedir

    def getAmountText(self, amount):
        if amount == 1:
            return "un"
        elif amount == 2:
            return "dos"
        elif amount == 3:
            return "tres"
        elif amount == 4:
            return "cuatro"
        elif amount == 5:
            return "cinco"
        elif amount == 6:
            return "seis"
        elif amount == 7:
            return "siete"
        elif amount == 8:
            return "ocho"
        elif amount == 9:
            return "nueve"