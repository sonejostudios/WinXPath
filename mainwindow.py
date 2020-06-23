# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(694, 329)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.win_prefix_box = QComboBox(self.centralwidget)
        self.win_prefix_box.setObjectName(u"win_prefix_box")
        self.win_prefix_box.setMinimumSize(QSize(60, 30))
        self.win_prefix_box.setMaximumSize(QSize(60, 16777215))
        self.win_prefix_box.setEditable(True)

        self.verticalLayout.addWidget(self.win_prefix_box)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setMinimumSize(QSize(60, 30))
        self.clear_btn.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout.addWidget(self.clear_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.path_field = QPlainTextEdit(self.centralwidget)
        self.path_field.setObjectName(u"path_field")
        self.path_field.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.horizontalLayout.addWidget(self.path_field)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.check_prefix_dict = QCheckBox(self.centralwidget)
        self.check_prefix_dict.setObjectName(u"check_prefix_dict")

        self.horizontalLayout_2.addWidget(self.check_prefix_dict)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_custom_prefix = QLabel(self.centralwidget)
        self.label_custom_prefix.setObjectName(u"label_custom_prefix")
        self.label_custom_prefix.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_custom_prefix)

        self.prefix_box = QComboBox(self.centralwidget)
        self.prefix_box.setObjectName(u"prefix_box")
        self.prefix_box.setMinimumSize(QSize(200, 30))
        self.prefix_box.setEditable(True)

        self.horizontalLayout_2.addWidget(self.prefix_box)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.convert_space_box = QCheckBox(self.centralwidget)
        self.convert_space_box.setObjectName(u"convert_space_box")

        self.horizontalLayout_2.addWidget(self.convert_space_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.converted_path_field = QPlainTextEdit(self.centralwidget)
        self.converted_path_field.setObjectName(u"converted_path_field")
        self.converted_path_field.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.converted_path_field)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.path_check_label = QLabel(self.centralwidget)
        self.path_check_label.setObjectName(u"path_check_label")

        self.verticalLayout_2.addWidget(self.path_check_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.copy_btn)

        self.open_btn = QPushButton(self.centralwidget)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.open_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 694, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.path_field, self.win_prefix_box)
        QWidget.setTabOrder(self.win_prefix_box, self.convert_space_box)
        QWidget.setTabOrder(self.convert_space_box, self.check_prefix_dict)
        QWidget.setTabOrder(self.check_prefix_dict, self.prefix_box)
        QWidget.setTabOrder(self.prefix_box, self.converted_path_field)
        QWidget.setTabOrder(self.converted_path_field, self.copy_btn)
        QWidget.setTabOrder(self.copy_btn, self.open_btn)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WinXPath", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Windows Path:", None))
#if QT_CONFIG(statustip)
        self.win_prefix_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Select a Windows Drive", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.clear_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear Windows Path field", None))
#endif // QT_CONFIG(statustip)
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(statustip)
        self.path_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter Windows Path", None))
#endif // QT_CONFIG(statustip)
        self.path_field.setPlainText(QCoreApplication.translate("MainWindow", u"C:\\", None))
#if QT_CONFIG(statustip)
        self.check_prefix_dict.setStatusTip(QCoreApplication.translate("MainWindow", u"Select between Prefix Dictionary and Custom Prefix", None))
#endif // QT_CONFIG(statustip)
        self.check_prefix_dict.setText(QCoreApplication.translate("MainWindow", u"Use Prefix Dictionary", None))
        self.label_custom_prefix.setText(QCoreApplication.translate("MainWindow", u"Use Custom Prefix:", None))
#if QT_CONFIG(statustip)
        self.prefix_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Select Custom Prefix (only if Use Prefix Dictionary is unchecked)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.convert_space_box.setStatusTip(QCoreApplication.translate("MainWindow", u"Replaces Spaces with %20 (e.g. for Samba shared folders)", None))
#endif // QT_CONFIG(statustip)
        self.convert_space_box.setText(QCoreApplication.translate("MainWindow", u"Replace Spaces with %20", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Unix Path:", None))
#if QT_CONFIG(statustip)
        self.converted_path_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Unix Path Result", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.path_check_label.setStatusTip(QCoreApplication.translate("MainWindow", u"Checks if the Unix Path exists on this computer (it doesn't check network paths)", None))
#endif // QT_CONFIG(statustip)
        self.path_check_label.setText(QCoreApplication.translate("MainWindow", u"Path check", None))
#if QT_CONFIG(statustip)
        self.copy_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Copy Path to Clipboard", None))
#endif // QT_CONFIG(statustip)
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
#if QT_CONFIG(statustip)
        self.open_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Try to open the Path with the configured File Browser", None))
#endif // QT_CONFIG(statustip)
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"Open Path", None))
    # retranslateUi

