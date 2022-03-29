from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QShortcut, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
import sys
from nltk.chat.util import Chat, reflections


class ShowImage(QMainWindow) :
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('maingui.ui', self)
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut_open.activated.connect(self.sendmessage)
        self.buttonSend.clicked.connect(self.sendmessage)
        self.textOutput.append('BOT : Welcome to Smartphone Information Media')
        self.textOutput.append('BOT : Can I help you?')

        pairs = (
            (
                r'hi|hello',
                ("hello can I help you?",)
            ),
            (
                r'show for help',
                ("\nshow menu > View a menu list \nshow menu+menu number  > Enter a menu",)
            ),
            (
                r'show menu1|show menu smartphone list',
                ("",)
            ),
            (
                r'show menu2|show menu the best smartphone list',
                ("",)
            ),
            (
                r'show menu',
                ("\nWrite 'menu+menu number' to enter a menu \n1. Smartphone List \n2. The Best Smartphone List",)
            ),
            (
                r'what is the spesification of samsung galaxy s21 ultra 5g?|show the spesification of samsung galaxy s21 ultra 5g',
                ("",)
            ),
            (
                r'what is the spesification of oppo find x3 pro?|show the spesification of oppo find x3 pro',
                ("",)
            ),
            (
                r'what is the spesification of huawei mate x2? |show the spesification of huawei mate x2',
                ("",)
            ),
            (
                r'what is the spesification of apple iphone 12 pro max?|show the spesification of apple iphone 12 pro max',
                ("",)
            ),
            (
                r'what is the spesification of xiaomi mi 11 ultra?|show the spesification of xiaomi mi 11 ultra',
                ("",)
            ),
            (
                r'what is the spesification of samsung galaxy z fold2 5g?|show the spesification of samsung galaxy z fold2 5g',
                ("",)
            ),
            (
                r'what is the spesification of vivo x60 pro+?|show the spesification of vivo x60 pro+',
                ("",)
            ),
            (
                r'how much is samsung galaxy s21 ultra 5g?',
                ("The price of samsung galaxy s21 ultra 5g is 12.844.723 rupiah",)
            ),
            (
                r'how much is oppo find x3 pro?',
                ("The price of oppo find x3 pro is 12.298.751 rupiah",)
            ),
            (
                r'how much is huawei mate x2?',
                ("The price of huawei mate x2 is 40.253.805 rupiah",)
            ),
            (
                r'how much is apple iphone 12 pro max?',
                ("The price of apple iphone 12 pro max is 15.215.394 rupiah",)
            ),
            (
                r'how much is xiaomi mi 11 ultra?',
                ("The price of xiaomi mi 11 ultra is 18.663.642 rupiah",)
            ),
            (
                r'how much is samsung galaxy z fold2 5g?',
                ("The price of samsung galaxy z fold2 5g is 23.261.306 rupiah",)
            ),
            (
                r'how much is vivo x60 pro+?',
                ("The price of vivo x60 pro+ is 16.752.738 rupiah",)
            ),
            (
                r'what is the best smartphone for now?',
                ("The best smartphone is samsung galaxy s21 ultra 5g",)
            ),
            (
                r'what is the most expensive smartphone here?',
                ("The price of  Huawei Mate X2 is 40 million rupiah, it is the most expensive smartphone here",)
            ),
            (
                r'what is the cheapest smartphone here?',
                ("The price of  Oppo Find X3 Pro is 12 million rupiah, it is the cheapest smartphone here",)
            ),
            (
                r'goodbye|bye',
                ("goodbye", "have a nice day",)
            ),
            (
                r'thank you ',
                ("you are welcome",)
            ),
            (
                r'(.*)',
                ("sorry, I do not understand",)
            ),
        )

        menu1 = open("menu_daftarsmartphone.txt", "r")
        self.menu1 = menu1.read()

        menu2 = open("menu_rekomendasismartphone.txt", "r")
        self.menu2 = menu2.read()

        spek_samsungs21ultra = open("spek_samsungs21ultra.txt", "r")
        self.spek_samsungs21ultra = spek_samsungs21ultra.read()

        spek_findx3pro = open("spek_findx3pro.txt", "r")
        self.spek_findx3pro = spek_findx3pro.read()

        spek_huaweimatex2 = open("spek_huaweimatex2.txt", "r")
        self.spek_huaweimatex2 = spek_huaweimatex2.read()

        spek_iphone12promax = open("spek_iphone12promax.txt", "r")
        self.spek_iphone12promax = spek_iphone12promax.read()

        spek_mi11ultra = open("spek_mi11ultra.txt", "r")
        self.spek_mi11ultra = spek_mi11ultra.read()

        spek_samsungzfold2 = open("spek_samsungzfold2.txt", "r")
        self.spek_samsungzfold2 = spek_samsungzfold2.read()

        spek_vivox60pro = open("spek_vivox60pro.txt", "r")
        self.spek_vivox60pro = spek_vivox60pro.read()

        self.bot = Chat(pairs, reflections)


    def sendmessage(self):
        s = self.textInput.toPlainText()
        s = s.lower()
        self.textOutput.append("<b>You : "+s+"</b>")
        if s:
            if s in ["show menu1","show menu smartphone list"]:
                self.textOutput.append("BOT : " + self.bot.respond(s))
                self.textOutput.append(self.menu1)
            elif s in ["show menu2","show menu the best smartphone list"]:
                self.textOutput.append("BOT : " + self.bot.respond(s))
                self.textOutput.append(self.menu2)
            elif s in ["what is the spesification of samsung galaxy s21 ultra 5g?","what is the spesification of samsung galaxy s21 ultra 5g","show the spesification of samsung galaxy s21 ultra 5g"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_samsungs21ultra)
            elif s in ["what is the spesification of oppo find x3 pro?","what is the spesification of oppo find x3 pro","show the spesification of oppo find x3 pro"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_findx3pro)
            elif s in ["what is the spesification of huawei mate x2?","what is the spesification of huawei mate x2", "show the spesification of huawei mate x2"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_huaweimatex2)
            elif s in ["what is the spesification of apple iphone 12 pro max?","what is the spesification of apple iphone 12 pro max","show the spesification of apple iphone 12 pro max"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_iphone12promax)
            elif s in ["what is the spesification of xiaomi mi 11 ultra?","what is the spesification of xiaomi mi 11 ultra","show the spesification of xiaomi mi 11 ultra"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_mi11ultra)
            elif s in ["what is the spesification of samsung galaxy z fold2 5g?","what is the spesification of samsung galaxy z fold2 5g","show the spesification of samsung galaxy z fold2 5g"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_samsungzfold2)
            elif s in ["what is the spesification of vivo x60 pro+?","what is the spesification of vivo x60 pro+","show the spesification of vivo x60 pro+"]:
                self.textOutput.append("BOT : " +self.bot.respond(s))
                self.textOutput.append(self.spek_vivox60pro)
            else:
                self.textOutput.append("BOT : "+self.bot.respond(s))
            self.textInput.clear()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Close Chatbot', 'Do You Want to Close Chatbot?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = ShowImage()
    Window.setWindowTitle("Chatbot.exe")
    Window.show()
    sys.exit(app.exec_())