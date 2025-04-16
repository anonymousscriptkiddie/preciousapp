from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 480)

        # Label for background image (ensure this path is correct or remove the image)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-40, -10, 451, 491))
        self.label.setText("")
        try:
            self.label.setPixmap(QtGui.QPixmap("background.gif"))
            self.label.setScaledContents(True)
        except:
            print("Warning: Background image not found.")
        self.label.setObjectName("label")

        # PlainTextEdit for user text input
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(100, 60, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(True)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 46, 119)")
        self.plainTextEdit.setObjectName("plainTextEdit")

        # RadioButton for user choice
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(70, 340, 261, 51))
        icon = QtGui.QIcon()
        try:
            icon.addPixmap(QtGui.QPixmap("pngtree-cute-cute-pink-button-game-ui-elements-png-image_7120693.png"),
                           QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.radioButton.setIcon(icon)
        except:
            print("Warning: Radio button icon not found.")
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setText("Do you Agree with terms and Conditions")

        # ScrollArea widget
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(70, 130, 241, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 239, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # PlainTextEdit inside the ScrollArea
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(40, 50, 191, 161))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        # TimeEdit inside the ScrollArea
        self.timeEdit = QtWidgets.QTimeEdit(self.scrollAreaWidgetContents)
        self.timeEdit.setGeometry(QtCore.QRect(70, 20, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # Button for Continue action
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 400, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("CONTINUE")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit.setPlainText(_translate("Form", "WELCOME TO CANDY'S\n"
                                                           " APPLICATION\n"
                                                           "PLEASE CHECK SOME BOXES"))
        self.plainTextEdit_2.setPlainText(_translate("Form",
                                                     "KINDLY PLEASE BE RESPECTFUL ON YOURE MESSAGE TO ME, AND IF YOU WANT FOLLOW BACK IN INSTAGRAM OR TO BE FRIENDS KINDLY REQUEST IT FROM HERE, THATS ALL ^^ THANK YOU\n"
                                                     "ADDITIONALLY, KINDLY PUT THE TIME YOU DISCOVERED MY APP"))


# Main section to run the app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()  # Create the main window
    ui = Ui_Form()  # Create an instance of the UI class
    ui.setupUi(Form)  # Set up the UI on the window
    Form.show()  # Show the window
    sys.exit(app.exec_())  # Start the application event loop
