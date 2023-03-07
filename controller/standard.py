import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6 import QtGui, QtCore

from view.ui_standard import *

from controller.history import HistoryWd

from view.ui_history import Ui_Form


class HistoryWd(QWidget):
    def __init__(self):
        super(HistoryWd, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def setNewHistory(self, btn_numbe: int, data: str):
        # create push button containning our history
        btn = QPushButton(self)
        btn.setText(data)
        btn.setStyleSheet(u"""background-color:transparent;
                          color: skyblue;""")

        self.ui.history_layout.addWidget(btn, btn_numbe, Qt.AlignTop)
        pass


class StandarWd(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_standard_mode_widget()
        self.ui.setupUi(self)
        
        self.hist = HistoryWd()
        
        # initialise data function
        self.initialiseData()
        
        # setup the widget
        self.setUpWidget()
        
        #set up calculation buttons
        self.calculationBtnsAction()
        
    def initialiseData(self):
        self.first_number = 0
        self.second_number = 0
        self.result = 0
        self.label_print = ""
        self.history_label = ""
        
        pass
    def setUpWidget(self):
        # removing window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.ui.standard_calc_entry.setText("0")
        pass
    
    def calculationBtnsAction(self):
        ################################
        # DEFINING ACTIONS FOR BUTTONS #
        ################################
        
        
        self.ui.standard_btn0.clicked.connect(lambda:self.completEntryByBtn(0))
        self.ui.standard_btn1.clicked.connect(lambda:self.completEntryByBtn(1))
        self.ui.standard_btn2.clicked.connect(lambda:self.completEntryByBtn(2))
        self.ui.standard_btn3.clicked.connect(lambda:self.completEntryByBtn(3))
        self.ui.standard_btn4.clicked.connect(
            lambda: self.completEntryByBtn(4))
        self.ui.standard_btn5.clicked.connect(
            lambda: self.completEntryByBtn(5))
        self.ui.standard_btn6.clicked.connect(
            lambda: self.completEntryByBtn(6))
        self.ui.standard_btn7.clicked.connect(
            lambda: self.completEntryByBtn(7))
        self.ui.standard_btn8.clicked.connect(
            lambda: self.completEntryByBtn(8))
        self.ui.standard_btn9.clicked.connect(
            lambda: self.completEntryByBtn(9))
        
        ###########################################
        # DEFINING ACTIONS FOR OPERATIONS BUTTONS #
        ###########################################
        
        self.ui.standard_btn_addition.clicked.connect(
            (lambda: self.completEntryByBtn(10)))
        self.ui.standard_btn_minus.clicked.connect(
            (lambda: self.completEntryByBtn(11)))
        self.ui.standard_btn_division.clicked.connect(
            (lambda: self.completEntryByBtn(12)))
        self.ui.standard_btn_multiplication.clicked.connect(
            (lambda: self.completEntryByBtn(13)))
        self.ui.standard_btn_equal.clicked.connect(
            (lambda: self.completEntryByBtn(14)))
        
    
    
    
    def completEntryByBtn(self, btn:int):
        
        if btn in range(10):
            # convert our button number into str
            btn_number = str(btn)
            # past entry data
            _past_entry = self.ui.standard_calc_entry.text()
            
            if len(_past_entry) == 1 and _past_entry == "0":
                self.ui.standard_calc_entry.setText("")
                _past_entry = ""
            
            _new_entry = f"{_past_entry}{btn_number}"
            
            # set updated data to the entry
            self.ui.standard_calc_entry.setText(_new_entry)
        
        elif btn in range(10,15):
            current_entry_data = self.ui.standard_calc_entry.text()
            current_number = float(current_entry_data)
            
            if btn == 10:
                # make addition
                
                #initialise the entry
                self.ui.standard_calc_entry.setText("0")
                # check if the first number is equal to zero
                if self.first_number == 0 and self.result == 0 and self.label_print == "" and self.history_label == "":
                    self.first_number = current_number
                    self.result = self.first_number + self.second_number
                    
                    if self.label_print == "":
                        self.label_print = f"{self.first_number} "
                        self.history_label = f"{self.first_number}\n {self.first_number}"
                        
                        self.hist.setNewHistory(1, self.history_label)
                        self.ui.standard_temp_label.setText(self.label_print)
                
                else:
                    self.first_number = current_number
                    self.result = self.result + self.first_number
                    
                    self.label_print = f"{self.label_print} + {str(self.first_number)}"
                    self.history_label = f"<html><body>{self.label_print}\n<b>{self.result}</b></body></html>"
                    self.ui.standard_temp_label.setText(self.label_print)
                
            elif btn == 11:
                
                # make substraction

                #initialise the entry
                self.ui.standard_calc_entry.setText("0")
                
                # check if the first number is equal to zero // for the first time
                if self.first_number == 0 and self.result == 0 and self.label_print == "" and self.label_print == "":
                    self.first_number = current_number
                    self.result = self.first_number - self.second_number

                    if self.label_print == "":
                        self.label_print = f"{self.first_number} "
                        self.history_label = f"{self.first_number}\n<b> {self.first_number}</b>"

                        self.ui.standard_temp_label.setText(self.label_print)

                else:
                    self.first_number = current_number
                    self.result = self.result - self.first_number

                    self.label_print = f"{self.label_print} - {str(self.first_number)}"
                    self.history_label = f"{self.label_print}\n<b>{self.result}</b>"
                    self.ui.standard_temp_label.setText(self.label_print)
            

            """ if current_entry_data == "":
                self.first_number = 0
                self.ui.standard_calc_entry.setText("0")
                self.ui.standard_temp_label.setText("0 + ")
                
            else:
                # clear entry
                self.ui.standard_calc_entry.setText("0")
                
                # check if the first number is 0
                if self.first_number == 0:
                    self.first_number = float(current_entry_data)
                    self.ui.standard_temp_label.setText(
                        f"{str(self.first_number)}")
                else:
                    self.second_number = self.first_number + float(current_entry_data)
                    
                    # get current label text and add the second number
                    lb_current_text = self.ui.standard_temp_label.text()
                    
                    self.ui.standard_temp_label.setText(
                        f"{lb_current_text} + {str(self.second_number)}") """
                     
                
                
                
        
        pass
    
    ########################
    # MANAGING KEYS EVENTS #
    ########################
    
    def keyPressEvent(self, event):
        _entry = self.ui.standard_calc_entry.text()
        if len(_entry) == 1 and _entry == "0":
            _entry = ""
      
        if event.key() == Qt.Key.Key_0:
            self.ui.standard_calc_entry.setText(f"{_entry}0")
        elif event.key() == Qt.Key.Key_1:
            self.ui.standard_calc_entry.setText(f"{_entry}1")
        elif event.key() == Qt.Key.Key_2:
            self.ui.standard_calc_entry.setText(f"{_entry}2")
        elif event.key() == Qt.Key.Key_3:
            self.ui.standard_calc_entry.setText(f"{_entry}3")
        elif event.key() == Qt.Key.Key_4:
            self.ui.standard_calc_entry.setText(f"{_entry}4")
        elif event.key() == Qt.Key.Key_5:
            self.ui.standard_calc_entry.setText(f"{_entry}5")
        elif event.key() == Qt.Key.Key_6:
            self.ui.standard_calc_entry.setText(f"{_entry}6")
        elif event.key() == Qt.Key.Key_7:
            self.ui.standard_calc_entry.setText(f"{_entry}7")
        elif event.key() == Qt.Key.Key_8:
            self.ui.standard_calc_entry.setText(f"{_entry}8")
        elif event.key() == Qt.Key.Key_9:
            self.ui.standard_calc_entry.setText(f"{_entry}9")
            
        elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Equal:
            print("equal action")
            #self.ui.standard_calc_entry.setText(f"{_entry}9")
        elif event.key() == Qt.Key.Key_Backspace:
            _entry_len = len(_entry)
            _entry_new_len = _entry_len - 1
            _entry = _entry[:_entry_new_len]
            self.ui.standard_calc_entry.setText(f"{_entry}")
            
            if _entry_len == 0:
                self.ui.standard_calc_entry.setText("0")

    


# running our main programm class
""" if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StandarWd()
    window.show()
    sys.exit(app.exec()) """
