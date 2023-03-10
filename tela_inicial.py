# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaLogin(object):
        '''
        Esta classe representa a tela de login (ou tela inicial) do L-Bank.
        Interface feita pelo Qt Designer.

        Possui como título o nome do banco, campos para login e senha,
        um botão para logar e outro botão que leva para a tela de cadastro.
        '''
        def setupUi(self, TelaLogin):
                TelaLogin.setObjectName("TelaLogin")
                TelaLogin.resize(800, 600)
                TelaLogin.setMinimumSize(QtCore.QSize(800, 600))
                TelaLogin.setMaximumSize(QtCore.QSize(3840, 2160))
                TelaLogin.setSizeIncrement(QtCore.QSize(110, 100))
                TelaLogin.setBaseSize(QtCore.QSize(800, 600))
                TelaLogin.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(TelaLogin)
                self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1200))
                self.centralwidget.setSizeIncrement(QtCore.QSize(110, 100))
                self.centralwidget.setBaseSize(QtCore.QSize(800, 600))
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-100, -100, 931, 771))
                self.label.setStyleSheet("background-image: url('C:/Users/kndso/OneDrive/Documentos/UFPI 4/POO II/Códigos/Projeto Banco/Lazimr/Projeto_Banco/imagens/fundo.png');\n")
                self.label.setText("")
                self.label.setObjectName("label")
                self.frame_principal = QtWidgets.QFrame(self.centralwidget)
                self.frame_principal.setGeometry(QtCore.QRect(190, 170, 431, 211))
                self.frame_principal.setStyleSheet("background:opacity(0.0);")
                self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_principal.setObjectName("frame_principal")
                self.Login_label = QtWidgets.QLabel(self.frame_principal)
                self.Login_label.setGeometry(QtCore.QRect(60, 50, 398, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.Login_label.setFont(font)
                self.Login_label.setObjectName("Login_label")
                self.Login_line = QtWidgets.QLineEdit(self.frame_principal)
                self.Login_line.setGeometry(QtCore.QRect(110, 50, 200, 25))
                self.Login_line.setMaximumSize(QtCore.QSize(200, 25))
                self.Login_line.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.Login_line.setObjectName("Login_line")
                self.Senha_label = QtWidgets.QLabel(self.frame_principal)
                self.Senha_label.setGeometry(QtCore.QRect(50, 80, 398, 46))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.Senha_label.setFont(font)
                self.Senha_label.setObjectName("Senha_label")
                self.Senha_line = QtWidgets.QLineEdit(self.frame_principal)
                self.Senha_line.setGeometry(QtCore.QRect(110, 90, 200, 25))
                self.Senha_line.setMaximumSize(QtCore.QSize(200, 25))
                self.Senha_line.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.Senha_line.setObjectName("Senha_line")
                self.Login_button = QtWidgets.QPushButton(self.frame_principal)
                self.Login_button.setGeometry(QtCore.QRect(140, 130, 100, 30))
                self.Login_button.setMaximumSize(QtCore.QSize(100, 30))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.Login_button.setFont(font)
                self.Login_button.setStyleSheet("border-radius:10px;\n"
        "border-style:solid;\n"
        "border-width:2px;\n"
        "border-color:black;")
                self.Login_button.setObjectName("Login_button")
                self.Cadastro_label = QtWidgets.QLabel(self.frame_principal)
                self.Cadastro_label.setGeometry(QtCore.QRect(100, 170, 110, 13))
                self.Cadastro_label.setMaximumSize(QtCore.QSize(110, 16777215))
                self.Cadastro_label.setObjectName("Cadastro_label")
                self.Cadastro_button = QtWidgets.QPushButton(self.frame_principal)
                self.Cadastro_button.setGeometry(QtCore.QRect(220, 170, 70, 15))
                self.Cadastro_button.setMinimumSize(QtCore.QSize(70, 0))
                self.Cadastro_button.setMaximumSize(QtCore.QSize(70, 15))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                self.Cadastro_button.setFont(font)
                self.Cadastro_button.setStyleSheet("border: opacity(0.0)")
                self.Cadastro_button.setObjectName("Cadastro_button")
                self.Senha_label.raise_()
                self.Login_label.raise_()
                self.Login_line.raise_()
                self.Senha_line.raise_()
                #self.Senha_line.setEchoMode(QLineEdit.Password)
                self.Login_button.raise_()
                self.Cadastro_label.raise_()
                self.Cadastro_button.raise_()
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(160, 30, 471, 121))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(70)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.Sair_Button = QtWidgets.QPushButton(self.centralwidget)
                self.Sair_Button.setGeometry(QtCore.QRect(700, 30, 51, 21))
                self.Sair_Button.setStyleSheet("border-radius: 2px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;\n"
        "background-color:white;")
                self.Sair_Button.setObjectName("Sair_Button")
                TelaLogin.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(TelaLogin)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
                self.menubar.setObjectName("menubar")
                TelaLogin.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(TelaLogin)
                self.statusbar.setObjectName("statusbar")
                TelaLogin.setStatusBar(self.statusbar)

                self.retranslateUi(TelaLogin)
                QtCore.QMetaObject.connectSlotsByName(TelaLogin)

        def retranslateUi(self, TelaLogin):
                _translate = QtCore.QCoreApplication.translate
                TelaLogin.setWindowTitle(_translate("TelaLogin", "L-Bank"))
                self.Login_label.setText(_translate("TelaLogin", "Login:"))
                self.Senha_label.setText(_translate("TelaLogin", "Senha:"))
                self.Login_button.setText(_translate("TelaLogin", "Login"))
                self.Cadastro_label.setText(_translate("TelaLogin", "Não possui cadastro? "))
                self.Cadastro_button.setText(_translate("TelaLogin", "Clique aqui"))
                self.label_2.setText(_translate("TelaLogin", "L-Bank"))
                self.Sair_Button.setText(_translate("TelaLogin", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaLogin = QtWidgets.QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())
