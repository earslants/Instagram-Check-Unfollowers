from PyQt5 import QtWidgets
import sys
from qtDesign import Ui_MainWindow
import browser


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)

    def login(self):

        username = self.ui.txt_id.text()
        password = self.ui.txt_password.text()
        browser.Browser("https://www.instagram.com", username, password)
    
    def app():
        app = QtWidgets.QApplication(sys.argv)
        win = App()

        win.show()
        sys.exit(app.exec_())

App.app()