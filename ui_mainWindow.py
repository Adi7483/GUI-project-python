# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 646)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(234, 199, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browserButton = QtWidgets.QPushButton(self.centralwidget)
        self.browserButton.setGeometry(QtCore.QRect(30, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.browserButton.setFont(font)
        self.browserButton.setMouseTracking(True)
        self.browserButton.setStyleSheet("background-color: rgb(255, 215, 243);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"Segoe Print\";")
        self.browserButton.setObjectName("browserButton")
        self.runFile = QtWidgets.QPushButton(self.centralwidget)
        self.runFile.setGeometry(QtCore.QRect(290, 30, 121, 51))
        self.runFile.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"background-color: rgb(255, 192, 233);")
        self.runFile.setObjectName("runFile")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 30, 121, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 166, 232);\n"
"font: 8pt \"Segoe Print\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 30, 121, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(241, 141, 223);\n"
"font: 8pt \"Segoe Print\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 100, 161, 441))
        self.treeWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget.setObjectName("treeWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(283, 100, 471, 441))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.selectAll.setGeometry(QtCore.QRect(10, 550, 61, 41))
        self.selectAll.setStyleSheet("background-color: rgb(234, 178, 255);\n"
"font: 8pt \"Segoe Print\";")
        self.selectAll.setObjectName("selectAll")
        self.disSelectAll = QtWidgets.QPushButton(self.centralwidget)
        self.disSelectAll.setGeometry(QtCore.QRect(90, 550, 71, 41))
        self.disSelectAll.setStyleSheet("background-color: rgb(222, 144, 255);\n"
"font: 8pt \"Segoe Print\";")
        self.disSelectAll.setObjectName("disSelectAll")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 550, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"background-color: rgb(210, 119, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browserButton.setText(_translate("MainWindow", "Select file"))
        self.runFile.setText(_translate("MainWindow", "Run"))
        self.pushButton_4.setText(_translate("MainWindow", "logs"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop run"))
        self.selectAll.setText(_translate("MainWindow", "check"))
        self.disSelectAll.setText(_translate("MainWindow", "uncheck"))
        self.pushButton.setText(_translate("MainWindow", "clear"))
