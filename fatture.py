#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import os
import sys
import subprocess

from PyQt4.QtCore import PYQT_VERSION_STR, QDate, QFile
from PyQt4.QtCore import QRegExp, QString, QVariant, Qt
from PyQt4.QtCore import SIGNAL, QModelIndex, QSettings
from PyQt4.QtCore import QSize, QPoint

from PyQt4.QtGui  import QApplication, QCursor, QDateEdit
from PyQt4.QtGui  import QDialog, QMainWindow, QHBoxLayout
from PyQt4.QtGui  import QLabel, QLineEdit, QMessageBox, QPixmap
from PyQt4.QtGui  import QTabWidget, QPushButton, QRegExpValidator
from PyQt4.QtGui  import QStyleOptionViewItem, QTableView, QVBoxLayout
from PyQt4.QtGui  import QDataWidgetMapper, QTextDocument, QStyle
from PyQt4.QtGui  import QColor, QBrush, QTextOption
from PyQt4.QtGui  import QItemSelectionModel,QStandardItemModel
from PyQt4.QtGui  import QAbstractItemView, QIntValidator
from PyQt4.QtGui  import QDoubleValidator, QIcon, QFileDialog, QItemDelegate

from PyQt4.QtSql  import QSqlDatabase, QSqlQuery, QSqlRelation
from PyQt4.QtSql  import QSqlRelationalDelegate, QSqlRelationalTableModel
from PyQt4.QtSql  import QSqlTableModel

import fatture_ui
import aboutfatt

# Definizione 6 righe intestazione ditta
r1 = "TIME di Stefano Zamprogno"                        # ragione sociale
r2 = "Via A.Bonetto, 6 31044 Montebelluna (TV)"         # es. indirizzo
r3 = "Cod.Fisc. ZMPSFN66T26F443D"                       # es. Codice Fiscale
r4 = "P.IVA: 02297230266 Reg. Impr. TV n'131843"        # es. Partita Iva
r5 = "Tel. 04231900335"                                 # es. telefono

# Definizione degli 'id' usati poi come colonne nelle tabelle ecc...
MID, MDATA, MDOC, MIDTDOC, MIDCLI, MPAG, MCAU, MNOTE = range(8)
SID, SQT, SDESC, SIMP, SIVA, SMID = range(6)
CID, CRAGSOC, CIND, CPIVA, CCF, CTEL, CFAX, CCELL, CEMAIL = range(9)

DATEFORMAT = "dd/MM/yyyy"

# usate per il salvataggio dei settings dell'applicazione
FATTORG = "TIME di Stefano Z."
FATTAPP = "Gestione FATT"
FATTDOMAIN = "zamprogno.it"

class MyQSqlTableModel(QSqlTableModel):
    def __init__(self, parent=None):
        super(MyQSqlTableModel, self).__init__(parent)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        column = index.column()
        if role == Qt.DisplayRole:
            if column == SIMP:
                return QVariant("€ %.2f" %
                        QSqlTableModel.data(self, index).toDouble()[0])
            elif column == SIVA:
                return QVariant("%.2f %%" %
                        QSqlTableModel.data(self, index).toDouble()[0])

        if role == Qt.TextAlignmentRole:
            return QVariant(int(Qt.AlignRight|Qt.AlignVCenter))

        # default, no specific condition found
        return QSqlTableModel.data(self, index, role)


class MyQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyQLineEdit, self).__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.emit(SIGNAL("keyDownPressEvent()"))
            return
        return QLineEdit.keyPressEvent(self, event)

class MyQSqlRelationalDelegate(QSqlRelationalDelegate):
    def __init__(self, parent=None):
        super(MyQSqlRelationalDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        if index.column() == SQT:
            editor = MyQLineEdit(parent)
            validator = QIntValidator(self)
            editor.setValidator(validator)
            editor.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.connect(editor, SIGNAL("keyDownPressEvent()"),
                        self.gestEvt)
            return editor
        elif index.column() == SIMP:
            editor = MyQLineEdit(parent)
            validator = QDoubleValidator(self)
            validator.setDecimals(3)
            editor.setValidator(validator)
            editor.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.connect(editor, SIGNAL("keyDownPressEvent()"),
                        self.gestEvt)
            return editor
        elif index.column() == SIVA:
            editor = MyQLineEdit(parent)
            validator = QDoubleValidator(self)
            validator.setDecimals(3)
            editor.setValidator(validator)
            editor.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.connect(editor, SIGNAL("keyDownPressEvent()"),
                        self.gestEvt)
            return editor
        elif index.column() == SDESC:
            editor = MyQLineEdit(parent)
            editor.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.connect(editor, SIGNAL("keyDownPressEvent()"),
                        self.gestEvt)
            return editor

        editor = QSqlRelationalDelegate.createEditor(self, parent,
                                                    option, index)
        return editor

    def setModelData(self, editor, model, index):
        if index.column() == SIVA:
            model.setData(index, QVariant(editor.text().replace(',', '.')))
        elif index.column() == SIMP:
            model.setData(index, QVariant(editor.text().replace(',', '.')))
        else:
            QSqlRelationalDelegate.setModelData(self, editor, model, index)

    def gestEvt(self):
        editor = self.sender()
        if isinstance(editor, (MyQLineEdit)):
            self.emit(SIGNAL("commitData(QWidget*)"), editor)
            self.emit(SIGNAL("addDettRecord()"))

class MainWindow(QMainWindow, fatture_ui.Ui_MainWindow):

    FIRST, PREV, NEXT, LAST = range(4)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setupMenu()
        self.restoreWinSettings()

        self.editindex = None
        self.filename = None
        self.db = QSqlDatabase.addDatabase("QSQLITE")

        self.loadInitialFile()
        self.setupUiSignals()

    def mmUpdate(self):
        row = self.mapper.currentIndex()
        id = self.mModel.data(self.mModel.index(row,MID)).toString()
        self.sModel.setFilter("mmid=%s" % id)
        self.sModel.select()
        self.sTableView.setColumnHidden(SID, True)
        self.sTableView.setColumnHidden(SMID, True)


    def addDdtRecord(self):
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return
        row = self.mModel.rowCount()
        self.mapper.submit()
        self.mModel.insertRow(row)
        self.mapper.setCurrentIndex(row)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setFocus()
        self.mmUpdate()

    def delDdtRecord(self):
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return
        row = self.mapper.currentIndex()
        if row == -1:
            self.statusbar.showMessage(
                        "Nulla da cancellare...",
                        5000)
            return
        record = self.mModel.record(row)
        id = record.value(MID).toInt()[0]
        fatt = record.value(MDOC).toString()
        if(QMessageBox.question(self, "Cancella Scaffale",
                    "Vuoi cancellare il ddt N': {0} ?".format(fatt),
                    QMessageBox.Yes|QMessageBox.No) ==
                    QMessageBox.No):
            self.statusbar.showMessage(
                        "Cancellazione ddt annullata...",
                        5000)
            return
        # cancella scaffale
        self.mModel.removeRow(row)
        self.mModel.submitAll()
        if row + 1 >= self.mModel.rowCount():
            row = self.mModel.rowCount() - 1
        self.mapper.setCurrentIndex(row)
        if self.mModel.rowCount() == 0:
            self.cauLineEdit.setText(QString(""))
            self.noteLineEdit.setText(QString(""))
            self.ddtLineEdit.setText(QString(""))
            self.cliComboBox.setCurrentIndex(-1)

        # cancella tutti gli articoli che si riferiscono
        # allo scaffale cancellato
        self.sModel.setFilter("mmid=%s" % id)
        self.sModel.select()
        self.sModel.removeRows(0, self.sModel.rowCount())
        self.sModel.submitAll()
        self.statusbar.showMessage(
                        "Cancellazione eseguita...",
                        5000)
        self.mmUpdate()

    def addDettRecord(self):
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return
        rowfatt = self.mapper.currentIndex()
        record = self.mModel.record(rowfatt)
        masterid = record.value(MID).toInt()[0]
        if masterid < 1:
            self.statusbar.showMessage(
                "Scaffale non valido o non confermato...",
                5000)
            self.dateEdit.setFocus()
            return
        # aggiunge la nuova riga alla vista
        self.sModel.submitAll()
        self.sModel.select()
        row = self.sModel.rowCount()
        self.sModel.insertRow(row)
        self.sModel.setData(self.sModel.index(row, SMID),
                                                QVariant(masterid))
        self.sModel.setData(self.sModel.index(row, SQT),
                                                QVariant(1))
        self.sModel.setData(self.sModel.index(row, SDESC),
                                                QVariant(""))
        self.sModel.setData(self.sModel.index(row, SIMP),
                                                QVariant(0.0))
        self.sModel.setData(self.sModel.index(row, SIVA),
                                                QVariant(20.0))
        self.editindex = self.sModel.index(row, SQT)
        self.sTableView.setCurrentIndex(self.editindex)
        self.sTableView.edit(self.editindex)

    def delDettRecord(self):
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return
        selrows = self.sItmSelModel.selectedRows()
        if not selrows:
            self.statusbar.showMessage(
                "No articles selected to delete...",
                5000)
            return
        if(QMessageBox.question(self, "Cancellazione righe",
                "Vuoi cancellare: {0} righe?".format(len(selrows)),
                QMessageBox.Yes|QMessageBox.No) ==
                QMessageBox.No):
            return
        QSqlDatabase.database().transaction()
        query = QSqlQuery()
        query.prepare("DELETE FROM fattslave WHERE id = :val")
        for i in selrows:
            if i.isValid():
                query.bindValue(":val", QVariant(i.data().toInt()[0]))
                query.exec_()
        QSqlDatabase.database().commit()
        self.sModel.revertAll()
        self.mmUpdate()


    def setupMenu(self):
        # AboutBox
        self.connect(self.action_About, SIGNAL("triggered()"),
                    self.showAboutBox)
        # FileNew
        self.connect(self.action_New_File, SIGNAL("triggered()"),
                    self.newFile)

        # FileLoad
        self.connect(self.action_Load_File, SIGNAL("triggered()"),
                    self.openFile)

    #~ def editEsc(self, idxcur, idxold):
        #~ if self.editindex and self.editindex.isValid():
            #~ print(idxcur.row(), idxold.row(), self.editindex.row())
            #~ if idxcur.row() != self.editindex.row():
                #~ #self.sModel.submitAll()
                #~ self.editindex = None

    def showAboutBox(self):
        dlg = aboutfatt.AboutBox(self)
        dlg.exec_()

    def creaStrutturaDB(self):
        query = QSqlQuery()
        if not ("tipofatt" in self.db.tables()):
            if not query.exec_("""CREATE TABLE tipofatt (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        tfatt VARCHAR(50) NOT NULL)"""):
                QMessageBox.warning(self, "Gestione Fatture",
                                QString("Creazione tabella tipofatt fallita!"))
                return False
            else:
                # aggiungi voci !!!!
                query.exec_("""INSERT INTO tipofatt
                            VALUES (NULL,'Fattura Semplice')""")
                query.exec_("""INSERT INTO tipofatt
                            VALUES (NULL,'Fattura Accompagnatoria')""")
                query.exec_("""INSERT INTO tipofatt
                            VALUES (NULL,'Nota Accredito')""")


        if not ("fattmaster" in self.db.tables()):
            if not query.exec_("""CREATE TABLE fattmaster (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        data DATE NOT NULL,
                        doc VARCHAR(50) NOT NULL,
                        idtdoc INTEGER NOT NULL,
                        idcli INTEGER NOT NULL,
                        tpag VARCHAR(50) NOT NULL DEFAULT 'Contanti',
                        causale VARCHAR(200),
                        note VARCHAR(200))"""):
                QMessageBox.warning(self, "Gestione Fatture",
                                QString("Creazione tabella master fallita!"))
                return False

        if not ("fattslave" in self.db.tables()):
            if not query.exec_("""CREATE TABLE fattslave (
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                qt INTEGER NOT NULL DEFAULT '1',
                                desc VARCHAR(200) NOT NULL,
                                imp DOUBLE NOT NULL DEFAULT '0.0',
                                iva DOUBLE NOT NULL DEFAULT '20.0',
                                mmid INTEGER NOT NULL,
                                FOREIGN KEY (mmid) REFERENCES master)"""):
                QMessageBox.warning(self, "Gestione Fatture",
                                QString("Creazione tabella slave fallita!"))
                return False
            QMessageBox.information(self, "Gestione Fatture",
                                QString("Database Creato!"))
            return True


        if not ("clienti" in self.db.tables()):
            if not query.exec_("""CREATE TABLE clienti (
                                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                ragsoc VARCHAR(200) NOT NULL,
                                indirizzo VARCHAR(200) NOT NULL,
                                piva VARCHAR(15),
                                cf VARCHAR(15),
                                tel VARCHAR(30),
                                fax VARCHAR(30),
                                cell VARCHAR(30),
                                email VARCHAR(50))"""):
                QMessageBox.warning(self, "Gestione Fatture",
                                QString("Creazione tabella clienti fallita!"))
                return False
        return True

    def loadFile(self, fname=None):
        if fname is None:
            return
        if self.db.isOpen():
            self.db.close()
        self.db.setDatabaseName(QString(fname))
        if not self.db.open():
            QMessageBox.warning(self, "Gestione Fatture",
                                QString("Database Error: %1")
                                .arg(db.lastError().text()))
        else:
            if not self.creaStrutturaDB():
                return
            self.filename = unicode(fname)
            self.setWindowTitle("Gestione Fatture - %s" % self.filename)
            self.setupModels()
            self.setupMappers()
            self.setupTables()
            #self.setupItmSignals()
            self.restoreTablesSettings()
            self.mmUpdate()


    def loadInitialFile(self):
        settings = QSettings()
        fname = unicode(settings.value("Settings/lastFile").toString())
        if fname and QFile.exists(fname):
            self.loadFile(fname)


    def openFile(self):
        dir = os.path.dirname(self.filename) \
                if self.filename is not None else "."
        fname = QFileDialog.getOpenFileName(self,
                    "Gestione Fatture - Scegli database",
                    dir, "*.db")
        if fname:
            self.loadFile(fname)


    def newFile(self):
        dir = os.path.dirname(self.filename) \
                if self.filename is not None else "."
        fname = QFileDialog.getSaveFileName(self,
                    "Gestione Fatture - Scegli database",
                    dir, "*.db")
        if fname:
            self.loadFile(fname)

    def restoreWinSettings(self):
        settings = QSettings()
        self.restoreGeometry(
                settings.value("MainWindow/Geometry").toByteArray())

    def restoreTablesSettings(self):
        settings = QSettings(self)
        # per la tablelview
        for column in range(1, self.sModel.columnCount()-1):
            width = settings.value("Settings/sTableView/%s" % column,
                                    QVariant(60)).toInt()[0]
            self.sTableView.setColumnWidth(column,
                                        width if width > 0 else 60)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Down:
            self.addDettRecord()
        else:
            QMainWindow.keyPressEvent(self, event)

    def closeEvent(self, event):
        self.mapper.submit()
        settings = QSettings()
        settings.setValue("MainWindow/Geometry", QVariant(
                          self.saveGeometry()))
        if self.filename is not None:
            settings.setValue("Settings/lastFile", QVariant(self.filename))
        if self.db.isOpen():
            # salva larghezza colonne tabella
            for column in range(1, self.sModel.columnCount()-1):
                width = self.sTableView.columnWidth(column)
                if width:
                    settings.setValue("Settings/sTableView/%s" % column,
                                        QVariant(width))
            self.db.close()
            del self.db

    def setupModels(self):
        """
            Initialize all the application models
        """
        # setup slaveModel
        self.sModel = MyQSqlTableModel(self)
        self.sModel.setTable(QString("fattslave"))
        self.sModel.setHeaderData(SID, Qt.Horizontal, QVariant("ID"))
        self.sModel.setHeaderData(SQT, Qt.Horizontal, QVariant("Qt"))
        self.sModel.setHeaderData(SDESC, Qt.Horizontal, QVariant("Descrizione"))
        self.sModel.setHeaderData(SIMP, Qt.Horizontal, QVariant("Importo"))
        self.sModel.setHeaderData(SIVA, Qt.Horizontal, QVariant("Iva"))
        self.sModel.setHeaderData(SMID, Qt.Horizontal, QVariant("idlegato"))
        self.sModel.setEditStrategy(QSqlTableModel.OnRowChange)
        self.sModel.select()

        # setup masterModel
        self.mModel = QSqlRelationalTableModel(self)
        self.mModel.setTable(QString("fattmaster"))
        #~ self.mModel.setHeaderData(MID, Qt.Horizontal, QVariant("ID"))
        #~ self.mModel.setHeaderData(MDATA, Qt.Horizontal, QVariant("Data"))
        #~ self.mModel.setHeaderData(MDOC, Qt.Horizontal, QVariant("Numero Fatt."))
        #~ self.mModel.setHeaderData(MIDTDOC, Qt.Horizontal, QVariant("Tipo Fatt."))
        #~ self.mModel.setHeaderData(MIDCLI, Qt.Horizontal, QVariant("Cliente"))
        #~ self.mModel.setHeaderData(MPAG, Qt.Horizontal, QVariant("Pagamento"))
        #~ self.mModel.setHeaderData(MCAU, Qt.Horizontal, QVariant("Causale"))
        #~ self.mModel.setHeaderData(MNOTE, Qt.Horizontal, QVariant("Note"))
        self.mModel.setSort(MDATA, Qt.AscendingOrder)
        self.mModel.setRelation(MIDCLI, QSqlRelation("clienti",
                                            "id", "ragsoc"))
        self.mModel.setRelation(MIDTDOC, QSqlRelation("tipofatt",
                                            "id", "tfatt"))
        self.mModel.select()

        # setup clientiModel
        self.cModel = QSqlTableModel(self)
        self.cModel.setTable(QString("clienti"))
        #~ self.cModel.setHeaderData(CID, Qt.Horizontal, QVariant("ID"))
        #~ self.cModel.setHeaderData(CRAGSOC, Qt.Horizontal, QVariant("RagSoc"))
        #~ self.cModel.setHeaderData(CIND, Qt.Horizontal, QVariant("Indirizzo"))
        #~ self.cModel.setHeaderData(CPIVA, Qt.Horizontal, QVariant("PIva"))
        #~ self.cModel.setHeaderData(CCF, Qt.Horizontal, QVariant("CF"))
        #~ self.cModel.setHeaderData(CTEL, Qt.Horizontal, QVariant("Tel"))
        #~ self.cModel.setHeaderData(CFAX, Qt.Horizontal, QVariant("Fax"))
        #~ self.cModel.setHeaderData(CCELL, Qt.Horizontal, QVariant("Cell"))
        #~ self.cModel.setHeaderData(CEMAIL, Qt.Horizontal, QVariant("EMail"))
        self.cModel.select()

    def setupMappers(self):
        '''
            Initialize all the application mappers
        '''
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.mModel)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.dateEdit, MDATA)
        self.mapper.addMapping(self.fattLineEdit, MDOC)

        relationModel = self.mModel.relationModel(MIDTDOC)
        self.tipoFattComboBox.setModel(relationModel)
        self.tipoFattComboBox.setModelColumn(relationModel.fieldIndex("tfatt"))
        self.mapper.addMapping(self.tipoFattComboBox, MIDTDOC)

        relationModel = self.mModel.relationModel(MIDCLI)
        self.cliComboBox.setModel(relationModel)
        self.cliComboBox.setModelColumn(relationModel.fieldIndex("ragsoc"))
        self.mapper.addMapping(self.cliComboBox, MIDCLI)

        self.mapper.addMapping(self.tipoPagLineEdit, MPAG)
        self.mapper.addMapping(self.cauLineEdit, MCAU)
        self.mapper.addMapping(self.noteLineEdit, MNOTE)
        self.mapper.toFirst()

    def setupTables(self):
        """
            Initialize all the application tablesview
        """
        self.sTableView.setModel(self.sModel)
        self.sTableView.setColumnHidden(SID, True)
        self.sTableView.setColumnHidden(SMID, True)
        self.sTableView.setWordWrap(True)
        self.sTableView.resizeRowsToContents()
        self.sTableView.setAlternatingRowColors(True)
        self.sItmSelModel = QItemSelectionModel(self.sModel)
        self.sTableView.setSelectionModel(self.sItmSelModel)
        self.sTableView.setSelectionBehavior(QTableView.SelectRows)
        self.sTableView.setTabKeyNavigation(False)
        self.myDelegate = MyQSqlRelationalDelegate(self)
        self.sTableView.setItemDelegate(self.myDelegate)
        self.connect(self.myDelegate, SIGNAL("addDettRecord()"),
            self.addDettRecord)

    def setupUiSignals(self):
        self.connect(self.printPushButton, SIGNAL("clicked()"),
                    self.printFatt)
        self.connect(self.addMPushButton, SIGNAL("clicked()"),
                    self.addDdtRecord)
        self.connect(self.delMPushButton, SIGNAL("clicked()"),
                    self.delDdtRecord)
        self.connect(self.addSPushButton, SIGNAL("clicked()"),
                    self.addDettRecord)
        self.connect(self.delSPushButton, SIGNAL("clicked()"),
                    self.delDettRecord)
        self.connect(self.firstMPushButton, SIGNAL("clicked()"),
                    lambda: self.saveRecord(MainWindow.FIRST))
        self.connect(self.prevMPushButton, SIGNAL("clicked()"),
                    lambda: self.saveRecord(MainWindow.PREV))
        self.connect(self.nextMPushButton, SIGNAL("clicked()"),
                    lambda: self.saveRecord(MainWindow.NEXT))
        self.connect(self.lastMPushButton, SIGNAL("clicked()"),
                    lambda: self.saveRecord(MainWindow.LAST))

    def saveRecord(self, where):
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return
        row = self.mapper.currentIndex()
        self.mapper.submit()
        self.sModel.revertAll()
        if where == MainWindow.FIRST:
            row=0
        elif where == MainWindow.PREV:
            row = 0 if row <= 1 else row - 1
        elif where == MainWindow.NEXT:
            row += 1
            if row >= self.mModel.rowCount():
                row = self.mModel.rowCount() -1
        elif where == MainWindow.LAST:
            row = self.mModel.rowCount()- 1
        self.mapper.setCurrentIndex(row)
        self.mmUpdate()

    def printFatt(self):
        '''
            Print Inventory
        '''
        if not self.db.isOpen():
            self.statusbar.showMessage(
                "Database non aperto...",
                5000)
            return

        def makeFATT(copia="Copia Cliente"):
            qmaster = QSqlQuery()
            qcli = QSqlQuery()
            qslave = QSqlQuery()

            curidx = self.mapper.currentIndex()
            currec = self.mModel.record(curidx)
            masterid = currec.value("id").toInt()[0]

            qmaster.exec_("SELECT id,data,doc,idtdoc,idcli,causale,note "
                        "FROM fattmaster WHERE doc = %s" % (currec.value("doc").toString()))
            qmaster.next()
            curcli = qmaster.value(4).toInt()[0]
            qcli.exec_("SELECT id,ragsoc,indirizzo,piva "
                        "FROM clienti WHERE id = %d" % (curcli))
            qslave.exec_("SELECT mmid,qt,desc,imp,iva "
                            "FROM fattslave WHERE mmid = %s" % (masterid))

            qcli.next()
            # variabili utili alla stampa del report
            datadoc = currec.value("data").toDate().toString(DATEFORMAT)
            causaledoc = currec.value("causale").toString()
            notedoc = currec.value("note").toString()
            tipodoc = currec.value(3).toString()
            numdoc = currec.value("doc").toString()
            cliragsoc = qcli.value(1).toString()
            cliind = qcli.value(2).toString()
            clipiva = qcli.value(3).toString()

            from reportlab.pdfgen.canvas import Canvas
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import cm
            from reportlab.lib.enums import TA_LEFT,TA_RIGHT,TA_CENTER
            from reportlab.platypus import Spacer, SimpleDocTemplate, Table, TableStyle, Paragraph, KeepTogether
            from reportlab.rl_config import defaultPageSize
            from reportlab.lib import colors
            from reportlab.lib.pagesizes import letter, A4
            from reportlab.lib import textsplit

            PAGE_WIDTH, PAGE_HEIGHT=defaultPageSize
            styles = getSampleStyleSheet()
            styleN = styles['Normal']
            styleH = styles['Heading1']
            styleH.alignment=TA_CENTER
            Elements = []
            #add some flowables
            p=Paragraph
            ps=ParagraphStyle

            Author = "Stefano Zamprogno"
            URL = "http://www.zamprogno.it/"
            email = "time@zamprogno.it"

            pageinfo = "%s / %s" % (Author, email)

            def myLaterPages(c, doc):
                c.saveState()
                c.setFont("Times-Bold", 82)
                c.rotate(45)
                c.setFillColorRGB(0.9,0.9,0.9)
                c.drawString(11*cm,2*cm, copia)
                c.rotate(-45)
                c.setFillColorRGB(0,0,0)
                # HEADER
                if tipodoc == "Fattura Accompagnatoria":
                    subt = 0
                else:
                    subt = 3
                c.setLineWidth(0.1*cm)
                c.setStrokeColorRGB(0,0,0)
                c.line(1.8*cm,(6.2-subt)*cm,19.5*cm,(6.2-subt)*cm)
                c.setStrokeColorRGB(0.5,0.5,0.5)
                c.line(1.9*cm,(6.1-subt)*cm,19.6*cm,(6.1-subt)*cm)
                # cerchi carta
                c.circle(0.9*cm,6*cm,0.3*cm, fill=1)
                c.circle(0.9*cm,24*cm,0.3*cm, fill=1)
                c.setFont("Times-Bold", 14)
                c.drawCentredString(5*cm, 28*cm, r1)
                c.setFont("Times-Bold", 9)
                c.drawCentredString(5*cm, 27.5*cm, r2)
                c.drawCentredString(5*cm, 27*cm, r3)
                c.drawCentredString(5*cm, 26.5*cm, r4)
                c.drawCentredString(5*cm, 26*cm, r5)
                # numero ddt e descrizione copia
                c.setFont("Times-Bold", 12)
                c.drawCentredString(18*cm, 28*cm, "DOC N: %s" % (numdoc))
                c.setFont("Times-Bold", 7)
                c.drawCentredString(18*cm, 27.6*cm, "(%s)" % (copia))
                c.drawCentredString(18*cm, 27.2*cm, "%s" % (tipodoc.toUpper()))
                # Data e causale
                c.setFont("Times-Bold", 10)
                c.drawString(1.8*cm, 25*cm, "Data:")
                c.drawString(1.8*cm, 24.5*cm, "Causale:")
                c.setFont("Times-Roman", 10)
                c.drawString(4*cm, 25*cm, unicode(datadoc))
                c.drawString(4*cm, 24.5*cm, unicode(causaledoc))
                # Cliente
                c.setFont("Times-Bold", 10)
                c.drawString(11*cm, 25*cm, "Destinatario:")
                c.setFont("Times-Roman", 10)
                c.drawCentredString(16*cm, 25*cm, unicode(cliragsoc))
                c.drawCentredString(16*cm, 24.5*cm, unicode(cliind))
                c.drawCentredString(16*cm, 24*cm, unicode(clipiva))
                # FOOTER
                c.setFont("Times-Bold", 10)
                c.setLineWidth(0.01*cm)
                c.drawString(1.8*cm, (5.5-subt)*cm, "Note:")
                c.setFont("Times-Roman", 10)
                strt = (5.5-subt)*cm
                for i in textsplit.wordSplit(unicode(notedoc),6*cm,
                                            "Times-Roman", 10):
                    c.drawString(3*cm, strt, i[1])
                    strt -= 0.5*cm
                if tipodoc == "Fattura Accompagnatoria":
                    c.setFont("Times-Bold", 10)
                    c.drawString(12*cm, 5.5*cm, "Data inizio trasporto:")
                    c.line(15.5*cm,5.4*cm,19*cm,5.4*cm)
                    c.drawString(12*cm, 5*cm, "Aspetto dei beni:")
                    c.line(15*cm,4.9*cm,19*cm,4.9*cm)
                    c.drawString(12*cm, 4.5*cm, "Numero colli:")
                    c.line(15*cm,4.4*cm,19*cm,4.4*cm)
                    c.drawString(12*cm, 3.8*cm, "Conducente:")
                    c.line(15*cm,3.7*cm,19*cm,3.7*cm)
                    c.drawString(12*cm, 3*cm, "Destinatario:")
                    c.line(15*cm,2.9*cm,19*cm,2.9*cm)
                    c.drawString(1.8*cm, 4*cm, "Trasporto a Mezzo:")
                    c.line(2.3*cm,3*cm,7*cm,3*cm)
                # note pie' pagina
                c.setFont('Times-Roman',9)
                c.drawString(12.4*cm, 1.5*cm, "Pagina %d %s" % (doc.page, pageinfo))
                c.restoreState()

            # crea il body del ddt
            data = [['Qt', 'Descrizione dei beni, natura e qualità',
                     'Importo', 'IVA'],]

            totimp = 0
            totiva = 0
            totesiva = 0
            while qslave.next():
                if qslave.value(4).toDouble()[0]!= 0:
                    totimp += qslave.value(3).toDouble()[0]
                    totiva += (qslave.value(3).toDouble()[0]*
                                qslave.value(4).toDouble()[0] / 100.0)
                else:
                    totesiva += qslave.value(3).toDouble()[0]

                data.append([qslave.value(1).toInt()[0],
                            p(unicode(qslave.value(2).toString()),
                                ps(name='Normal')),
                            "€ %.2f" % qslave.value(3).toDouble()[0],
                            "%.2f %%" % qslave.value(4).toDouble()[0]])

            Elements.append(Table(data,colWidths=(1*cm,12.5*cm,2*cm,2*cm),repeatRows=1,
                                style=(
                                        ['LINEBELOW', (0,0), (-1,0),
                                            1, colors.black],
                                        ['BACKGROUND',(0,0),(-1,0),
                                            colors.lightgrey],
                                        ['GRID',(0,0),(-1,-1), 0.2,
                                            colors.black],
                                        ['FONT', (0, 0), (-1, 0),
                                            'Helvetica-Bold', 10],
                                        ['VALIGN', (0,0), (-1,-1), 'TOP'],
                                        ['ALIGN', (0,0), (-1,0), 'CENTER'],
                                        ['ALIGN', (2,1), (3,-1), 'RIGHT'],

                                )))

            summary = []
            summary.append(Spacer(0.5*cm, 0.5*cm))
            summary.append(Paragraph("<para align=right><b>___________________________________"
                            "</b></para>", styleN))
            summary.append(Paragraph("<para align=right><b>TOTALE IMPONIBILE: "
                            "€ %.2f</b></para>" % totimp, styleN))
            summary.append(Paragraph("<para align=right><b>TOTALE IVA: "
                            "€ %.2f</b></para>" % totiva, styleN))
            summary.append(Paragraph("<para align=right><b>TOTALE Es.IVA: "
                            "€ %.2f</b></para>" % totesiva, styleN))
            summary.append(Spacer(0.5*cm, 0.5*cm))
            summary.append(Paragraph("<para align=right><b>TOTALE GENERALE: "
                            "€ %.2f</b></para>" % (totesiva+totimp+totiva), styleN))
            Elements.append(KeepTogether(summary))

            # 'depure' numddt
            numdoc = numdoc.replace("/",".")
            if tipodoc == "Fattura Accompagnatoria":
                doc = SimpleDocTemplate(os.path.join(os.path.dirname(__file__),
                                "fatt%s.%s.pdf" % (numdoc, copia.replace(" ","."))),topMargin=6.2*cm, bottomMargin=6.2*cm)
            else:
                doc = SimpleDocTemplate(os.path.join(os.path.dirname(__file__),
                                "fatt%s.%s.pdf" % (numdoc, copia.replace(" ","."))),topMargin=6.2*cm, bottomMargin=3*cm)

            doc.build(Elements,onFirstPage=myLaterPages,onLaterPages=myLaterPages)

            subprocess.call(['gnome-open',os.path.join(os.path.dirname(__file__),
                            "fatt%s.%s.pdf" % (numdoc, copia.replace(" ",".")))])

        if self.copiaCliCheckBox.isChecked():
            makeFATT()
        if self.copiaIntCheckBox.isChecked():
            makeFATT(copia="Copia Interna")
        if self.copiaVettCheckBox.isChecked():
            makeFATT(copia="Copia Vettore")

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName(FATTORG)
    app.setOrganizationDomain(FATTDOMAIN)
    app.setApplicationName(FATTAPP)

    form = MainWindow()
    form.show()
    form.raise_()
    app.exec_()
    del form

main()
