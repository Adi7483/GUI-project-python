import signal

import sys
import os
import subprocess
import psutil

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTreeWidgetItem, QTreeWidgetItemIterator
from PyQt5 import QtGui, QtWidgets, QtCore
from ui_mainWindow import Ui_MainWindow
from subprocess import Popen, PIPE, check_output, call


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.retranslateUi(self)
        self.ui.browserButton.clicked.connect(self.select_test)
        self.ui.runFile.clicked.connect(self.run_files)
        self.ui.treeWidget.setHeaderHidden(True)
        self.ui.pushButton_4.clicked.connect(self.log_output)
        self.ui.pushButton_2.clicked.connect(self.stop_run)
        self.ui.selectAll.clicked.connect(self.check_all)
        self.ui.selectAll.setEnabled(False)
        self.ui.disSelectAll.clicked.connect(self.remove_all)
        self.ui.disSelectAll.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.clear_log)
        self.list_files = []
        self.tree_files = []
        self.kill = []
        # self.trpid = os.getpid()
        self.folder_name = ""
        self.run_subprocess = ""

    def select_test(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, 'Open files',
                                                            "C:/Users/idana/Desktop/QA Automation Bootcamp/project/week_5/.vscode/")
        print(self.folder_name)
        for file in os.listdir(self.folder_name):
            if file.endswith("js") or file.endswith("py"):
                item = QTreeWidgetItem(self.ui.treeWidget, [file])
                item.setCheckState(0, QtCore.Qt.Unchecked)
                self.tree_files.append(file)
        print(self.tree_files)
        self.ui.selectAll.setEnabled(True)

    def run_files(self):
        iterator = QTreeWidgetItemIterator(self.ui.treeWidget)
        print(iterator)
        while iterator.value():
            item = iterator.value()
            print(item)
            if item.checkState(0):
                self.list_files.append(item.text(0))
                print(self.list_files)
            iterator += 1
        # self.thread.start()
        # self.kill.append({"id": self.trpid})
        # print(self.trpid)
        os.chdir(self.folder_name)

        self.path()
        # print(self.path)

    def path(self):
        a = 'node '
        for i in range(0, len(self.list_files)):
            if i != 0:
                # a += f" && node {self.folder_name}/{self.list_files[i]}"
                a += f" && {self.list_files[i]}"
                print(a)
            else:
                # a += f"{self.folder_name}/{self.list_files[i]}"
                a += f"{self.list_files[i]}"
            print(a)
        self.run_subprocess = Popen(a, stdout=PIPE, stderr=PIPE, shell=True)
        print(self.run_subprocess)
        self.kill.append({"id": self.run_subprocess.pid})
        print(self.kill)

    def stop_run(self):
        try:
            for process in self.kill:
                # process_pid = process["id"]
                subprocess.Popen("taskkill /F /T /PID %i" % self.run_subprocess.pid, shell=True)
            print('stopped running tests')
        except:
            print("Couldn't stop the process")

    def check_all(self):
        iteratorx = QTreeWidgetItemIterator(self.ui.treeWidget)
        while iteratorx.value():
            namex = iteratorx.value()
            namex.setCheckState(0, QtCore.Qt.Checked)
            iteratorx += 1
            self.ui.disSelectAll.setEnabled(True)
            self.ui.selectAll.setEnabled(False)

    def remove_all(self):
        iteratory = QTreeWidgetItemIterator(self.ui.treeWidget)
        while iteratory.value():
            namey = iteratory.value()
            namey.setCheckState(0, QtCore.Qt.Unchecked)
            iteratory += 1
            self.ui.disSelectAll.setEnabled(False)
            self.ui.selectAll.setEnabled(True)

    def clear_log(self):
        self.ui.textEdit.clear()

    def log_output(self):
        the_file = open("C:/Users/idana/Desktop/QA Automation Bootcamp/project/week_5/.vscode/logs/log.log")
        x = the_file.read()
        self.ui.textEdit.setText(x)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

# def thread_tests(self):
#     global p
#     global s
#     for i in range(0, len(self.list_name)):
#         print(self.list_name)
#         p = Popen(
#             ['node', 'C:/Users/idana/Desktop/QA Automation Bootcamp/project/week_5/.vscode/' + self.list_name[i]],
#             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print(self.list_name[i])
#         s = os.getpid()
#         print(s)
#         print(p)
#         p.communicate()
#         print(p.pid)
