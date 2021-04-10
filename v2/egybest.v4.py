
import ctypes
import os
import sys
import time
import uuid

import pyperclip
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType
from qtpy import QtGui

import core
import threads


def get_correct_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ui, _ = loadUiType(get_correct_path('gui.ui'))


class egybest(QMainWindow, ui, threads.EBThreads, core.EgybestLogic):
    def __init__(self, parent=None):
        super(egybest, self).__init__(parent)
        QMainWindow.__init__(self)
        threads.EBThreads.__init__(self)
        core.EgybestLogic.__init__(self)
        self.url = ""
        self.state = ""
        self.base_domain = ""
        self.session_id = uuid.uuid4()
        self.setupUi(self)
        self.InitUI()

    def InitUI(self):
        self.setFixedSize(570, 320)
        self.setWindowIcon(QtGui.QIcon(get_correct_path('icon.ico')))
        self.assign_buttons()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Episode Name', "Episode Size", "Status", "Title"])
        self.statusBar().showMessage(
            f"Your current session ID: {self.session_id}")
        self.comboBox.addItem("1080p")
        self.comboBox.addItem("720p")
        self.comboBox.addItem("480p")
        self.comboBox.addItem("360p")

    def assign_buttons(self):
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.handle_button)
        self.lineEdit.mousePressEvent = self.handle_clipboard

    def handle_clipboard(self, _):
        try:
            current_clip = pyperclip.paste()
            url_check = self.check_url(current_clip)
            if url_check == "season" or url_check == "series":
                self.base_domain = current_clip.split("/")[2]
                self.lineEdit.setText(current_clip)
                self.url = current_clip
                self.pushButton.setEnabled(True)
                if url_check == "series":
                    self.state = "series"
                else:
                    self.url = current_clip
                    self.state = "season"

        except Exception as e:
            print("I'm From handle_clipboard {}".format(e))

    def handle_button(self):
        try:
            self.pushButton.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.start_time = time.time()
            self.fetch_info()
            self.single_episode_info_thread()
        except Exception as e:
            print(e)

    def check_url(self, url):
        egybest = "egybest"
        series = "/series/"
        season = "/season/"
        if egybest and series in url:
            return "series"
        elif egybest and season in url:
            return "season"
        return False

    def change_status(self, text):
        self.label_2.setText(text)

    def info_box(self, msg):
        ctypes.windll.user32.MessageBoxW(0, msg, "EgyBest Scrapper V4.0", 0)


def main():
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)

    window = egybest()

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
