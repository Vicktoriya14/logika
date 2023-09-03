from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
layout_form =  QFormLayout()

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form.addRow('питання:', txt_Question)
layout_form.addRow('правильна відповідь:', txt_Answer)
layout_form.addRow('неправильна відповідь 1:', txt_Wrong1)
layout_form.addRow('неправильна відповідь 2:', txt_Wrong2)
layout_form.addRow('неправильна відповідь 3:', txt_Wrong3)
