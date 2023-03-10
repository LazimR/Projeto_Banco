# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipal(object):
        '''
        Esta classe representa a tela de operações (ou tela principal) do L-Bank.

        Possui um cabeçalho com as informações básicas do usuário logado,
        botões de logout e sair, ocultar e exibir saldo e botões que levam
        aos frames de operação do banco (depósito, saque, transferência e extrato).

        Frame de:
        Depósito - campo para o valor e botão para depositar.
        Saque - campo para valor, senha e botão para sacar.
        Transferência - campo para valor, número da conta de destinatário, senha e botão para transferir.
        Extrato - janela com um label de registros de operações.

        Todos os frames possuem botão de retorno.
        '''

        def setupUi(self, TelaPrincipal):
                TelaPrincipal.setObjectName("TelaPrincipal")
                TelaPrincipal.resize(800, 600)
                TelaPrincipal.setMinimumSize(QtCore.QSize(800, 600))
                TelaPrincipal.setMaximumSize(QtCore.QSize(3840, 2160))
                TelaPrincipal.setSizeIncrement(QtCore.QSize(110, 100))
                TelaPrincipal.setBaseSize(QtCore.QSize(800, 600))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                TelaPrincipal.setFont(font)
                TelaPrincipal.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
                self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1200))
                self.centralwidget.setSizeIncrement(QtCore.QSize(110, 100))
                self.centralwidget.setBaseSize(QtCore.QSize(800, 600))
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(30, 20, 751, 100))
                self.frame.setMinimumSize(QtCore.QSize(0, 100))
                self.frame.setStyleSheet("background-color:white;\n"
        "border-radius:15;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.Mensagem_user = QtWidgets.QLabel(self.frame)
                self.Mensagem_user.setGeometry(QtCore.QRect(30, 20, 541, 16))
                self.Mensagem_user.setMinimumSize(QtCore.QSize(400, 0))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Mensagem_user.setFont(font)
                self.Mensagem_user.setStyleSheet("")
                self.Mensagem_user.setObjectName("Mensagem_user")
                self.Saldo_label = QtWidgets.QLabel(self.frame)
                self.Saldo_label.setGeometry(QtCore.QRect(30, 50, 51, 16))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Saldo_label.setFont(font)
                self.Saldo_label.setObjectName("Saldo_label")
                self.Saldo_set = QtWidgets.QLabel(self.frame)
                self.Saldo_set.setGeometry(QtCore.QRect(95, 50, 91, 16))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.Saldo_set.setFont(font)
                self.Saldo_set.setStyleSheet("background-color:white;")
                self.Saldo_set.setObjectName("Saldo_set")
                self.Ocultar_Button = QtWidgets.QPushButton(self.frame)
                self.Ocultar_Button.setGeometry(QtCore.QRect(210, 50, 23, 23))
                self.Ocultar_Button.setMinimumSize(QtCore.QSize(23, 23))
                self.Ocultar_Button.setMaximumSize(QtCore.QSize(23, 23))
                self.Ocultar_Button.setStyleSheet("background-image: url('C:/Users/kndso/OneDrive/Documentos/UFPI 4/POO II/Códigos/Projeto Banco/Lazimr/Projeto_Banco/imagens/olho_fechado.png');\n"
        "background-repeat: no-repeat;\n"
        "border-radius: 7px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;\n"
        "")
                self.Ocultar_Button.setText("")
                self.Ocultar_Button.setObjectName("Ocultar_Button")
                self.Sair_Button = QtWidgets.QPushButton(self.frame)
                self.Sair_Button.setGeometry(QtCore.QRect(670, 50, 51, 21))
                self.Sair_Button.setStyleSheet("border-radius: 2px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;\n"
        "")
                self.Sair_Button.setObjectName("Sair_Button")
                self.Logout_Button = QtWidgets.QPushButton(self.frame)
                self.Logout_Button.setGeometry(QtCore.QRect(670, 20, 51, 23))
                self.Logout_Button.setStyleSheet("border-radius: 2px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;\n"
        "")
                self.Logout_Button.setObjectName("Logout_Button")
                self.Fundo = QtWidgets.QLabel(self.centralwidget)
                self.Fundo.setGeometry(QtCore.QRect(-210, -130, 1200, 1200))
                self.Fundo.setMinimumSize(QtCore.QSize(1200, 1200))
                self.Fundo.setMaximumSize(QtCore.QSize(4000, 3000))
                self.Fundo.setStyleSheet("background-image: url('C:/Users/kndso/OneDrive/Documentos/UFPI 4/POO II/Códigos/Projeto Banco/Lazimr/Projeto_Banco/imagens/fundo.png');\n"
        "background-repeat: no-repeat;")
                self.Fundo.setObjectName("Fundo")
                self.Frame_opc = QtWidgets.QFrame(self.centralwidget)
                self.Frame_opc.setGeometry(QtCore.QRect(30, 150, 751, 426))
                self.Frame_opc.setObjectName("Frame_opc")
                self.Layout_opc = QtWidgets.QVBoxLayout(self.Frame_opc)
                self.Layout_opc.setSpacing(0)
                self.Layout_opc.setObjectName("Layout_opc")
                self.horizontalLayout = QtWidgets.QHBoxLayout()
                self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
                self.horizontalLayout.setSpacing(0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.Saque_Button = QtWidgets.QPushButton(self.Frame_opc)
                self.Saque_Button.setMinimumSize(QtCore.QSize(204, 210))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                self.Saque_Button.setFont(font)
                self.Saque_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "border-width: 2px;\n"
        "border-style: solid;\n"
        "background-color: #ffffff;\n"
        "")
                self.Saque_Button.setObjectName("Saque_Button")
                self.horizontalLayout.addWidget(self.Saque_Button)
                self.Deposito_Button = QtWidgets.QPushButton(self.Frame_opc)
                self.Deposito_Button.setMinimumSize(QtCore.QSize(0, 210))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                self.Deposito_Button.setFont(font)
                self.Deposito_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ffffff;\n"
        "border-width: 2px;\n"
        "border-style: solid;")
                self.Deposito_Button.setObjectName("Deposito_Button")
                self.horizontalLayout.addWidget(self.Deposito_Button)
                self.Layout_opc.addLayout(self.horizontalLayout)
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.Transf_Button_2 = QtWidgets.QPushButton(self.Frame_opc)
                self.Transf_Button_2.setMinimumSize(QtCore.QSize(0, 210))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                self.Transf_Button_2.setFont(font)
                self.Transf_Button_2.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ffffff;\n"
        "border-width:2px;\n"
        "border-style: solid;")
                self.Transf_Button_2.setObjectName("Transf_Button_2")
                self.horizontalLayout_2.addWidget(self.Transf_Button_2)
                self.Extrato_Button_2 = QtWidgets.QPushButton(self.Frame_opc)
                self.Extrato_Button_2.setMinimumSize(QtCore.QSize(0, 210))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(15)
                self.Extrato_Button_2.setFont(font)
                self.Extrato_Button_2.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ffffff;\n"
        "border-width:2px;\n"
        "border-style: solid;")
                self.Extrato_Button_2.setObjectName("Extrato_Button_2")
                self.horizontalLayout_2.addWidget(self.Extrato_Button_2)
                self.Layout_opc.addLayout(self.horizontalLayout_2)
                self.Frame_Saque = QtWidgets.QFrame(self.centralwidget)
                self.Frame_Saque.setGeometry(QtCore.QRect(30, 150, 751, 426))
                self.Frame_Saque.setObjectName("Frame_Saque")
                self.Layout_opc_2 = QtWidgets.QVBoxLayout(self.Frame_Saque)
                self.Layout_opc_2.setContentsMargins(-1, 100, -1, -1)
                self.Layout_opc_2.setSpacing(0)
                self.Layout_opc_2.setObjectName("Layout_opc_2")
                self.formLayout = QtWidgets.QFormLayout()
                self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
                self.formLayout.setContentsMargins(100, -1, -1, -1)
                self.formLayout.setObjectName("formLayout")
                self.ValorLabel = QtWidgets.QLabel(self.Frame_Saque)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.ValorLabel.setFont(font)
                self.ValorLabel.setObjectName("ValorLabel")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ValorLabel)
                self.ValorLineEdit = QtWidgets.QLineEdit(self.Frame_Saque)
                self.ValorLineEdit.setMinimumSize(QtCore.QSize(200, 0))
                self.ValorLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.ValorLineEdit.setFont(font)
                self.ValorLineEdit.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.ValorLineEdit.setObjectName("ValorLineEdit")
                self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ValorLineEdit)
                self.senhaLabel = QtWidgets.QLabel(self.Frame_Saque)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.senhaLabel.setFont(font)
                self.senhaLabel.setObjectName("senhaLabel")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.senhaLabel)
                self.senhaLineEdit = QtWidgets.QLineEdit(self.Frame_Saque)
                self.senhaLineEdit.setMinimumSize(QtCore.QSize(200, 0))
                self.senhaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
                self.senhaLineEdit.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.senhaLineEdit.setObjectName("senhaLineEdit")
                self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.senhaLineEdit)
                self.Frame_botoes = QtWidgets.QFrame(self.Frame_Saque)
                self.Frame_botoes.setMinimumSize(QtCore.QSize(0, 50))
                self.Frame_botoes.setStyleSheet("")
                self.Frame_botoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame_botoes.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame_botoes.setObjectName("Frame_botoes")
                self.Sacar_Button = QtWidgets.QPushButton(self.Frame_botoes)
                self.Sacar_Button.setGeometry(QtCore.QRect(10, 10, 100, 25))
                self.Sacar_Button.setMinimumSize(QtCore.QSize(100, 25))
                self.Sacar_Button.setMaximumSize(QtCore.QSize(100, 16777215))
                self.Sacar_Button.setBaseSize(QtCore.QSize(100, 0))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Sacar_Button.setFont(font)
                self.Sacar_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #00ff00;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Sacar_Button.setObjectName("Sacar_Button")
                self.Voltar_Button = QtWidgets.QPushButton(self.Frame_botoes)
                self.Voltar_Button.setGeometry(QtCore.QRect(230, 10, 100, 25))
                self.Voltar_Button.setMinimumSize(QtCore.QSize(0, 25))
                self.Voltar_Button.setMaximumSize(QtCore.QSize(100, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Voltar_Button.setFont(font)
                self.Voltar_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ff0000;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Voltar_Button.setObjectName("Voltar_Button")
                self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Frame_botoes)
                self.Layout_opc_2.addLayout(self.formLayout)
                self.Frame_deposito = QtWidgets.QFrame(self.centralwidget)
                self.Frame_deposito.setGeometry(QtCore.QRect(30, 150, 751, 421))
                self.Frame_deposito.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame_deposito.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame_deposito.setObjectName("Frame_deposito")
                self.layoutWidget = QtWidgets.QWidget(self.Frame_deposito)
                self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 733, 424))
                self.layoutWidget.setObjectName("layoutWidget")
                self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
                self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
                self.formLayout_2.setContentsMargins(105, 120, 0, 0)
                self.formLayout_2.setObjectName("formLayout_2")
                self.ValorLabel_2 = QtWidgets.QLabel(self.layoutWidget)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.ValorLabel_2.setFont(font)
                self.ValorLabel_2.setObjectName("ValorLabel_2")
                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ValorLabel_2)
                self.ValorLineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
                self.ValorLineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
                self.ValorLineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.ValorLineEdit_2.setFont(font)
                self.ValorLineEdit_2.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.ValorLineEdit_2.setObjectName("ValorLineEdit_2")
                self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ValorLineEdit_2)
                self.Frame_botoes_2 = QtWidgets.QFrame(self.layoutWidget)
                self.Frame_botoes_2.setMinimumSize(QtCore.QSize(0, 50))
                self.Frame_botoes_2.setStyleSheet("")
                self.Frame_botoes_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame_botoes_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame_botoes_2.setObjectName("Frame_botoes_2")
                self.Depositar_Button = QtWidgets.QPushButton(self.Frame_botoes_2)
                self.Depositar_Button.setGeometry(QtCore.QRect(10, 10, 100, 25))
                self.Depositar_Button.setMinimumSize(QtCore.QSize(100, 25))
                self.Depositar_Button.setMaximumSize(QtCore.QSize(100, 16777215))
                self.Depositar_Button.setBaseSize(QtCore.QSize(100, 0))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Depositar_Button.setFont(font)
                self.Depositar_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #00ff00;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Depositar_Button.setObjectName("Depositar_Button")
                self.Voltar_Button_2 = QtWidgets.QPushButton(self.Frame_botoes_2)
                self.Voltar_Button_2.setGeometry(QtCore.QRect(230, 10, 100, 25))
                self.Voltar_Button_2.setMinimumSize(QtCore.QSize(0, 25))
                self.Voltar_Button_2.setMaximumSize(QtCore.QSize(100, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Voltar_Button_2.setFont(font)
                self.Voltar_Button_2.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ff0000;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Voltar_Button_2.setObjectName("Voltar_Button_2")
                self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Frame_botoes_2)
                self.Frame_Transf = QtWidgets.QFrame(self.centralwidget)
                self.Frame_Transf.setGeometry(QtCore.QRect(30, 155, 751, 421))
                self.Frame_Transf.setObjectName("Frame_Transf")
                self.Layout_opc_3 = QtWidgets.QVBoxLayout(self.Frame_Transf)
                self.Layout_opc_3.setContentsMargins(-1, 60, -1, -1)
                self.Layout_opc_3.setSpacing(0)
                self.Layout_opc_3.setObjectName("Layout_opc_3")
                self.formLayout_3 = QtWidgets.QFormLayout()
                self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
                self.formLayout_3.setContentsMargins(100, -1, -1, -1)
                self.formLayout_3.setObjectName("formLayout_3")
                self.ValorLabel_3 = QtWidgets.QLabel(self.Frame_Transf)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.ValorLabel_3.setFont(font)
                self.ValorLabel_3.setObjectName("ValorLabel_3")
                self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ValorLabel_3)
                self.ValorLineEdit_3 = QtWidgets.QLineEdit(self.Frame_Transf)
                self.ValorLineEdit_3.setMinimumSize(QtCore.QSize(200, 0))
                self.ValorLineEdit_3.setMaximumSize(QtCore.QSize(200, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.ValorLineEdit_3.setFont(font)
                self.ValorLineEdit_3.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.ValorLineEdit_3.setObjectName("ValorLineEdit_3")
                self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ValorLineEdit_3)
                self.senhaLabel_2 = QtWidgets.QLabel(self.Frame_Transf)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.senhaLabel_2.setFont(font)
                self.senhaLabel_2.setObjectName("senhaLabel_2")
                self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.senhaLabel_2)
                self.senhaLineEdit_2 = QtWidgets.QLineEdit(self.Frame_Transf)
                self.senhaLineEdit_2.setMinimumSize(QtCore.QSize(200, 0))
                self.senhaLineEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
                self.senhaLineEdit_2.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.senhaLineEdit_2.setObjectName("senhaLineEdit_2")
                self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.senhaLineEdit_2)
                self.Frame_botoes_3 = QtWidgets.QFrame(self.Frame_Transf)
                self.Frame_botoes_3.setMinimumSize(QtCore.QSize(0, 50))
                self.Frame_botoes_3.setStyleSheet("")
                self.Frame_botoes_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.Frame_botoes_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.Frame_botoes_3.setObjectName("Frame_botoes_3")
                self.Transf_Button = QtWidgets.QPushButton(self.Frame_botoes_3)
                self.Transf_Button.setGeometry(QtCore.QRect(10, 10, 100, 25))
                self.Transf_Button.setMinimumSize(QtCore.QSize(100, 25))
                self.Transf_Button.setMaximumSize(QtCore.QSize(100, 16777215))
                self.Transf_Button.setBaseSize(QtCore.QSize(100, 0))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Transf_Button.setFont(font)
                self.Transf_Button.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #00ff00;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Transf_Button.setObjectName("Transf_Button")
                self.Voltar_Button_3 = QtWidgets.QPushButton(self.Frame_botoes_3)
                self.Voltar_Button_3.setGeometry(QtCore.QRect(230, 10, 100, 25))
                self.Voltar_Button_3.setMinimumSize(QtCore.QSize(0, 25))
                self.Voltar_Button_3.setMaximumSize(QtCore.QSize(100, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.Voltar_Button_3.setFont(font)
                self.Voltar_Button_3.setStyleSheet("border-radius:10px;\n"
        "border-color:black;\n"
        "background-color: #ff0000;\n"
        "border-width: 0.1px;\n"
        "border-style: solid;")
                self.Voltar_Button_3.setObjectName("Voltar_Button_3")
                self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Frame_botoes_3)
                self.destinatarioLabel = QtWidgets.QLabel(self.Frame_Transf)
                font = QtGui.QFont()
                font.setFamily("Arial Black")
                font.setPointSize(11)
                self.destinatarioLabel.setFont(font)
                self.destinatarioLabel.setObjectName("destinatarioLabel")
                self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.destinatarioLabel)
                self.destinatarioLineEdit = QtWidgets.QLineEdit(self.Frame_Transf)
                self.destinatarioLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.destinatarioLineEdit.setFont(font)
                self.destinatarioLineEdit.setStyleSheet("border-radius:5px;\n"
        "border-style:solid;\n"
        "border-width:1px;\n"
        "border-color:black;")
                self.destinatarioLineEdit.setObjectName("destinatarioLineEdit")
                self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinatarioLineEdit)
                self.Layout_opc_3.addLayout(self.formLayout_3)
                self.Frame_extrato = QtWidgets.QFrame(self.centralwidget)
                self.Frame_extrato.setGeometry(QtCore.QRect(29, 149, 751, 421))
                self.Frame_extrato.setObjectName("Frame_extrato")
                self.LayoutExtrato = QtWidgets.QVBoxLayout(self.Frame_extrato)
                self.LayoutExtrato.setObjectName("LayoutExtrato")
                self.scrollArea = QtWidgets.QScrollArea(self.Frame_extrato)
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 370))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout.setObjectName("verticalLayout")
                self.Texto_extrato = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.Texto_extrato.sizePolicy().hasHeightForWidth())
                self.Texto_extrato.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(11)
                self.Texto_extrato.setFont(font)
                self.Texto_extrato.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Texto_extrato.setStyleSheet("background-color:white;")
                self.Texto_extrato.setText("")
                self.Texto_extrato.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                self.Texto_extrato.setObjectName("Texto_extrato")
                self.verticalLayout.addWidget(self.Texto_extrato)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.LayoutExtrato.addWidget(self.scrollArea)
                self.Voltar = QtWidgets.QPushButton(self.Frame_extrato)
                self.Voltar.setObjectName("Voltar")
                self.LayoutExtrato.addWidget(self.Voltar)
                self.Fundo.raise_()
                self.frame.raise_()
                self.Frame_opc.raise_()
                self.Frame_Saque.raise_()
                self.Frame_deposito.raise_()
                self.Frame_Transf.raise_()
                self.Frame_extrato.raise_()
                TelaPrincipal.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(TelaPrincipal)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
                self.menubar.setObjectName("menubar")
                TelaPrincipal.setMenuBar(self.menubar)

                self.retranslateUi(TelaPrincipal)
                QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

        def retranslateUi(self, TelaPrincipal):
                _translate = QtCore.QCoreApplication.translate
                TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "L-Bank"))
                self.Mensagem_user.setText(_translate("TelaPrincipal", "Olá, User"))
                self.Saldo_label.setText(_translate("TelaPrincipal", "Saldo:"))
                self.Saldo_set.setText(_translate("TelaPrincipal", "123456789,9"))
                self.Sair_Button.setText(_translate("TelaPrincipal", "SAIR"))
                self.Logout_Button.setText(_translate("TelaPrincipal", "LOGOUT"))
                self.Fundo.setText(_translate("TelaPrincipal", "TextLabel"))
                self.Saque_Button.setText(_translate("TelaPrincipal", "Saque"))
                self.Deposito_Button.setText(_translate("TelaPrincipal", "Deposito"))
                self.Transf_Button_2.setText(_translate("TelaPrincipal", "Transferência"))
                self.Extrato_Button_2.setText(_translate("TelaPrincipal", "Extrato"))
                self.ValorLabel.setText(_translate("TelaPrincipal", "Quantidade:"))
                self.senhaLabel.setText(_translate("TelaPrincipal", "         Senha:"))
                self.Sacar_Button.setText(_translate("TelaPrincipal", "Sacar"))
                self.Voltar_Button.setText(_translate("TelaPrincipal", "Voltar"))
                self.ValorLabel_2.setText(_translate("TelaPrincipal", "Quantidade:"))
                self.Depositar_Button.setText(_translate("TelaPrincipal", "Depositar"))
                self.Voltar_Button_2.setText(_translate("TelaPrincipal", "Voltar"))
                self.ValorLabel_3.setText(_translate("TelaPrincipal", "Quantidade:"))
                self.senhaLabel_2.setText(_translate("TelaPrincipal", "         Senha:"))
                self.Transf_Button.setText(_translate("TelaPrincipal", "Transferir"))
                self.Voltar_Button_3.setText(_translate("TelaPrincipal", "Voltar"))
                self.destinatarioLabel.setText(_translate("TelaPrincipal", "Destinatario: "))
                self.Voltar.setText(_translate("TelaPrincipal", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())
