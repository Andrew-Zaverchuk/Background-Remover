import sys
from PyQt5 import QtWidgets
from first import Ui_FirstWindow
from second import Ui_SecondWindow
from third import Ui_ThirdWindow
from PyQt5.QtWidgets import QFileDialog, QApplication

from rembg import remove
from PIL import Image
from pathlib import Path


app = QtWidgets.QApplication(sys.argv)

FirstWindow = QtWidgets.QMainWindow()
ui = Ui_FirstWindow()
ui.setupUi(FirstWindow)
FirstWindow.show()


def test():
    if ui.lineEdit1.text() == '':
        ui.next1.setEnabled(False)
    elif ui.lineEdit1.text() != '':
        ui.next1.setEnabled(True)

test()

def search1():
    global res
    res = QFileDialog.getOpenFileName(None, 'toolButton', 'D:/', 'JPG File (*.jpg);; PNG File (*.png)')
    ui.lineEdit1.setText(str(res[0]))
    if ui.lineEdit1.text() == '':
        ui.next1.setEnabled(False)
    elif ui.lineEdit1.text() != '':
        ui.next1.setEnabled(True)

def cancell(self):
    QApplication.quit()


def openSecondWindow():
    inp = res[0]
    global SecondWindow, ui
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    FirstWindow.hide()
    SecondWindow.show()

    def test():
        if ui.lineEdit2.text() == '':
            ui.go.setEnabled(False)
        elif ui.lineEdit2.text() != '':
            ui.go.setEnabled(True)

    test()

    def Back2First():
        SecondWindow.hide()
        FirstWindow.show()

    def search2():
        global dirname
        dirname = QFileDialog.getExistingDirectory(None, 'Вибрати папку' 'D:/' ".")
        ui.lineEdit2.setText(str(dirname))
        if ui.lineEdit2.text() == '':
            ui.go.setEnabled(False)
        elif ui.lineEdit2.text() != '':
            ui.go.setEnabled(True)

    def go():
        input_path = Path(inp)
        file_name = input_path.stem
        output_path = f'{dirname}/{file_name}_output.png'
        input_img = Image.open(input_path)
        output_img = remove(input_img)
        output_img.save(output_path)

        global ThirdWindow
        ThirdWindow = QtWidgets.QMainWindow()
        ui = Ui_ThirdWindow()
        ui.setupUi(ThirdWindow)
        SecondWindow.close()
        ThirdWindow.show()

        def view():
            img = Image.open(output_path)
            img.show()

        def exit():
            QApplication.quit()


        ui.view.clicked.connect(view)
        ui.exit.clicked.connect(exit)

    ui.go.clicked.connect(go)
    ui.search2.clicked.connect(search2)
    ui.back1.clicked.connect(Back2First)
    ui.cancell2.clicked.connect(cancell)

ui.cancell1.clicked.connect(cancell)
ui.search1.clicked.connect(search1)
ui.next1.clicked.connect(openSecondWindow)

sys.exit(app.exec_())