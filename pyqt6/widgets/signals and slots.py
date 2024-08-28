"""PyQt6 widget signals"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt


# simple demonstration
# create a class for the main window
class MainWindow(QWidget):
    """application window"""

    def __init__(self):
        super().__init__()
        # set the window title
        self.setWindowTitle("Hello PyQt6")
        # set the window size and position
        self.setGeometry(100, 100, 800, 600)

        # create layout manager
        # the syntax creates and sets the layout to the MainWindow
        layout = QVBoxLayout(self)

        # alternative to the above syntax
        # layout = QVBoxLayout()
        # self.setLayout(layout)

        # set layout properties
        # place widgets at the center of the window
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # widgets
        self.status_label = QLabel("Status:")
        # add button with text "Change"
        self.button = QPushButton("Play")

        # set button properties
        self.button.setMinimumHeight(40)  # it doesn't get any smaller
        self.button.setMaximumWidth(120)  # it doesn't get bigger

        # hook button 'clicked' signal to a slot (function)
        # we start with 'play'
        self.button.clicked.connect(self.play)

        # add widgets to the layout manager
        layout.addWidget(self.status_label)
        layout.addWidget(self.button)

    def play(self):
        """
        called when button is clicked,
        change the status text to 'Playing'
        """
        self.button.clicked.disconnect(self.play)
        self.button.clicked.connect(self.pause)
        self.status_label.setText("Status: Playing")
        self.button.setText("Pause")

    def pause(self):
        """
        called when button is clicked,
        change the status text to 'Paused'
        """
        self.button.clicked.disconnect(self.pause)
        self.button.clicked.connect(self.play)
        self.status_label.setText("Status: Paused")
        self.button.setText("Play")


if __name__ == "__main__":
    # create the application object
    app = QApplication(sys.argv)
    # create an instance of the main window
    window = MainWindow()
    window.show()  # show the window
    sys.exit(app.exec())  # start the application's event loop
