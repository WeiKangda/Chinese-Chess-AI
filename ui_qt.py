# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1189, 1024)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 932, 1024))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/bg.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(917, 0, 272, 1024))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/pure.jpg"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(952, 420, 151, 31))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(952, 40, 250, 320))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(952, 330, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(982, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_end = QtWidgets.QLabel(self.centralwidget)
        self.label_end.setGeometry(QtCore.QRect(952, 500, 141, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(20)
        self.label_end.setFont(font)
        self.label_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_end.setObjectName("label_end")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chinese Chess-AlphaZero"))
        self.label_3.setText(_translate("MainWindow", "Move format：xyx\'y\'\n"
"xy are coordiantes before the move.\n"
"x is the row number.\n"
"y is the column number.\n"
"x\'y\'are coordiantes\n" 
"after the move.\n"                                   
"Please wait for the AI\n" 
"after your move.\n"
"The piece won't move if the \n"
"coordinates are illegal.\n"
"Please try again.\n"
 "Green dot represents\n"
 "the last move by AI"))
        self.label_4.setText(_translate("MainWindow", "--------------\n"
"Your turn\n"
"Enter your move"))
        self.pushButton.setText(_translate("MainWindow", "Game over"))
        self.label_end.setText(_translate("MainWindow", "Game on"))


