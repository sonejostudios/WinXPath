import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QShortcut
from PySide2.QtCore import Qt, QFile
from PySide2.QtGui import QKeySequence

# import mainwindow.py as module and it's main class
from mainwindow import Ui_MainWindow

import config


from pathlib import Path, PureWindowsPath, PurePosixPath
import pyperclip
import webbrowser
import os
import pathlib
import subprocess
import json

import stat



# in PyCharm:
# in Run Configuration, Run Before Launch, add External Tool
# Command: pyside2-uic
# Arguments: mainwindow.ui -o mainwindow.py
# Folder: $ProjectFileDir$




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        # Signals
        #self.ui.convert_btn.clicked.connect(self.onwin2lin)
        self.ui.copy_btn.clicked.connect(self.copy2clipboard)
        self.ui.open_btn.clicked.connect(self.open_path)
        self.ui.clear_btn.clicked.connect(self.clear_win_path)

        self.ui.converted_path_field.textChanged.connect(self.path_check)

        self.ui.prefix_box.currentTextChanged.connect(self.onwin2lin)
        self.ui.win_prefix_box.currentTextChanged.connect(self.set_win_prefix)

        self.ui.path_field.textChanged.connect(self.onwin2lin)
        self.ui.convert_space_box.clicked.connect(self.onwin2lin)

        self.ui.check_prefix_dict.clicked.connect(self.onwin2lin)

        self.ui.add_fav_btn.clicked.connect(self.add_fav)

        self.ui.fav_list_widget.itemDoubleClicked.connect(self.load_fav)

        # delete cmd from cmdlist
        QShortcut(QKeySequence(Qt.Key_Delete), self.ui.fav_list_widget, self.delete_fav)



        # popultate prefix list
        self.ui.prefix_box.clear()
        self.ui.prefix_box.addItem("")

        # add home to prefix list
        self.home = pathlib.Path.home()
        self.ui.prefix_box.addItem(str(self.home))

        # add custom prefix_list from config
        for i in config.prefix_list:
            self.ui.prefix_box.addItem(i)


        # add win prefix list from config
        for i in config.prefix_dict.keys():
            self.ui.win_prefix_box.addItem(i)



        # set config checkboxes
        if config.prefix_dict_checkbox_state == True:
            self.ui.check_prefix_dict.setChecked(True)
        else:
            self.ui.check_prefix_dict.setChecked(False)


        if config.replace_spaces_checkbox_state == True:
            self.ui.convert_space_box.setChecked(True)
        else:
            self.ui.convert_space_box.setChecked(False)



        # create favorite list
        self.favlist = []


        # read favorite file
        self.read_fav_file()


            # start
        self.win2lin()




    def test(self):
        print("test!")





    def load_fav(self):
        winpath = self.ui.fav_list_widget.currentItem().text()
        self.ui.path_field.setPlainText(winpath)


    def add_fav(self):
        # add with path to list
        self.favlist.append(self.ui.path_field.toPlainText())
        self.change_fav_file()


    def delete_fav(self):
        item = self.ui.fav_list_widget.currentItem().text()
        self.favlist.remove(item)
        self.change_fav_file()


    def change_fav_file(self):
        #write fav list
        with open("favs.json", 'w') as f:
            json.dump(self.favlist, f, indent=0)

        # read fav file
        self.read_fav_file()


    def read_fav_file(self):

        # read fav list
        with open("favs.json", 'r') as f:
            self.favlist = json.load(f)

        # populate fav list widget
        self.ui.fav_list_widget.clear()
        self.ui.fav_list_widget.addItems(self.favlist)




    def onwin2lin(self):
        self.win2lin()


    def win2lin(self):
        # path
        path = self.ui.path_field.toPlainText()
        #print(path)
        filename = PureWindowsPath(path)

        # convert to posix
        path_on_linux = PurePosixPath(filename)


        # get drive_letter
        drive_letter = str(path_on_linux)[:2]
        #print(drive_letter)

        # remove drive_letter
        path_on_linux = str(path_on_linux)[3:]

        # replace spaces
        if self.ui.convert_space_box.checkState() == 2:
            path_on_linux = path_on_linux.replace(" ", "%20")


        # add prefix
        if self.ui.check_prefix_dict.checkState() == 0:
            path_on_linux = self.ui.prefix_box.currentText() + path_on_linux
            self.ui.label_custom_prefix.setEnabled(True)
        else:
            lin_prefix = config.prefix_dict[drive_letter]
            path_on_linux = lin_prefix  + path_on_linux
            self.ui.label_custom_prefix.setEnabled(False)


        #print(path_on_linux)
        # put in new path field
        self.ui.converted_path_field.setPlainText(path_on_linux)


        #adjust win path letter
        winpath = self.ui.path_field.toPlainText()
        winpath = winpath[:2]
        self.ui.win_prefix_box.setCurrentText(winpath)






    def set_win_prefix(self):
        winpath = self.ui.path_field.toPlainText()
        winpath = winpath[2:]
        winpath = self.ui.win_prefix_box.currentText() + winpath
        self.ui.path_field.setPlainText(winpath)



    def clear_win_path(self):
        self.ui.path_field.setPlainText("C:\\")



    def copy2clipboard(self):
        print("copied to clipboard!")
        newpath = self.ui.converted_path_field.toPlainText()
        pyperclip.copy(newpath)
        self.ui.statusbar.showMessage("Path copied to Clipboard!")



    def open_path(self):
        new_path = self.ui.converted_path_field.toPlainText()
        #webbrowser.open('file:///' + str(new_path))

        cmd = config.file_browser + " " + new_path
        #print(cmd)
        os.system(cmd)



    def path_check(self):
        new_path = self.ui.converted_path_field.toPlainText()

        if os.path.exists(new_path) == True:
            self.ui.path_check_label.setText("This path exists.")
            #self.ui.open_btn.setEnabled(True)
        else:
            self.ui.path_check_label.setText("This path doesn't exists on this computer.")
            #self.ui.open_btn.setEnabled(False)












if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())