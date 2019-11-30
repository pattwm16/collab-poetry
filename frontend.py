# LITR 0110D - Final Project Frontend
import sys
import re
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import gpt_2_simple as gpt2
import os
import requests

def corr(s):
    return re.sub(r'\.(?! )', '. ', re.sub(r' +', ' ', s))

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Pocket Litter'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
        self.sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.sess,
                      run_name="run2",
                      checkpoint_dir="checkpoint")

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        text = gpt2.generate(self.sess,
                      length=100,
                      temperature=0.7,
                      prefix=textboxValue,
                      nsamples=1,
                      batch_size=4,
                      return_as_list=True)[0]
        # clean text of utf-8 mess
        text = corr(re.sub(r'[^\x00-\x7f]',r'', text))
        print(text)
        QMessageBox.question(self, 'Message', "Result: {}".format(text), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
