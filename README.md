# Basic Calculator using Python PyQt
This app is divided in three main parts as per MCV.
## 1: Create View: 
View is basically GUI of an application. In this calc it is grid of numbers and symbols.

## 2: Create Controller
It is a class that connects interactions between model and view

## 3: Create Model
This is business logic. In this calc it is just calculations of operations such as addition and multiplication.

# Steps
## 1: Install pyqt

## 2: Test installation
To check installation and basic woking of pyqt follow steps below
-- Create file test.py
```
import sys

from PyQt5.QtWidgets import QAplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
```
-- Go to CMD and run python test.py
If installtion is working this run will not give any error

-- Now add following lines to check how to create GUI in pyqt

This code is going to create GUI but will not retain window(When you run code it will show window and exit)
```
app = QApplication(sys.argv)

window = QWidget()
window.QLabel("This is Test", parent = window)
window.show()
```
-- To retain window add following code
```
sys.exit(app.exce_())
```

-- Also, add following code lines to experiment moe
```
window.setGeometry(100, 100, 280, 80) # It will set  x, y, w, h of app window
window.move(600,400) # Move window x from left and y from top
```
## 3: Create view of application i.e. GUI

## 4: Create Controller of application

## 5: Create Model of application
