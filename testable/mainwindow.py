# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/main.ui'
#
# Created: Fri Oct 16 09:24:08 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 463)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 286, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_text = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.name_text.setObjectName("name_text")
        self.horizontalLayout.addWidget(self.name_text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.submit_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout_2.addWidget(self.submit_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.hello_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.hello_label.setText("")
        self.hello_label.setObjectName("hello_label")
        self.verticalLayout.addWidget(self.hello_label)
        self.names_list = QtGui.QListWidget(self.centralwidget)
        self.names_list.setGeometry(QtCore.QRect(390, 20, 271, 192))
        self.names_list.setObjectName("names_list")
        self.clear_list_button = QtGui.QPushButton(self.centralwidget)
        self.clear_list_button.setGeometry(QtCore.QRect(390, 230, 98, 27))
        self.clear_list_button.setObjectName("clear_list_button")
        self.restore_list_button = QtGui.QPushButton(self.centralwidget)
        self.restore_list_button.setGeometry(QtCore.QRect(500, 230, 98, 27))
        self.restore_list_button.setObjectName("restore_list_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Qt Test Methods", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "What is your name:", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_button.setText(QtGui.QApplication.translate("MainWindow", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_list_button.setText(QtGui.QApplication.translate("MainWindow", "Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.restore_list_button.setText(QtGui.QApplication.translate("MainWindow", "Restore List", None, QtGui.QApplication.UnicodeUTF8))

