# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import cv2
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QFileDialog, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(2, 2, 471, 96))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.Edit_choose_file = QLineEdit(self.layoutWidget)
        self.Edit_choose_file.setObjectName(u"Edit_choose_file")

        self.horizontalLayout_2.addWidget(self.Edit_choose_file)

        self.btn_choose_file = QPushButton(self.layoutWidget)
        self.btn_choose_file.setObjectName(u"btn_choose_file")
        self.btn_choose_file.clicked.connect(self.choose_file)

        self.horizontalLayout_2.addWidget(self.btn_choose_file)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Edit_save_file = QLineEdit(self.layoutWidget)
        self.Edit_save_file.setObjectName(u"Edit_save_file")

        self.horizontalLayout.addWidget(self.Edit_save_file)

        self.btn_save_file = QPushButton(self.layoutWidget)
        self.btn_save_file.setObjectName(u"btn_save_file")
        self.btn_save_file.clicked.connect(self.save_file)

        self.horizontalLayout.addWidget(self.btn_save_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.btn_start = QPushButton(self.layoutWidget)
        self.btn_start.setObjectName(u"start")
        self.btn_start.clicked.connect(self.start)

        self.verticalLayout.addWidget(self.btn_start)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe\u7247\u8def\u5f84", None))
        self.btn_choose_file.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.btn_save_file.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8...", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316", None))
    # retranslateUi


    def choose_file(self):
        img_name,img_type = QFileDialog.getOpenFileName(None,'选择图片','','*.jpg;;*.png','')
        self.Edit_choose_file.setText(img_name)
    

    def save_file(self):
        img_name,img_type = QFileDialog.getSaveFileName(None,'保存图片','','*.jpg;;*.png','')
        self.Edit_save_file.setText(img_name)


    def start(self):
        try:
            image = cv2.imread(self.Edit_choose_file.text(), cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(self.Edit_save_file.text(), image)
            QMessageBox.information(None,'提示','转换完成')
        except cv2.error as err:
            QMessageBox.warning(None,"警告","路径为空或有误")

