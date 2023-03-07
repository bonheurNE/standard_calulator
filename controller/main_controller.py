from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6 import QtGui, QtCore

from views.ui_standard import *
from model import main_model

import json


class MainController(QWidget):
    def __init__(self, tempDire):
        super().__init__()
        self.ui = Ui_standard_mode_widget()
        self.ui.setupUi(self)

        # define  data
        self.defineData()
        self._temp_history_folder = tempDire
        
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
        print(f"first number {value}")
        if empty == True:
            self._first_entered_number = [0]
        else:
            self._first_entered_number[0] = value

    def getFirstNumber(self) -> float:
        return self._first_entered_number[0]
    
    def getSecondNumber(self) -> float:
        return self._second_entered_number[0]

    def setSecondNumber(self, value: float = 0.0, empty: bool =False) -> None:
        print(f"second number {value}")
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
            if s_number < 0 and f_number >= 0:
                self._result = (f_number) - abs(s_number)
            elif f_number < 0 and s_number >= 0:
                self._result = (s_number) - abs(f_number)
            else:
                self._result = (f_number) + (s_number)
        
        elif operator == "X":
            self._result = (f_number) * (s_number)
        
        elif operator == "/":
            if s_number == 0:
                self._result = "Error"
            else:
                self._result = (f_number) / (s_number)
            
        elif operator == "-":
            self._result = (f_number) - (s_number)
            
        print(f"the result as result func {self._result}")
        # set the result to the entry
        # check if the result is a number or an error text
        if isinstance(self._result, (int, float)):
            self.ui.standard_calc_entry.setText(f"{round(self._result, 4)}")
        else:
            self.ui.standard_calc_entry.setText(f"{self._result}")
        
        

    def getResult(self) -> float | int | str:
        if isinstance(self._result, str):
            return self._result
        else:
            return round(self._result, 4)
        
    def setHistoryNewData(self, data:tuple):
        # define the initial data ID
        ID = 0
        
        # define the data to add
        data = f"{data[0]} {data[1]} {data[2]} = {data[3]}"
        
        # open the temp history file
        with open(self._history_file_path, 'r') as f:
            json_data = json.load(f)
        
        # get the size of json_data
        json_data_size = len(json_data)
        
        # check if the file dict is empty to use the initial id or increment the id
        if json_data_size == 0:
            # if the file dict is empty set the initial id to 0
            json_data[ID] = data
        else:
            # get the last ID in the data dict
            last_id = list(json_data.keys())
            last_id = max(last_id)
            print(f"max id = {type(last_id)}")
            # increment the ID 
            last_id = int(last_id)+1
            
            json_data[last_id] = data
        # write the new data to the json file
        with open(self._history_file_path, 'w') as file_:
            json.dump(json_data, file_, indent=4)
            
        print(json_data)
    
    def getHistoryData(self, data_id:int = 0) -> None:
        # open the history temp json file to get the json data
        with open( self._history_file_path, 'r') as f:
            json_data = json.load(f)
        
        # look for the data of the specific id
        data_id = str(data_id)
        data = json_data[data_id]
        
        
        # separate data by = sign
        data_ = data.split('=')
        
        data__ = data_[0]
        # separate data by + sign
        if '+' in data_[0]:
            data__ = data__.split('+')
            operator = '+'
        elif '-' in data_[0]:
            data__ = data__.split('-')
            operator = '-'
        elif 'X' in data_[0]:
            data__ = data__.split('X')
            operator = 'X'
        elif '/' in data_[0]:
            data__ = data__.split('/')
            operator = '/'
        
        # assign the first, second, result they specific numbers
        self.setFirstNumber(value=float(data__[0]))
        self.setSecondNumber(value=float(data__[0]))
        self.setResult(f_value=float(data__[0]), s_value=float(data__[1]),operator=operator)
        
        # complete the temp
        self.completTemp(f_number=self.getFirstNumber(), s_number=self.getSecondNumber(), precedent_operator=operator, result= self.getResult())

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
            
            # clean the calculation entry
            self.ui.standard_calc_entry.setText("")
            
            
            
            
        elif self.getFirstNumber() != 0 and self.getSecondNumber() == 0:
            print("second case")
            
            # assign the current number to the second number variable
            self.setSecondNumber(value=number, empty=False)
            
            # calculate the result ,set the result to the result variable and print the result 
            self.setResult(f_value=self.getFirstNumber(), s_value=self.getSecondNumber(), operator=self.getPrecedentOperator())
            
            # add to history
            self.setHistoryNewData((self.getFirstNumber(),self.getPrecedentOperator(),self.getSecondNumber(),self.getResult()))
            # manage the next stage by checking the used operator
            if used_operator in ["+","-","/","X"]:
                
                # get the last  result
                last_result = self.getResult()
                
                # get the current value on the edit
                #current_text = self.ui.standard_calc_entry.text()
                
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
        
        
    def memoryButton(self, button:str="") -> None:
        # get the text of the clicked button
        button_value = button
        if button_value == "CE":
                # clear the calculation entry
                self.ui.standard_calc_entry.setText("")
                
                # reset the second number
                self.setSecondNumber(empty=True)
                
        elif button_value == "C":
            # clear the calculation entry
            self.ui.standard_calc_entry.setText("0")
            
            # clear the temp label
            self.ui.standard_temp_label.setText("")
            
            # reset the second number
            self.setSecondNumber(empty=True)
            # reset the first number
            self.setFirstNumber(empty=True)
            
        elif button_value == "MC":
            pass
        
        elif button_value == "MR":
            pass
        
        elif button_value == "MS":
            pass
        
        elif button_value == "M-":
            pass
        
        elif button_value == "M+":
            pass
        pass
    
    def plusMinusBnt(self):
        """ change the sing of the current number
            if the current number was positive it's will be preceded by a negative sign
            if the current number was negative it's will be preceded by a positive sign"""
        
        # get the current text number 
        current_text = self.ui.standard_calc_entry.text()
        
        # get the first character
        first_character = current_text[0]
        print(first_character)
        
        # check the first character
        if first_character == "+" or first_character != "-":
            # define the new negative number
            new_text = f"-{current_text}"
            
            # set the new number to the entry
            self.ui.standard_calc_entry.setText(new_text)
            
        elif first_character == "-":
            # define the new positive number by removing the first character
            new_text = current_text[1:]
            new_text = f"{new_text}"
            
            # set the new number to the entry
            self.ui.standard_calc_entry.setText(new_text)
    
    def _createHistoryFile(self):
        sample = {}
        
        # create the file named history.json on the directory model
        self._history_file_path = self._temp_history_folder +"/history.json"
        
        with open(self._history_file_path, 'w') as f:
            json.dump(sample, f, indent=4) 
        
        print("history file created created")

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
        self._history_file_path = ""
         
        
        
        pass
    
    def initialiseData(self):
        
        self.setFirstNumber(empty=True)
        self.setSecondNumber(empty=True)
        
        # create and initialize the history json file
        self._createHistoryFile()
        
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
            if current_text == str(self.getResult()):
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
            
        elif button_value in range(15,18):
            if button_value == 15:
                pass
                
            elif button_value == 16:
                """ remove the last character on the current text 
                    define the function of the delete button """
                # get the current text on the entry
                current_text = self.ui.standard_calc_entry.text()
                
                # remove the last number 
                new_text = current_text[:-1]
                
                # set the new text to the entry
                self.ui.standard_calc_entry.setText(new_text) 
                
            elif button_value == 17:
                """ put a point in the current number 
                    if the current number is empty set the initial number as 0 """
                    
                # get the current text on the entry
                current_text = self.ui.standard_calc_entry.text()
                
                # check if the current number begin with a number different from 0
                if current_text == "":
                    self.ui.standard_calc_entry.setText("0.")
                    
                # check if there is a point in the current number do not add an other
                elif "." in current_text:
                    pass
                 
                else:
                    new_text = f"{current_text}."
                
                    # set the new text to the entry
                    self.ui.standard_calc_entry.setText(new_text) 
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
        
        #####################################################
        # DEFINING ACTIONS FOR EXTRATS OPERATIONS   BUTTONS #
        #####################################################
        
        self.ui.standard_btn_prcnt.clicked.connect(
            (lambda: self.completEntryByBtn(button=15)))
        self.ui.standard_btn_delete.clicked.connect(
            (lambda: self.completEntryByBtn(button=16)))
        self.ui.standard_btn_point.clicked.connect(
            (lambda: self.completEntryByBtn(button=17)))
        
        # plus minus change button
        
        self.ui.standard_btn_plus_minus.clicked.connect(
            (lambda: self.plusMinusBnt()))
        
        ###########################################
        # DEFINING ACTIONS FOR EXTRATS    BUTTONS #
        ###########################################
        
        self.ui.standard_btn_C.clicked.connect(lambda:self.memoryButton(button="C"))
        self.ui.standard_btn_CE.clicked.connect(lambda:self.memoryButton(button="CE"))
        self.ui.standard_btn_MC.clicked.connect(lambda:self.memoryButton(button="MC"))
        self.ui.standard_btn_MR.clicked.connect(lambda:self.memoryButton(button="MR"))
        self.ui.standard_btn_MS.clicked.connect(lambda:self.memoryButton(button="MS"))
        self.ui.standard_btn_M_minus.clicked.connect(lambda:self.memoryButton(button="M-"))
        self.ui.standard_btn_M_plus.clicked.connect(lambda:self.memoryButton(button="M+"))
