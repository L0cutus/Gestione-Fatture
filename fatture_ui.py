# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fatture.ui'
#
# Created: Sat Jun 27 18:12:35 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 502)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(111, 0))
        self.dateEdit.setFrame(False)
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.copiaVettCheckBox = QtGui.QCheckBox(self.groupBox)
        self.copiaVettCheckBox.setGeometry(QtCore.QRect(0, 60, 113, 21))
        self.copiaVettCheckBox.setObjectName("copiaVettCheckBox")
        self.copiaCliCheckBox = QtGui.QCheckBox(self.groupBox)
        self.copiaCliCheckBox.setGeometry(QtCore.QRect(0, 40, 121, 21))
        self.copiaCliCheckBox.setChecked(True)
        self.copiaCliCheckBox.setObjectName("copiaCliCheckBox")
        self.copiaIntCheckBox = QtGui.QCheckBox(self.groupBox)
        self.copiaIntCheckBox.setGeometry(QtCore.QRect(0, 20, 111, 21))
        self.copiaIntCheckBox.setChecked(True)
        self.copiaIntCheckBox.setObjectName("copiaIntCheckBox")
        self.gridLayout.addWidget(self.groupBox, 0, 8, 3, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.fattLineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fattLineEdit.sizePolicy().hasHeightForWidth())
        self.fattLineEdit.setSizePolicy(sizePolicy)
        self.fattLineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fattLineEdit.setObjectName("fattLineEdit")
        self.gridLayout.addWidget(self.fattLineEdit, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.tipoFattComboBox = QtGui.QComboBox(self.centralwidget)
        self.tipoFattComboBox.setObjectName("tipoFattComboBox")
        self.tipoFattComboBox.addItem(QtCore.QString())
        self.tipoFattComboBox.addItem(QtCore.QString())
        self.tipoFattComboBox.addItem(QtCore.QString())
        self.gridLayout.addWidget(self.tipoFattComboBox, 2, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(47, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.cliComboBox = QtGui.QComboBox(self.centralwidget)
        self.cliComboBox.setMinimumSize(QtCore.QSize(211, 0))
        self.cliComboBox.setEditable(False)
        self.cliComboBox.setObjectName("cliComboBox")
        self.gridLayout.addWidget(self.cliComboBox, 3, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(67, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.tipoPagLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.tipoPagLineEdit.setObjectName("tipoPagLineEdit")
        self.gridLayout.addWidget(self.tipoPagLineEdit, 4, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.cauLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.cauLineEdit.setMinimumSize(QtCore.QSize(381, 0))
        self.cauLineEdit.setObjectName("cauLineEdit")
        self.gridLayout.addWidget(self.cauLineEdit, 5, 1, 1, 6)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.noteLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.noteLineEdit.setMinimumSize(QtCore.QSize(381, 0))
        self.noteLineEdit.setObjectName("noteLineEdit")
        self.gridLayout.addWidget(self.noteLineEdit, 6, 1, 1, 6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addMPushButton.sizePolicy().hasHeightForWidth())
        self.addMPushButton.setSizePolicy(sizePolicy)
        self.addMPushButton.setMinimumSize(QtCore.QSize(37, 0))
        self.addMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.addMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMPushButton.setIcon(icon1)
        self.addMPushButton.setObjectName("addMPushButton")
        self.horizontalLayout.addWidget(self.addMPushButton)
        self.delMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delMPushButton.sizePolicy().hasHeightForWidth())
        self.delMPushButton.setSizePolicy(sizePolicy)
        self.delMPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.delMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.delMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delMPushButton.setIcon(icon2)
        self.delMPushButton.setObjectName("delMPushButton")
        self.horizontalLayout.addWidget(self.delMPushButton)
        self.firstMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstMPushButton.sizePolicy().hasHeightForWidth())
        self.firstMPushButton.setSizePolicy(sizePolicy)
        self.firstMPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.firstMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.firstMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstMPushButton.setIcon(icon3)
        self.firstMPushButton.setObjectName("firstMPushButton")
        self.horizontalLayout.addWidget(self.firstMPushButton)
        self.prevMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevMPushButton.sizePolicy().hasHeightForWidth())
        self.prevMPushButton.setSizePolicy(sizePolicy)
        self.prevMPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.prevMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.prevMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevMPushButton.setIcon(icon4)
        self.prevMPushButton.setObjectName("prevMPushButton")
        self.horizontalLayout.addWidget(self.prevMPushButton)
        self.nextMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextMPushButton.sizePolicy().hasHeightForWidth())
        self.nextMPushButton.setSizePolicy(sizePolicy)
        self.nextMPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.nextMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.nextMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextMPushButton.setIcon(icon5)
        self.nextMPushButton.setObjectName("nextMPushButton")
        self.horizontalLayout.addWidget(self.nextMPushButton)
        self.lastMPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastMPushButton.sizePolicy().hasHeightForWidth())
        self.lastMPushButton.setSizePolicy(sizePolicy)
        self.lastMPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.lastMPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.lastMPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastMPushButton.setIcon(icon6)
        self.lastMPushButton.setObjectName("lastMPushButton")
        self.horizontalLayout.addWidget(self.lastMPushButton)
        self.printPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.printPushButton.sizePolicy().hasHeightForWidth())
        self.printPushButton.setSizePolicy(sizePolicy)
        self.printPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.printPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.printPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/fileprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printPushButton.setIcon(icon7)
        self.printPushButton.setObjectName("printPushButton")
        self.horizontalLayout.addWidget(self.printPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 4)
        spacerItem3 = QtGui.QSpacerItem(167, 33, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 7, 4, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(67, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 7, 7, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(83, 31, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 8, 1, 1)
        self.sTableView = QtGui.QTableView(self.centralwidget)
        self.sTableView.setObjectName("sTableView")
        self.gridLayout.addWidget(self.sTableView, 8, 0, 1, 9)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSPushButton.sizePolicy().hasHeightForWidth())
        self.addSPushButton.setSizePolicy(sizePolicy)
        self.addSPushButton.setMinimumSize(QtCore.QSize(37, 0))
        self.addSPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.addSPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addSPushButton.setIcon(icon1)
        self.addSPushButton.setObjectName("addSPushButton")
        self.horizontalLayout_2.addWidget(self.addSPushButton)
        self.delSPushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delSPushButton.sizePolicy().hasHeightForWidth())
        self.delSPushButton.setSizePolicy(sizePolicy)
        self.delSPushButton.setMinimumSize(QtCore.QSize(36, 0))
        self.delSPushButton.setMaximumSize(QtCore.QSize(46, 16777215))
        self.delSPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delSPushButton.setIcon(icon2)
        self.delSPushButton.setObjectName("delSPushButton")
        self.horizontalLayout_2.addWidget(self.delSPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 9, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 9, 2, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(423, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 9, 3, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 23))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setObjectName("menu_Tools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_About = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About.setIcon(icon8)
        self.action_About.setObjectName("action_About")
        self.action_New_File = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/filenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New_File.setIcon(icon9)
        self.action_New_File.setObjectName("action_New_File")
        self.action_Load_File = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Load_File.setIcon(icon10)
        self.action_Load_File.setObjectName("action_Load_File")
        self.action_Exit = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon11)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Add_Customers = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/add3d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Add_Customers.setIcon(icon12)
        self.action_Add_Customers.setObjectName("action_Add_Customers")
        self.menu_File.addAction(self.action_New_File)
        self.menu_File.addAction(self.action_Load_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addAction(self.action_About)
        self.menu_Tools.addAction(self.action_Add_Customers)
        self.menu_Tools.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label.setBuddy(self.dateEdit)
        self.label_5.setBuddy(self.fattLineEdit)
        self.label_7.setBuddy(self.tipoFattComboBox)
        self.label_2.setBuddy(self.cliComboBox)
        self.label_6.setBuddy(self.tipoPagLineEdit)
        self.label_3.setBuddy(self.cauLineEdit)
        self.label_4.setBuddy(self.noteLineEdit)

        self.retranslateUi(MainWindow)
        self.cliComboBox.setCurrentIndex(-1)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateEdit, self.fattLineEdit)
        MainWindow.setTabOrder(self.fattLineEdit, self.tipoFattComboBox)
        MainWindow.setTabOrder(self.tipoFattComboBox, self.cliComboBox)
        MainWindow.setTabOrder(self.cliComboBox, self.tipoPagLineEdit)
        MainWindow.setTabOrder(self.tipoPagLineEdit, self.cauLineEdit)
        MainWindow.setTabOrder(self.cauLineEdit, self.noteLineEdit)
        MainWindow.setTabOrder(self.noteLineEdit, self.sTableView)
        MainWindow.setTabOrder(self.sTableView, self.copiaIntCheckBox)
        MainWindow.setTabOrder(self.copiaIntCheckBox, self.copiaCliCheckBox)
        MainWindow.setTabOrder(self.copiaCliCheckBox, self.copiaVettCheckBox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gestione Fatture", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("MainWindow", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Stampa Fattura", None, QtGui.QApplication.UnicodeUTF8))
        self.copiaVettCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Copia Vettore", None, QtGui.QApplication.UnicodeUTF8))
        self.copiaCliCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Copia Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.copiaIntCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Copia Interna", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "N.Fatt:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Tipo Fattura:", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoFattComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Fattura Normale", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoFattComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Fattura Accompagnatoria", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoFattComboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Nota di Accredito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Pagamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Causale:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Note:", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Tools.setTitle(QtGui.QApplication.translate("MainWindow", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&Aiuto", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_File.setText(QtGui.QApplication.translate("MainWindow", "&Nuovo Database", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_File.setText(QtGui.QApplication.translate("MainWindow", "&Carica Database", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Esci", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Add_Customers.setText(QtGui.QApplication.translate("MainWindow", "&Aggiungi Cliente", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc