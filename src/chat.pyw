__author__ = 'Chelsea, Robin, Chris, Catherine'

from chatapp import *
import sys
import os
import aiml
import random
import time
from spellcheck import correct
# import socket
# from thread import *


class ChatApplication(QtGui.QMainWindow):

    # setup window
    def __init__(self, parent=None):
        # setup the gui
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load kernel
        self.kernel = aiml.Kernel()
        self.kernel.setBotPredicate('gender', 'male')
        self.kernel.setBotPredicate('species', 'human')
        #self.kernel.setBotPredicate('nationality',)
        #self.kernel.setBotPredicate('location',)
        #self.kernel.setBotPredicate('favouritecolor',)
        #self.kernel.setBotPredicate('favouritemovie',)
        #self.kernel.setBotPredicate('birthplace',)
        #self.kernel.setBotPredicate('friends',)
        #print self.kernel.getBotPredicate('gender')


        # connect the buttons to the methods
        QtCore.QObject.connect(self.ui.sendMessage_Button, QtCore.SIGNAL('clicked()'), self.send_message)
        QtCore.QObject.connect(self.ui.clearLogs_Button, QtCore.SIGNAL('clicked()'), self.clear_logs)
        QtCore.QObject.connect(self.ui.connect_Button, QtCore.SIGNAL('clicked()'), self.connect)
        QtCore.QObject.connect(self.ui.disconnectButton, QtCore.SIGNAL('clicked()'), self.disconnect)

        self.ui.actionExit.triggered.connect(self.exit)

        self.user_list = []
        self.previous_message = ""
        self.list = []
        self.newlist = []
        self.system_names = ['userA', 'userB']
        self.response = ""

    def load_brain(self):

        # change this to wherever your directory is

        os.chdir('C:\Users\user\Desktop\GroupProject')

        # if brain file is in directory, load it else load aiml files and create brain file.
        if os.path.isfile('brain.brn'):
            self.kernel.bootstrap(brainFile='brain.brn')
        else:
            self.kernel.bootstrap(learnFiles='startup.xml', commands='load aiml b')
            self.kernel.saveBrain('brain.brn')

    # Starts conversation with user
    def start_conversation(self):

        self.clear_logs()

        self.ui.listWidget.addItem(self.user_list[1] + ":" + "Hello")

    # Sends user message to list, checks are made
    def send_message(self):

        self.clear_logs()

        message = str(self.ui.lineEdit_2.text())
        current_message = message.lower()

        if current_message != "" and current_message == self.previous_message:
            self.ui.listWidget.addItem(self.user_list[0] + ": " + message)
            self.ui.lineEdit_2.clear()
            call_out = ["Please don't repeat yourself", "You are repeating yourself", "Theres no need for repetition", "Stop it", "Well thats annoying"]
            self.ui.listWidget.addItem(self.user_list[1] + ": " + random.choice(call_out))

        if current_message == "":
            error = QtGui.QMessageBox.information(self, 'Error', "You need to enter a message!", QtGui.QMessageBox.Ok)

            # add pop up window telling user to type text, null values is not allowed.

        if current_message != self.previous_message:

            self.ui.listWidget.addItem(self.user_list[0] + ": " + message)
            self.previous_message = current_message
            self.ui.lineEdit_2.clear()

            check = self.check_spelling(current_message)
            self.respond(check)
            self.save_conversation(message)



    # Function to respond to user input
    def respond(self, message):
        self.response = (self.kernel.respond(message))
        self.ui.listWidget.addItem(self.user_list[1] + ": " + self.response)

    #Function to reload aiml files
    def reload_brain(self):

        self.kernel.bootstrap(learnFiles='startup.xml', commands='load aiml b')
        self.kernel.saveBrain('brain.brn')

    # Clears the screen
    def clear_logs(self):
        self.ui.listWidget.clear()

    # Adds user to list
    def connect(self):

        try:
            if self.ui.lineEdit.text() == "":
                error = QtGui.QMessageBox.information(self, 'Error', "You need to enter your name!", QtGui.QMessageBox.
                                                      Ok)
            else:

                answer = "Connecting to user..."
                self.ui.listWidget.addItem(answer)

                ai_system = 'userA'
                answer = "Connection Established"
                self.ui.listWidget.addItem(answer)

                del answer

                if str(self.ui.lineEdit.text()) in self.user_list:

                    # change to pop up window telling user name already exists.
                    print "name already exists please choose another"

                else:
                    self.user_list.append(str(self.ui.lineEdit.text()))

                    if 'userA' in self.user_list:

                        self.user_list.remove('userA')
                        ai_system = 'userB'
                        self.user_list.append(ai_system)

                    else:
                        self.user_list.append(ai_system)

                    self.ui.lineEdit.clear()

                    for name in self.user_list:

                        self.ui.listWidget_2.addItem(name)

                    self.start_conversation()


        except:

            pass

    # Disconnect judge from user
    def disconnect(self):
        self.ui.listWidget_2.clear()
        self.user_list.remove(self.user_list[0])

    # Saves a log of the conversation
    def save_conversation(self, message):

        file = open(str(self.user_list), 'a')

        #self.response = (self.kernel.respond(message))

        file.write(self.user_list[0] + ": " + message + "\n")
        file.write(self.user_list[1] + ": " + self.response + "\n")

        file.close()

    # Checks spelling of words in user input
    def check_spelling(self, message):
        # Checks if list is empty before deleting contents of list
        if not self.list:
            print "list is empty"
        else:
            del self.list[:]
            # print self.list
        # Splits message from user in this variable
        words = message.split()

        # Adds each word to the empty list
        for word in words:
            self.list.append(word)

        # Checks if the new list is empty before deleting its contents
        if not self.newlist:
            print " new list is empty"
        else:

            del self.newlist[:]
            # print self.newlist
        # Loops through each word in list, corrects them then adds to new list.
        for item in self.list:
            corr = correct(item)

            self.newlist.append(corr)
        # print self.newlist
        # Contents of new list is then placed in a variable and into a readable format.
        checked_message = ' '.join(self.newlist)

        # Returns the checked message for system to look through aiml files for a response.
        return checked_message

    # Exits application
    def exit(self):

        self.close()

# Execute application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ChatApplication()
    myapp.load_brain()
    myapp.show()
    sys.exit(app.exec_())