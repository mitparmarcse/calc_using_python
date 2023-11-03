# Import QApplication and the required widgets from PyQt5.QtWidgets

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

class GUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()

        # Set some main window's properties
        self.setWindowTitle('Calculator')
        self.setFixedSize(235, 235)

        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()

        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # Create the display and the buttons
        self._createDisplayLED()
        self._createButtons()

    def _createDisplayLED(self):
        """Create the display."""
        
        # Create the display widget
        self.display = QLineEdit()
        # Set some display's properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        
        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)
    


    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        # Button text | position on the QGridLayout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   'cm_mm':(4,0),
                   'mm_cm':(4,1),
                   'm_cm':(4,2),
                   'cm_m':(4,3),
                   'inch_cm':(4,4),
                   'cm_inch':(5,0),
                   #added buttons for added functionalites
                  }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')
    
    def mmToCm(self,expression):
        """Convert milimetre to centimeter"""
        result=expression/10
        self.setDisplayText(result)
        
    def cmTomm(self,expression):
        """Convert centimeter to milimetre"""
        result=expression*10
        self.setDisplayText(result)
    
    def mToCm(self,expression):
        """Convert metre to centimeter"""
        result=expression*100
        self.setDisplayText(result)
    
    def cmToM(self):
        """Convert centimeter to metre"""
        result=expression*100
        self.setDisplayText(result)

        
    def inchToCm(self):
        """Convert inch to centimeter"""
        result=expression*2.5
        self.setDisplayText(result)
    
    def cmToInch(self):
        """Convert centimeter to inch"""
        result=expression/2.65
        