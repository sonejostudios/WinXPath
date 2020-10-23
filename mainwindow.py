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
        MainWindow.resize(739, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMaximumSize(QSize(16777215, 340))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
#ifndef Q_OS_MAC
        self.verticalLayout_5.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
#endif
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_3.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#endif
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.win_prefix_box = QComboBox(self.widget)
        self.win_prefix_box.setObjectName(u"win_prefix_box")
        self.win_prefix_box.setMinimumSize(QSize(60, 30))
        self.win_prefix_box.setMaximumSize(QSize(60, 16777215))
        self.win_prefix_box.setEditable(True)

        self.verticalLayout.addWidget(self.win_prefix_box)

        self.clear_btn = QPushButton(self.widget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setMinimumSize(QSize(60, 30))
        self.clear_btn.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout.addWidget(self.clear_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.path_field = QPlainTextEdit(self.widget)
        self.path_field.setObjectName(u"path_field")
        self.path_field.setMaximumSize(QSize(16777215, 70))
        self.path_field.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.horizontalLayout.addWidget(self.path_field)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.check_prefix_dict = QCheckBox(self.widget)
        self.check_prefix_dict.setObjectName(u"check_prefix_dict")

        self.horizontalLayout_2.addWidget(self.check_prefix_dict)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_custom_prefix = QLabel(self.widget)
        self.label_custom_prefix.setObjectName(u"label_custom_prefix")
        self.label_custom_prefix.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_custom_prefix)

        self.prefix_box = QComboBox(self.widget)
        self.prefix_box.setObjectName(u"prefix_box")
        self.prefix_box.setMinimumSize(QSize(200, 30))
        self.prefix_box.setEditable(True)

        self.horizontalLayout_2.addWidget(self.prefix_box)

        self.convert_space_box = QCheckBox(self.widget)
        self.convert_space_box.setObjectName(u"convert_space_box")

        self.horizontalLayout_2.addWidget(self.convert_space_box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.converted_path_field = QPlainTextEdit(self.widget)
        self.converted_path_field.setObjectName(u"converted_path_field")
        self.converted_path_field.setMaximumSize(QSize(16777215, 70))
        self.converted_path_field.setLineWrapMode(QPlainTextEdit.WidgetWidth)

        self.verticalLayout_3.addWidget(self.converted_path_field)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.path_check_label = QLabel(self.widget)
        self.path_check_label.setObjectName(u"path_check_label")

        self.verticalLayout_2.addWidget(self.path_check_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.add_fav_btn = QPushButton(self.widget)
        self.add_fav_btn.setObjectName(u"add_fav_btn")
        self.add_fav_btn.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_3.addWidget(self.add_fav_btn)

        self.copy_btn = QPushButton(self.widget)
        self.copy_btn.setObjectName(u"copy_btn")
        self.copy_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.copy_btn)

        self.open_btn = QPushButton(self.widget)
        self.open_btn.setObjectName(u"open_btn")
        self.open_btn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.open_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addWidget(self.widget)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label)

        self.fav_list_widget = QListWidget(self.centralwidget)
        self.fav_list_widget.setObjectName(u"fav_list_widget")
        sizePolicy.setHeightForWidth(self.fav_list_widget.sizePolicy().hasHeightForWidth())
        self.fav_list_widget.setSizePolicy(sizePolicy)
        self.fav_list_widget.setMinimumSize(QSize(0, 80))

        self.verticalLayout_6.addWidget(self.fav_list_widget)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 20))
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
        self.label_custom_prefix.setText(QCoreApplication.translate("MainWindow", u"Use Custom Prefix:  ", None))
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
        self.add_fav_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Add Path to Favorites", None))
#endif // QT_CONFIG(statustip)
        self.add_fav_btn.setText(QCoreApplication.translate("MainWindow", u"+ Favorite", None))
#if QT_CONFIG(statustip)
        self.copy_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Copy Path to Clipboard", None))
#endif // QT_CONFIG(statustip)
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy to Clipboard", None))
#if QT_CONFIG(statustip)
        self.open_btn.setStatusTip(QCoreApplication.translate("MainWindow", u"Try to open the Path with the configured File Browser", None))
#endif // QT_CONFIG(statustip)
        self.open_btn.setText(QCoreApplication.translate("MainWindow", u"Open Path", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Favorites:", None))
#if QT_CONFIG(statustip)
        self.fav_list_widget.setStatusTip(QCoreApplication.translate("MainWindow", u"Load Favorite: double left click / Delete Favorite: del key", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

