# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThirdWindow(object):
    def setupUi(self, ThirdWindow):
        ThirdWindow.setObjectName("ThirdWindow")
        ThirdWindow.setFixedSize(600, 400)
        self.centralwidget3 = QtWidgets.QWidget(ThirdWindow)
        self.centralwidget3.setObjectName("centralwidget3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 441, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_1_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1_3.setObjectName("verticalLayout_1_3")
        self.label_1_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1_3.setObjectName("label_1_3")
        self.verticalLayout_1_3.addWidget(self.label_1_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(420, 359, 171, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.view = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.view.setObjectName("view")
        self.horizontalLayout3.addWidget(self.view)
        self.exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.exit.setObjectName("exit")
        self.horizontalLayout3.addWidget(self.exit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 581, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2_3.setObjectName("verticalLayout_2_3")
        self.label_2_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2_3.setText("")
        self.label_2_3.setPixmap(QtGui.QPixmap("Фон.png"))
        self.label_2_3.setObjectName("label_2_3")
        self.verticalLayout_2_3.addWidget(self.label_2_3)
        ThirdWindow.setCentralWidget(self.centralwidget3)

        self.retranslateUi(ThirdWindow)
        QtCore.QMetaObject.connectSlotsByName(ThirdWindow)

    def retranslateUi(self, ThirdWindow):
        _translate = QtCore.QCoreApplication.translate
        ThirdWindow.setWindowTitle(_translate("ThirdWindow", "Background Remover"))
        ThirdWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label_1_3.setText(_translate("ThirdWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#00ff00;\">Готово ☑</span></p></body></html>"))
        self.view.setText(_translate("ThirdWindow", "Переглянути"))
        self.exit.setText(_translate("ThirdWindow", "Вийти"))

