from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6 import QtGui, QtCore

from views.ui_standard import *
from model import main_model


class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_standard_mode_widget()
        self.ui.setupUi(self)

        # define  data
        self.defineData()
        
        # initialise data
        self.initialiseData()
        
        # initialize the widget setup
        self.setUpWidget()
        
        # setup calculation buttons actions
        self.calculationBtnsAction()
        
    def setPrecedentOperator(self, operator:str = ""):
        self._precedent_operator = operator
        #self.ui.standard_calc_entry.setText("0")
        pass
    
    def getPrecedentOperator(self) -> str:
        return self._precedent_operator
    
    def setFirstNumber(self, value: float = 0.0, empty: bool =False) -> None:
        if empty == True:
            self._first_entered_number = [0]
        else:
            self._first_entered_number[0] = value

    def getFirstNumber(self) -> float:
        return self._first_entered_number[0]
    
    def getSecondNumber(self) -> float:
        return self._second_entered_number[0]

    def setSecondNumber(self, value: float = 0.0, empty: bool =False) -> None:
        if empty == True:
            self._second_entered_number = [0]
        else:
            self._second_entered_number[0] = value

    

    def setResult(self, f_value: float = 0.0, s_value: float = 0.0, operator:str = "") -> None:
        #g get the first and sec ond number seted
        f_number = f_value
        s_number = s_value
        
        # get used operator
        operator = operator
        
        # manage operation
        if operator == "+":
            self._result = f_number + s_number
        
        elif operator == "X":
            self._result = f_number * s_number
        
        elif operator == "/":
            self._result = f_number / s_number
            
        elif operator == "-":
            self._result = f_number - s_number
            
        print(f"the result as result func {self._result}")
        # set the result to the entry
        #self.ui.standard_calc_entry.setText("")
        self.ui.standard_calc_entry.setText(f"{self._result}")
        

    def getResult(self) -> float | int:
        return self._result

    def setEnteredNumber(self, number: float, operator:str = ""):
        # get the current value on the entry
        current_number = number
        
        # get the used operator symbol
        used_operator = operator
        
        # MANAGE NUMBERS LOCATIONS
        print("precedent stage")
        print(self.getFirstNumber())
        print(self.getSecondNumber())

        if self.getFirstNumber() == 0 and self.getSecondNumber() == 0:
            
            """"if first number and second numbers are both empty """
            # assign the current number to the first number variable
            self.setFirstNumber(value=current_number, empty=False)
            
            # assign the used operator to the precedent operator variable
            self.setPrecedentOperator(operator=used_operator)
            
            print("first stage")
            print(self.getFirstNumber())
            print(self.getSecondNumber())
            
            # use the f_number and the used operator to print  the temp "f_number used_operator"
            self.simpleTemp(first_number=self.getFirstNumber(), operator=self.getPrecedentOperator())
            
            
            
            
        elif self.getFirstNumber() != 0 and self.getSecondNumber() == 0:
            print("second case")
            
            # assign the current number to the second number variable
            self.setSecondNumber(value=number, empty=False)
            
            # calculate the result ,set the result to the result variable and print the result 
            self.setResult(f_value=self.getFirstNumber(), s_value=self.getSecondNumber(), operator=self.getPrecedentOperator())
            
            # manage the next stage by checking the used operator
            if used_operator in ["+","-","/","X"]:
                # get the last  result
                last_result = self.getResult()
                
                # assign this result value as the new value of the first_number
                self.setFirstNumber(value=last_result, empty=False)
                
                self.setSecondNumber(empty=True)
                
                print("second 1 stage")
                print(self.getFirstNumber())
                print(self.getSecondNumber()) # always empty
                
                # assign the used operator as the new value of the precedent used operator variable
                self.setPrecedentOperator(operator=used_operator)
                
                # use the new f_number and the  new used operator to print  the temp "f_number used_operator"
                self.simpleTemp(first_number=self.getFirstNumber(), operator=self.getPrecedentOperator())
            
            elif used_operator == "=":
                # print the comlete temp like : "f_number operator s_second = result"
                self.completTemp(f_number = self.getFirstNumber(), s_number=self.getSecondNumber(), precedent_operator=self.getPrecedentOperator(), result=self.getResult())
                 
                print("second 2 stage")
                print(self.getFirstNumber())
                print(self.getSecondNumber())
                # initialize all the two variables
                self.setFirstNumber(empty=True)
                self.setSecondNumber(empty=True)
                self.result_ = 0.0
                self._used_operator = ""
                self._precedent_operator = ""
                self._precedent_operator = ""

        """ elif len(self._first_entered_number) != 0 and len(self._second_entered_number) != 0:
            # set the result
            self.setResult(self.getFirstNumber(), self.getSecondNumber())
            # initialize all the two variables
            self.setFirstNumber(empty=True)
            self.setSecondNumber(empty=True) """
            
        pass
    
    def simpleTemp(self, first_number:float = 0,operator:str = "") -> None:
        text_ = f"{first_number} {operator}"
        
        # set the temp operator as the temp entry data
        self.ui.standard_temp_label.setText(text_)
        
        #self.ui.standard_calc_entry.setText(f"{first_number}")
        pass
    
    def completTemp(self, f_number:float = 0.0, s_number:float = 0.0, precedent_operator:str = "", result:float = 0.0):
        # get the first and second numbers values and the precedent operator
        f_number = f_number
        s_number = s_number
        p_operator = precedent_operator
        
        # get the result value
        result_ = result
        
        # create the temp text
        text_ = f"{f_number} {p_operator} {s_number} = {result_}"
        print(f"result {text_}")
        # set the text to the temp label
        self.ui.standard_temp_label.setText(text_)
        #self.ui.standard_calc_entry.setText(f"{f_number}")
    
    

    def defineData(self):
        """ initializing all data we will need to use 
            in our code as:
            * the variable to hold the value entred in the prencipal entry edit
            * the variable to hold the result of of calculation
            * the variable to hold the text to print on the TEMP RESULT LABEL
            """
        
        # INITIALIZING DATA VARIABLE
        self._first_entered_number = [0]
        self._second_entered_number = [0]
        self._result = 0.0
        self._used_operator = ""
        self._precedent_operator = ""
        self._temp_operation = ""
        
        pass
    
    def initialiseData(self):
        
        self.setFirstNumber(empty=True)
        self.setSecondNumber(empty=True)
        
        pass
        
    def setUpWidget(self):
        # removing window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.ui.standard_calc_entry.setText("0")
        pass
    
    def completEntryByBtn(self, button:int):
        
        # get the value of the clicked button
        button_value = button
        
        # get the current text on the text entry 
        current_text = self.ui.standard_calc_entry.text()
        
        if button_value in range(10) and current_text == "0":
            self.ui.standard_calc_entry.setText("")
            
            new_text = f"{button_value}"
            
            self.ui.standard_calc_entry.setText(new_text)
            
        elif button_value in range(10) and current_text != "0":
            print(f"first number {self.getFirstNumber()}")
            print(f"second number {self.getSecondNumber()}")
            if current_text == str(self.getResult()) :
                self.ui.standard_calc_entry.setText("")
                new_text = f"{button_value}"
            
                # set updated data to the entry
                self.ui.standard_calc_entry.setText(new_text)
            
            else:
            
                new_text = f"{current_text}{button_value}"
            
                # set updated data to the entry
                self.ui.standard_calc_entry.setText(new_text)
            
            
        elif button_value in range(10,15) :
            # manage current entry data getUp
            current_number = float(current_text)
            
            
            # define the used operator
            if button_value == 10:
                self._used_operator = "+"
            
            elif button_value == 11:
                self._used_operator = "-"
            
            elif button_value == 12:
                self._used_operator = "/"
                
            elif button_value == 13:
                self._used_operator = "X"
                
            elif button_value == 14:
                self._used_operator = "="
                
            # manage settingUp of numbers 
            # place the preview current number in the first_number or second_number list
            self.setEnteredNumber(number=current_number,operator = self._used_operator)
            
            # manage temp label
            #self.setTempData()
            
            # initialize the entry
            """ if self.getPrecedentOperator() != "=":
                self.ui.standard_calc_entry.setText("0")
            elif self.getPrecedentOperator() == "=":
                self.ui.standard_calc_entry.setText("78")
            """
        pass

        
    def calculationBtnsAction(self):
        ################################
        # DEFINING BUTTONS     ACTIONs #
        ################################
        
        self.ui.standard_btn0.clicked.connect(
            lambda:self.completEntryByBtn(button= 0))
        self.ui.standard_btn1.clicked.connect(
            lambda:self.completEntryByBtn(button=1))
        self.ui.standard_btn2.clicked.connect(
            lambda:self.completEntryByBtn(button=2))
        self.ui.standard_btn3.clicked.connect(
            lambda:self.completEntryByBtn(button=3))
        self.ui.standard_btn4.clicked.connect(
            lambda: self.completEntryByBtn(button=4))
        self.ui.standard_btn5.clicked.connect(
            lambda: self.completEntryByBtn(button=5))
        self.ui.standard_btn6.clicked.connect(
            lambda: self.completEntryByBtn(button=6))
        self.ui.standard_btn7.clicked.connect(
            lambda: self.completEntryByBtn(button=7))
        self.ui.standard_btn8.clicked.connect(
            lambda: self.completEntryByBtn(button=8))
        self.ui.standard_btn9.clicked.connect(
            lambda: self.completEntryByBtn(button=9))
        
        ###########################################
        # DEFINING ACTIONS FOR OPERATIONS BUTTONS #
        ###########################################
        
        self.ui.standard_btn_addition.clicked.connect(
            (lambda: self.completEntryByBtn(button=10)))
        self.ui.standard_btn_minus.clicked.connect(
            (lambda: self.completEntryByBtn(button=11)))
        self.ui.standard_btn_division.clicked.connect(
            (lambda: self.completEntryByBtn(button=12)))
        self.ui.standard_btn_multiplication.clicked.connect(
            (lambda: self.completEntryByBtn(button=13)))
        self.ui.standard_btn_equal.clicked.connect(
            (lambda: self.completEntryByBtn(button=14)))
