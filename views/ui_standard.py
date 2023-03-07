# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'standard.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from model.icon import icon_rc

class Ui_standard_mode_widget(object):
    def setupUi(self, standard_mode_widget):
        if not standard_mode_widget.objectName():
            standard_mode_widget.setObjectName(u"standard_mode_widget")
        standard_mode_widget.resize(396, 503)
        standard_mode_widget.setStyleSheet(u"background-color:#2d2d2d")
        self.verticalLayout = QVBoxLayout(standard_mode_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.standard_title_frame = QFrame(standard_mode_widget)
        self.standard_title_frame.setObjectName(u"standard_title_frame")
        self.standard_title_frame.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:transparent;\n"
"border:1px solid darkgrey;\n"
"}\n"
"QLabel{\n"
"color:skyblue;}\n"
"QLabel:hover{\n"
"color:rgb(0, 85, 127);\n"
"border:2px solid rgb(0, 58, 0);\n"
"	border-top-color: transparent;\n"
"border-right-color: transparent;\n"
"border-left-color: transparent;\n"
"}")
        self.standard_title_frame.setFrameShape(QFrame.StyledPanel)
        self.standard_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.standard_title_frame)
        self.horizontalLayout_14.setSpacing(19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.standard_title_icon_btn = QPushButton(self.standard_title_frame)
        self.standard_title_icon_btn.setObjectName(u"standard_title_icon_btn")
        icon = QIcon()
        icon.addFile(u":/icons/MANAS_ICON.png", QSize(), QIcon.Normal, QIcon.Off)
        self.standard_title_icon_btn.setIcon(icon)
        self.standard_title_icon_btn.setIconSize(QSize(80, 80))

        self.horizontalLayout_14.addWidget(self.standard_title_icon_btn)

        self.standard_calc_title_label = QLabel(self.standard_title_frame)
        self.standard_calc_title_label.setObjectName(u"standard_calc_title_label")

        self.horizontalLayout_14.addWidget(self.standard_calc_title_label, 0, Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(51, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.standard_title_frame)

        self.standard_calc_frame = QFrame(standard_mode_widget)
        self.standard_calc_frame.setObjectName(u"standard_calc_frame")
        self.standard_calc_frame.setStyleSheet(u"QLabel{\n"
"background-color:transparent;\n"
"color:rgb(214, 214, 214);\n"
"\n"
"}\n"
"QLineEdit{\n"
"border:2px solid rgb(218, 218, 218);\n"
"background-color:transparent;\n"
"color:rgb(139, 139, 139);\n"
"}\n"
"QLineEdit:hover{\n"
"border:2px solid rgb(0, 74, 0);\n"
"background-color:transparent;\n"
"color:rgb(214, 214, 214);\n"
"}")
        self.standard_calc_frame.setFrameShape(QFrame.StyledPanel)
        self.standard_calc_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.standard_calc_frame)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.standard_temp_label = QLabel(self.standard_calc_frame)
        self.standard_temp_label.setObjectName(u"standard_temp_label")
        self.standard_temp_label.setMinimumSize(QSize(0, 40))
        self.standard_temp_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(10)
        self.standard_temp_label.setFont(font)

        self.verticalLayout_9.addWidget(self.standard_temp_label)

        self.standard_calc_entry = QLineEdit(self.standard_calc_frame)
        self.standard_calc_entry.setObjectName(u"standard_calc_entry")
        self.standard_calc_entry.setMinimumSize(QSize(0, 60))
        self.standard_calc_entry.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.standard_calc_entry.setFont(font1)

        self.verticalLayout_9.addWidget(self.standard_calc_entry)


        self.verticalLayout.addWidget(self.standard_calc_frame)

        self.standard_memory_btn_frame = QFrame(standard_mode_widget)
        self.standard_memory_btn_frame.setObjectName(u"standard_memory_btn_frame")
        self.standard_memory_btn_frame.setStyleSheet(u"QPushButton{\n"
"color:skyblue;\n"
"border:none;\n"
"background-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"color:skyblue;\n"
"border:1px solid rgb(206, 206, 206);\n"
"background-color:rgb(73, 73, 73);\n"
"}")
        self.standard_memory_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.standard_memory_btn_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.standard_memory_btn_frame)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.standard_btn_MR = QPushButton(self.standard_memory_btn_frame)
        self.standard_btn_MR.setObjectName(u"standard_btn_MR")
        self.standard_btn_MR.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.standard_btn_MR, 0, 1, 1, 1)

        self.standard_btn_MC = QPushButton(self.standard_memory_btn_frame)
        self.standard_btn_MC.setObjectName(u"standard_btn_MC")
        self.standard_btn_MC.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.standard_btn_MC, 0, 0, 1, 1)

        self.standard_btn_MS = QPushButton(self.standard_memory_btn_frame)
        self.standard_btn_MS.setObjectName(u"standard_btn_MS")
        self.standard_btn_MS.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.standard_btn_MS, 0, 4, 1, 1)

        self.standard_btn_M_plus = QPushButton(self.standard_memory_btn_frame)
        self.standard_btn_M_plus.setObjectName(u"standard_btn_M_plus")
        self.standard_btn_M_plus.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.standard_btn_M_plus, 0, 2, 1, 1)

        self.standard_btn_M_minus = QPushButton(self.standard_memory_btn_frame)
        self.standard_btn_M_minus.setObjectName(u"standard_btn_M_minus")
        self.standard_btn_M_minus.setMinimumSize(QSize(0, 25))

        self.gridLayout_2.addWidget(self.standard_btn_M_minus, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.standard_memory_btn_frame)

        self.standard_calc_number_frame = QFrame(standard_mode_widget)
        self.standard_calc_number_frame.setObjectName(u"standard_calc_number_frame")
        self.standard_calc_number_frame.setStyleSheet(u"QPushButton{\n"
"color:skyblue;\n"
"background-color:rgb(6, 6, 6);\n"
"border:none;\n"
"border-color:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"color:skyblue;\n"
"border:1px solid rgb(206, 206, 206);\n"
"background-color:rgb(73, 73, 73);\n"
"}")
        self.standard_calc_number_frame.setFrameShape(QFrame.StyledPanel)
        self.standard_calc_number_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.standard_calc_number_frame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.label_3 = QLabel(self.standard_calc_number_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:skyblue;")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)

        self.label_2 = QLabel(self.standard_calc_number_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/activity.svg"))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.standard_btn_prcnt = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_prcnt.setObjectName(u"standard_btn_prcnt")
        self.standard_btn_prcnt.setMinimumSize(QSize(0, 40))
        self.standard_btn_prcnt.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_prcnt, 1, 0, 1, 1)

        self.standard_btn_CE = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_CE.setObjectName(u"standard_btn_CE")
        self.standard_btn_CE.setMinimumSize(QSize(0, 40))
        self.standard_btn_CE.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_CE, 1, 1, 1, 1)

        self.standard_btn8 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn8.setObjectName(u"standard_btn8")
        self.standard_btn8.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn8, 2, 1, 1, 1)

        self.standard_btn5 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn5.setObjectName(u"standard_btn5")
        self.standard_btn5.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn5, 3, 1, 1, 1)

        self.standard_btn_C = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_C.setObjectName(u"standard_btn_C")
        self.standard_btn_C.setMinimumSize(QSize(0, 40))
        self.standard_btn_C.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_C, 1, 2, 1, 1)

        self.standard_btn7 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn7.setObjectName(u"standard_btn7")
        self.standard_btn7.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn7, 2, 0, 1, 1)

        self.standard_btn9 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn9.setObjectName(u"standard_btn9")
        self.standard_btn9.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn9, 2, 2, 1, 1)

        self.standard_btn4 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn4.setObjectName(u"standard_btn4")
        self.standard_btn4.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn4, 3, 0, 1, 1)

        self.standard_btn6 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn6.setObjectName(u"standard_btn6")
        self.standard_btn6.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn6, 3, 2, 1, 1)

        self.standard_btn1 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn1.setObjectName(u"standard_btn1")
        self.standard_btn1.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn1, 4, 0, 1, 1)

        self.standard_btn_plus_minus = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_plus_minus.setObjectName(u"standard_btn_plus_minus")
        self.standard_btn_plus_minus.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn_plus_minus, 5, 0, 1, 1)

        self.standard_btn_point = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_point.setObjectName(u"standard_btn_point")
        self.standard_btn_point.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn_point, 5, 2, 1, 1)

        self.standard_btn3 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn3.setObjectName(u"standard_btn3")
        self.standard_btn3.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn3, 4, 2, 1, 1)

        self.standard_btn_delete = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_delete.setObjectName(u"standard_btn_delete")
        self.standard_btn_delete.setMinimumSize(QSize(0, 40))
        self.standard_btn_delete.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.standard_btn_delete.setIcon(icon1)

        self.gridLayout.addWidget(self.standard_btn_delete, 0, 3, 1, 1)

        self.standard_btn0 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn0.setObjectName(u"standard_btn0")
        self.standard_btn0.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn0, 5, 1, 1, 1)

        self.standard_btn_division = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_division.setObjectName(u"standard_btn_division")
        self.standard_btn_division.setMinimumSize(QSize(0, 40))
        self.standard_btn_division.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_division, 1, 3, 1, 1)

        self.standard_btn_multiplication = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_multiplication.setObjectName(u"standard_btn_multiplication")
        self.standard_btn_multiplication.setMinimumSize(QSize(0, 40))
        self.standard_btn_multiplication.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_multiplication, 2, 3, 1, 1)

        self.standard_btn_equal = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_equal.setObjectName(u"standard_btn_equal")
        self.standard_btn_equal.setMinimumSize(QSize(0, 40))
        self.standard_btn_equal.setStyleSheet(u"background-color:rgb(149, 74, 0);")

        self.gridLayout.addWidget(self.standard_btn_equal, 5, 3, 1, 1)

        self.standard_btn_minus = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_minus.setObjectName(u"standard_btn_minus")
        self.standard_btn_minus.setMinimumSize(QSize(0, 40))
        self.standard_btn_minus.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_minus, 3, 3, 1, 1)

        self.standard_btn_addition = QPushButton(self.standard_calc_number_frame)
        self.standard_btn_addition.setObjectName(u"standard_btn_addition")
        self.standard_btn_addition.setMinimumSize(QSize(0, 40))
        self.standard_btn_addition.setStyleSheet(u"background-color:rgba(19, 19, 19,155);")

        self.gridLayout.addWidget(self.standard_btn_addition, 4, 3, 1, 1)

        self.standard_btn2 = QPushButton(self.standard_calc_number_frame)
        self.standard_btn2.setObjectName(u"standard_btn2")
        self.standard_btn2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.standard_btn2, 4, 1, 1, 1)


        self.verticalLayout.addWidget(self.standard_calc_number_frame)


        self.retranslateUi(standard_mode_widget)

        QMetaObject.connectSlotsByName(standard_mode_widget)
    # setupUi

    def retranslateUi(self, standard_mode_widget):
        standard_mode_widget.setWindowTitle(QCoreApplication.translate("standard_mode_widget", u"Form", None))
        self.standard_title_icon_btn.setText("")
        self.standard_calc_title_label.setText(QCoreApplication.translate("standard_mode_widget", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Standard</span></p></body></html>", None))
        self.standard_temp_label.setText("")
        self.standard_btn_MR.setText(QCoreApplication.translate("standard_mode_widget", u"MR", None))
        self.standard_btn_MC.setText(QCoreApplication.translate("standard_mode_widget", u"MC", None))
        self.standard_btn_MS.setText(QCoreApplication.translate("standard_mode_widget", u"MS", None))
        self.standard_btn_M_plus.setText(QCoreApplication.translate("standard_mode_widget", u"M+", None))
        self.standard_btn_M_minus.setText(QCoreApplication.translate("standard_mode_widget", u"M-", None))
        self.label_3.setText(QCoreApplication.translate("standard_mode_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">MANAS COMPANY</span></p></body></html>", None))
        self.label_2.setText("")
        self.standard_btn_prcnt.setText(QCoreApplication.translate("standard_mode_widget", u"%", None))
        self.standard_btn_CE.setText(QCoreApplication.translate("standard_mode_widget", u"CE", None))
        self.standard_btn8.setText(QCoreApplication.translate("standard_mode_widget", u"8", None))
        self.standard_btn5.setText(QCoreApplication.translate("standard_mode_widget", u"5", None))
        self.standard_btn_C.setText(QCoreApplication.translate("standard_mode_widget", u"C", None))
        self.standard_btn7.setText(QCoreApplication.translate("standard_mode_widget", u"7", None))
        self.standard_btn9.setText(QCoreApplication.translate("standard_mode_widget", u"9", None))
        self.standard_btn4.setText(QCoreApplication.translate("standard_mode_widget", u"4", None))
        self.standard_btn6.setText(QCoreApplication.translate("standard_mode_widget", u"6", None))
        self.standard_btn1.setText(QCoreApplication.translate("standard_mode_widget", u"1", None))
        self.standard_btn_plus_minus.setText(QCoreApplication.translate("standard_mode_widget", u"+/_", None))
        self.standard_btn_point.setText(QCoreApplication.translate("standard_mode_widget", u".", None))
        self.standard_btn3.setText(QCoreApplication.translate("standard_mode_widget", u"3", None))
        self.standard_btn_delete.setText("")
        self.standard_btn0.setText(QCoreApplication.translate("standard_mode_widget", u"0", None))
        self.standard_btn_division.setText(QCoreApplication.translate("standard_mode_widget", u"/", None))
        self.standard_btn_multiplication.setText(QCoreApplication.translate("standard_mode_widget", u"X", None))
        self.standard_btn_equal.setText(QCoreApplication.translate("standard_mode_widget", u"=", None))
        self.standard_btn_minus.setText(QCoreApplication.translate("standard_mode_widget", u"-", None))
        self.standard_btn_addition.setText(QCoreApplication.translate("standard_mode_widget", u"+", None))
        self.standard_btn2.setText(QCoreApplication.translate("standard_mode_widget", u"2", None))
    # retranslateUi

