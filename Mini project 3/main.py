from os import name
import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import cv2
import mydatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("log in.ui", None)
        self.ui.show()
        self.ui.setWindowTitle("Log In")
        self.ui.label.setStyleSheet("image : url(kindpng_170301.png);")
        self.ui.enterbtn.clicked.connect(self.enterroom)

    def enterroom(self):
        if self.ui.lineEdit.text() == "admin" and self.ui.lineEdit_2.text() == "admin":
            self.ui = Userslist()
        else :
            self.msgBox = QMessageBox()
            self.msgBox.setText("Wrong username or password! \n Try again!")
            self.msgBox.exec()
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")

class Userslist(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("main.ui", None)
        self.ui.show()
        self.ReadFromDB()
        self.ui.setWindowTitle("Users list")   
        self.ui.add_account.clicked.connect(self.next_page) 
    
    def ReadFromDB(self):
        self.result = mydatabase.GetAll()
        self.editlist = []

        for i in range(len(self.result)):

            self.id_label = QLabel()
            self.id_label.setText(self.result[i][4])
            self.ui.IdLayout.addWidget(self.id_label, 5)

            self.new_label = QLabel()
            self.new_label.setText(self.result[i][0])
            self.ui.nameslayout.addWidget(self.new_label, 5)

            self.new_label = QLabel()
            self.new_label.setText(self.result[i][1])
            self.ui.Familylayout.addWidget(self.new_label, 5)

            self.edit_btn = QPushButton()
            self.edit_btn.setText('📝')
            self.ui.EditLayout.addWidget(self.edit_btn, 5)
            self.editlist.append(self.edit_btn)

            # self.img_label = QLabel()
            # self.ui.img_label.setStyleSheet("image : url(f'face_images/user{counter}.jpg');")
            # self.ui.ImageLayout.addWidget(self.img_label)

            for i in range(len(self.editlist)):
                self.editlist[i].clicked.connect(partial(self.edit_user_page,self.result[i][0],self.result[i][1],self.result[i][2],self.result[i][3],self.result[i][4]))
    
    def edit_user_page(self,name,lastname,nationalcode,birthdate,id):
        self.ui = EditUser(name,lastname,nationalcode,birthdate,id)

    def next_page(self):
        self.ui = NewUser()

class NewUser(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("new user.ui", None)
        self.ui.show()
        self.ui.setWindowTitle("Add new account")   
        self.ui.addAccount.clicked.connect(self.AddNewUser)
        self.ui.capButton.clicked.connect(self.OpenCam)
    
    def AddNewUser(self):
        # id = self.ui.id.text()
        name = self.ui.uname.text()
        family = self.ui.ufamily.text()
        nationalcode = self.ui.unational.text()
        birthdate = self.ui.ubirthdate.text()
        mydatabase.Add(name,family,nationalcode,birthdate)
        

        self.msgBox = QMessageBox()
        self.msgBox.setText("The User added successfully ;)")
        self.msgBox.exec()
        self.ui = Userslist()
    
    def OpenCam(self):
        self.ui = Webcam()

class EditUser(QWidget):
    def __init__(self,name,lastname,nationalcode,birthdate,id):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("user edit.ui", None)
        self.ui.show()
        self.ui.setWindowTitle("Edit User Info")   
        self.ui.DoneBtn.clicked.connect(partial(self.Edit_User,name,lastname,nationalcode,birthdate,id))
        self.ui.pushButton.clicked.connect(self.OpenCam)

        self.new_label = QLabel()
        self.new_label.setText(f"Name : {name}")
        self.family_label = QLabel()
        self.family_label.setText(f"Lastname : {lastname}")
        self.nation_label = QLabel()
        self.nation_label.setText(f"Nationalcode : {nationalcode}")
        self.birthdate_label = QLabel()
        self.birthdate_label.setText(f"Birthdate : {birthdate}")
        self.id_label = QLabel()
        self.id_label.setText(f"User ID : {id}")

        self.ui.verticalLayout_3.addWidget(self.id_label)
        self.ui.verticalLayout_3.addWidget(self.new_label)
        self.ui.verticalLayout_3.addWidget(self.family_label)
        self.ui.verticalLayout_3.addWidget(self.nation_label)
        self.ui.verticalLayout_3.addWidget(self.birthdate_label)
        

    def Edit_User(self,name,lastname,nationalcode,birthdate,id):

        if self.ui.uname.text() == "" :
            name = name 
        else :
            name = self.ui.uname.text()

        if self.ui.ufamily.text() == "":
            family = lastname
        else:
            family = self.ui.ufamily.text()

        if self.ui.unational.text() == "":
            nationalcode1 = nationalcode
        else:
            nationalcode1 = self.ui.unational.text()

        if self.ui.ubirthdate.text() == "":
            birthdate = birthdate
        else:
            birthdate = self.ui.ubirthdate.text()

        mydatabase.Edit(name,family,nationalcode1,birthdate,id)
        # mydatabase.InsertImg()

        self.msgBox = QMessageBox()
        self.msgBox.setText("The User info modified successfully")
        self.msgBox.exec()
        self.ui = Userslist()

    def OpenCam(self):
        self.ui = Webcam()

class Webcam(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("webcam.ui", None)
        self.ui.show()
        self.ui.setWindowTitle("Capture Image")  
        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.ui.captureButton.clicked.connect(self.controlTimer)
      
    def viewCam(self):
        ret, image = self.cap.read()
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.ui.labelCam.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        counter = 1
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(1)
            self.ui.captureButton.setText("Capture")
            
        else:
            self.timer.stop()
            self.cap.release()
            self.ui.captureButton.setText("Done")
            cv2.imwrite(f"face_images/user{counter}.jpg", self.image)
            counter +=1
            self.msgBox = QMessageBox()
            self.msgBox.setText("Photo captured successfully")
            self.msgBox.exec()
            self.ui = Userslist()

app = QApplication(sys.argv)
window = MainWindow()
app.exec()