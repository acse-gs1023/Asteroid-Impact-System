# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deepimpack_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1005, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.generate_buttom.setGeometry(QtCore.QRect(760, 290, 113, 32))
        self.generate_buttom.setObjectName("generate_buttom")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 20, 227, 250))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.angle = QtWidgets.QLineEdit(self.layoutWidget)
        self.angle.setObjectName("angle")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.angle)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.strength = QtWidgets.QLineEdit(self.layoutWidget)
        self.strength.setObjectName("strength")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.strength)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.density = QtWidgets.QLineEdit(self.layoutWidget)
        self.density.setObjectName("density")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.density)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.velocity = QtWidgets.QLineEdit(self.layoutWidget)
        self.velocity.setObjectName("velocity")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.velocity)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.latitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.latitude.setObjectName("latitude")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.latitude)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.longitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.longitude.setObjectName("longitude")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.longitude)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.bearing = QtWidgets.QLineEdit(self.layoutWidget)
        self.bearing.setObjectName("bearing")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.bearing)
        self.radius = QtWidgets.QLineEdit(self.layoutWidget)
        self.radius.setObjectName("radius")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radius)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(660, 340, 321, 141))
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(3, 0, item)
        self.plot_button = QtWidgets.QPushButton(self.centralwidget)
        self.plot_button.setGeometry(QtCore.QRect(760, 500, 113, 32))
        self.plot_button.setObjectName("plot_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 591, 461))
        self.widget.setBaseSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 500, 601, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        self.type = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.type.setObjectName("type")
        self.horizontalLayout_11.addWidget(self.type)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_11.addWidget(self.label_16)
        self.zero_point1 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.zero_point1.setObjectName("zero_point1")
        self.horizontalLayout_11.addWidget(self.zero_point1)
        self.zero_point2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.zero_point2.setObjectName("zero_point2")
        self.horizontalLayout_11.addWidget(self.zero_point2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(620, 0, 20, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generate_buttom.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "radius"))
        self.label_2.setText(_translate("MainWindow", "angle"))
        self.angle.setText(_translate("MainWindow", "45"))
        self.label_3.setText(_translate("MainWindow", "strength"))
        self.strength.setText(_translate("MainWindow", "1e7"))
        self.label_5.setText(_translate("MainWindow", "density"))
        self.density.setText(_translate("MainWindow", "3000"))
        self.label_4.setText(_translate("MainWindow", "velocity"))
        self.velocity.setText(_translate("MainWindow", "19e3"))
        self.label_6.setText(_translate("MainWindow", "entry latitude"))
        self.latitude.setText(_translate("MainWindow", "55.2"))
        self.label_7.setText(_translate("MainWindow", "entry longitude"))
        self.longitude.setText(_translate("MainWindow", "-2.5"))
        self.label_8.setText(_translate("MainWindow", "bearing"))
        self.bearing.setText(_translate("MainWindow", "217"))
        self.radius.setText(_translate("MainWindow", "50"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Damage level 1"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Damage level 2"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Damage level 3"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Damage level 4"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pressure"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Radius"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Plot"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("MainWindow", "1 kPa"))
        item = self.table.item(1, 0)
        item.setText(_translate("MainWindow", "4 kPa"))
        item = self.table.item(2, 0)
        item.setText(_translate("MainWindow", "30 kPa"))
        item = self.table.item(3, 0)
        item.setText(_translate("MainWindow", "50 kPa"))
        self.table.setSortingEnabled(__sortingEnabled)
        self.plot_button.setText(_translate("MainWindow", "Plot map"))
        self.label_15.setText(_translate("MainWindow", "Type"))
        self.label_16.setText(_translate("MainWindow", "zero point"))
