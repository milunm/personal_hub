import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt  #import pyqt5 widgets and alignment constants
from PyQt5.QtGui import QIcon  # Import QIcon for icons


 # created main application window
class MainMenu(QMainWindow): 
    def __init__(self):  ##run constructor and initialise window
        super().__init__() #call constructor of parent class
        self.setWindowTitle("Milun's Personal Hub") 
        self.setGeometry(200, 200, 600, 150) #set window title and geometry

        # Layout setup
        layout = QVBoxLayout()
        layout.setSpacing(25)
        layout.setContentsMargins(50, 50, 50, 50)

        # Header label
        header = QLabel("Welcome to Milun's Personal Hub:")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: black; 
        """)

        # Buttons and icons added
        gymButton = QPushButton("Gym Track")
        gymButton.setIcon(QIcon("gym_icon.png"))
        
        flashcardButton = QPushButton("Flashcards")
        flashcardButton.setIcon(QIcon("flashcard_icon.png"))
                                
        financeButton = QPushButton("Financial Tracker")
        financeButton.setIcon(QIcon("money_icon.png"))

        gymButton.setFixedWidth(200)  # Set the width to 200 pixels
        flashcardButton.setFixedWidth(200)
        financeButton.setFixedWidth(200)
                                

        # Apply button styles
        button_style = """
            QPushButton {
                background-color: #333333; /* Semi-transparent black colour*/
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.8); /* Light hover effect for buttons */
                color: black;
            }
        """
        gymButton.setStyleSheet(button_style)
        flashcardButton.setStyleSheet(button_style)
        financeButton.setStyleSheet(button_style)

        # Add header widget to layout
        layout.addWidget(header)
        
        
        for item in [gymButton,flashcardButton, financeButton]:
            buttonLayout = QHBoxLayout()
            buttonLayout.addStretch()  # Add space on the left
            buttonLayout.addWidget(item)
            buttonLayout.addStretch()  # Add space on the right
            layout.addLayout(buttonLayout)

        # Create container and set layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv) #create application object to handle event loop

    # Global stylesheet with background image
    app.setStyleSheet("""
        QMainWindow {
            background-image: url("background.jpg"); 
            background-repeat: no-repeat; 
            background-position: center;
            background-size: cover; /* Ensures the image covers the whole window */
            
        }
        QLabel {
            color: white;
        }
    """)

    window = MainMenu() #create mainmenu instance
    window.show() #display window
    sys.exit(app.exec_()) #start app event loop
